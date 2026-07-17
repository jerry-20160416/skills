# Spring Boot 分层完整示例(模块化 + gateway 防腐)

演示 `user` 模块自洽分层 + `order` 模块**跨模块经 `UserGateway`** 调用 user。Spring Boot 3 + MyBatis-Plus + Lombok + Bean Validation。

包结构(业务模块优先):
```
com.example
  common/                      # 跨模块共享
    Result.java  ErrorCode.java  BusinessException.java  GlobalExceptionHandler.java
  user/                        # user 业务模块
    controller/UserController.java
    gateway/UserGateway.java
    scheduler/UserScheduler.java
    service/UserService.java
    service/impl/UserServiceImpl.java
    mapper/UserMapper.java
    domain/po/UserPo.java
    domain/dto/UserDto.java
    domain/vo/reqVo/UserCreateReqVo.java
    domain/vo/respVo/UserRespVo.java
  order/
    service/impl/OrderServiceImpl.java   # 跨模块调 UserGateway
resources/mapper/user/UserMapper.xml
```

## common(跨模块共享,节选)

```java
@Data @AllArgsConstructor
public class Result<T> {
    private int code; private String message; private T data;
    public static <T> Result<T> success(T d) { return new Result<>(0, "success", d); }
    public static <T> Result<T> fail(ErrorCode e) { return new Result<>(e.getCode(), e.getMessage(), null); }
}
// ErrorCode: 1000x 业务 / 4000x 参数 / 5000x 系统
// BusinessException(ErrorCode) extends RuntimeException
// GlobalExceptionHandler @RestControllerAdvice: BusinessException→200, MethodArgumentNotValidException→200, DuplicateKeyException→200, Exception→500
```
(完整实现见上一版示例的 common 块,结构不变。)

## user/domain/po/UserPo(与表一一对应)

```java
package com.example.user.domain.po;

import com.baomidou.mybatisplus.annotation.*;
import lombok.Data;
import java.time.LocalDateTime;

@Data
@TableName("user")
public class UserPo {
    @TableId(type = IdType.AUTO)
    private Long id;
    private String username;
    private String email;
    @TableField(fill = FieldFill.INSERT)
    private LocalDateTime createTime;
}
```

## user/mapper/UserMapper + XML

```java
package com.example.user.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.example.user.domain.po.UserPo;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface UserMapper extends BaseMapper<UserPo> { }   // 只返 UserPo
```

`resources/mapper/user/UserMapper.xml`(自定义 SQL 走这里,不用注解散落):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.example.user.mapper.UserMapper">
    <!-- 自定义查询写这里,resultType 用 UserPo -->
</mapper>
```
`application.yml`:`mybatis-plus.mapper-locations=classpath*:mapper/**/*.xml`

## user/domain/dto/UserDto(跨模块传输)

```java
package com.example.user.domain.dto;

import lombok.Data;

@Data
public class UserDto {
    private Long id;
    private String username;
    private String email;
}
```

## user/domain/vo/reqVo + respVo

```java
package com.example.user.domain.vo.reqVo;

import jakarta.validation.constraints.*;
import lombok.Data;

@Data
public class UserCreateReqVo {              // 校验在 reqVo,不在 po
    @NotBlank(message = "用户名不能为空") @Size(max = 64)
    private String username;
    @NotBlank(message = "邮箱不能为空") @Email(message = "邮箱格式不正确")
    private String email;
}
```

```java
package com.example.user.domain.vo.respVo;

import com.example.user.domain.dto.UserDto;
import lombok.Data;
import java.time.LocalDateTime;

@Data
public class UserRespVo {
    private Long id;
    private String username;
    private String email;
    private LocalDateTime createTime;

    public static UserRespVo of(UserDto d) {     // dto→respVo 转换(供 controller 路径)
        if (d == null) return null;
        UserRespVo v = new UserRespVo();
        v.setId(d.getId()); v.setUsername(d.getUsername()); v.setEmail(d.getEmail());
        return v;
    }
}
```

## user/service/UserService(接口:web 路径返回 respVo,gateway 路径返回 dto)

```java
package com.example.user.service;

import com.example.user.domain.dto.UserDto;
import com.example.user.domain.vo.reqVo.UserCreateReqVo;
import com.example.user.domain.vo.respVo.UserRespVo;

public interface UserService {
    UserRespVo create(UserCreateReqVo req);   // controller 调,返回 respVo
    UserRespVo getById(Long id);              // controller 调,返回 respVo
    UserDto getForModule(Long id);           // gateway 调,返回 dto(跨模块)
}
```

## user/service/impl/UserServiceImpl(事务+转换都在这)

```java
package com.example.user.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.example.user.domain.dto.UserDto;
import com.example.user.domain.po.UserPo;
import com.example.user.domain.vo.reqVo.UserCreateReqVo;
import com.example.user.domain.vo.respVo.UserRespVo;
import com.example.user.mapper.UserMapper;
import com.example.user.service.UserService;
import com.example.common.BusinessException;
import com.example.common.ErrorCode;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@RequiredArgsConstructor
public class UserServiceImpl implements UserService {

    private final UserMapper userMapper;     // 注入 mapper;跨模块需求注入他模块 gateway

    @Override
    @Transactional(rollbackFor = Exception.class)        // 写方法才加事务
    public UserRespVo create(UserCreateReqVo req) {
        boolean exists = userMapper.exists(
                new LambdaQueryWrapper<UserPo>().eq(UserPo::getUsername, req.getUsername()));
        if (exists) throw new BusinessException(ErrorCode.USERNAME_DUPLICATE);
        UserPo po = new UserPo();
        po.setUsername(req.getUsername());
        po.setEmail(req.getEmail());
        userMapper.insert(po);
        return UserRespVo.of(toDto(po));                  // po→dto→respVo 转换在 serviceImpl
    }

    @Override
    public UserRespVo getById(Long id) {                  // 查询不加事务
        return UserRespVo.of(getForModule(id));           // 复用 getForModule,转 respVo
    }

    @Override
    public UserDto getForModule(Long id) {               // gateway 调,返 dto
        UserPo po = userMapper.selectById(id);
        if (po == null) throw new BusinessException(ErrorCode.USER_NOT_FOUND);
        return toDto(po);
    }

    private UserDto toDto(UserPo po) {                   // po→dto 私有转换
        UserDto d = new UserDto();
        d.setId(po.getId()); d.setUsername(po.getUsername()); d.setEmail(po.getEmail());
        return d;
    }
}
```

## user/gateway/UserGateway(防腐层,只调 service,返回 dto)

```java
package com.example.user.gateway;

import com.example.user.domain.dto.UserDto;
import com.example.user.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;

@Component
@RequiredArgsConstructor
public class UserGateway {

    private final UserService userService;               // 只注入 service,绝不注入 mapper

    public UserDto getById(Long id) {                   // 给他模块调,返回 dto
        return userService.getForModule(id);
    }
    // 方法体只允许出现 userService.xxx();严禁 userMapper./cache./转换
}
```

## user/controller/UserController(极薄,调 service,不调 gateway)

```java
package com.example.user.controller;

import com.example.common.Result;
import com.example.user.domain.vo.reqVo.UserCreateReqVo;
import com.example.user.domain.vo.respVo.UserRespVo;
import com.example.user.service.UserService;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/user")
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;              // 注入 service,不注入 gateway

    @PostMapping
    public Result<UserRespVo> create(@Valid @RequestBody UserCreateReqVo req) {
        return Result.success(userService.create(req));
    }

    @GetMapping("/{id}")
    public Result<UserRespVo> getById(@PathVariable Long id) {
        return Result.success(userService.getById(id));
    }
}
```

## user/scheduler/UserScheduler(定时入口,只调 service;非 Web 入口,异常自记日志)

```java
package com.example.user.scheduler;

import com.example.user.service.UserService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Slf4j
@Component
@RequiredArgsConstructor
public class UserScheduler {

    private final UserService userService;               // 只调 service,绝不注入 mapper

    @Scheduled(cron = "0 0 2 * * ?")                    // 每天凌晨 2 点
    public void cleanExpiredUsers() {
        try {                                           // 非 Web 入口,RestControllerAdvice 不兜底:
            userService.cleanExpired();                 //   try-catch 仅记日志,不得吞异常继续业务
        } catch (Exception e) {
            log.error("清理过期用户任务失败", e);
        }
    }
}
```

> `@EnableScheduling` 标在主启动类(或 `common` 的全局 config);`cleanExpired()` 是 UserService 上一个普通业务方法(写方法加 `@Transactional`),scheduler 只决定"何时调"。业务逻辑、事务、mapper 调用全在 serviceImpl。

## order/service/impl/OrderServiceImpl(跨模块:注入 UserGateway,不注入 UserService)

```java
package com.example.order.service.impl;

import com.example.user.gateway.UserGateway;            // 跨模块只依赖他模块 gateway
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class OrderServiceImpl {                         // (略去 OrderService 接口,结构同 user)
    private final UserGateway userGateway;              // ✓ 注入 gateway
    // ✗ 禁止:private final UserService userService;   // 跨模块直调 service = 强耦合
    // ✗ 禁止:private final UserMapper userMapper;     // 跨模块直调 mapper = 泄漏

    public void doSomething(Long userId) {
        var user = userGateway.getById(userId);         // 拿到 UserDto,不是 UserPo
    }
}
```

## 提交前自检清单

- [ ] 包是 `com.example.<module>.<技术层>`,没有 `com.example.controller` 这种技术大包
- [ ] 跨模块只注入他模块的 `XxxGateway`,不注入 `XxxService`/`XxxMapper`
- [ ] service 不注入非本功能 `XxxMapper`(关联表/中间表例外),跨模块走 gateway
- [ ] gateway 方法体只有 `xxxService.` 调用,无 mapper/cache/转换
- [ ] controller 方法体无 `xxxGateway.`、无 `try/catch`、无 `new XxxRespVo()`
- [ ] scheduler 只调 service(无 `xxxMapper.`/业务逻辑);异常 try-catch 仅记日志不吞;`@Scheduled` 不标在 service/mapper
- [ ] `XxxPo` 只在 mapper/service;controller 出参是 `XxxRespVo`,跨模块返回是 `XxxDto`
- [ ] service 有接口+Impl,写方法有 `@Transactional(rollbackFor=Exception.class)`,查询无
- [ ] 校验注解在 reqVo,不在 po
- [ ] 业务异常走 `BusinessException`,由 `@RestControllerAdvice` 兜底,业务 200 / 系统 500
- [ ] mapper XML 放 resources/mapper/<module>/,已配 mapper-locations