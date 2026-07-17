---
name: backend-architecture
description: Use when 后端接口开发或 review Spring Boot + MyBatis-Plus 的分层与分包;新增业务模块/接口、写 controller/gateway/scheduler/service/mapper/domain 各层、写定时任务、code review 后端、或发现跨模块直调 service/mapper、PO 泄漏、技术分包与业务分包混用、异常未统一处理、事务加错层等问题时。
---

# 后端架构规范

> Spring Boot + MyBatis-Plus 后端分层与分包规范

## Overview

**先按业务模块(功能)分包,模块内部再按技术分层**。每个业务模块是一个自洽单元,对外仅暴露 **gateway(防腐层)**;跨模块调用必经 gateway,不得直调他模块的 service/mapper。模块内调用链:**controller / gateway / scheduler → service(接口+Impl) → mapper**;入口层(controller/gateway/scheduler)都只调 service,严禁调 mapper 或其他类。配套统一 `Result<T>` + 全局异常处理,Controller 极薄。

## When to Use

- 新增业务模块或接口,需要规划包结构/写任一层代码
- code review 后端,判断分包与调用是否合规
- 出现:跨模块直调 service/mapper、PO 泄漏到前端、技术分包与业务分包混用、Controller try-catch、事务加错层、gateway 调 mapper、定时任务里写业务逻辑或吞异常

**不适用**:非 Web 入口(定时任务、MQ 消费)顶层调度,但仍按模块组织、入口→service→mapper。

## 模块内技术分包

每个业务模块包 `com.example.<module>`(如 `com.example.user`)下:

| 子包 | 职责 |
|---|---|
| `controller` | Web 入口,`@RestController`,只调本模块 service |
| `gateway` | 对外防腐层,供**他模块**调用,只调本模块 service,返回 dto |
| `scheduler` | 定时调度入口,`@Scheduled`(`@EnableScheduling` 开启),只调本模块 service;非 Web 入口,`@RestControllerAdvice` 不兜底,异常自行 try-catch 记日志 |
| `service` | 业务接口(必须接口+Impl) |
| `service.impl` | `@Service` 实现,业务逻辑+事务+对象转换,调 mapper/cache/util/他模块 gateway |
| `mapper` | dao,`extends BaseMapper<Po>`,只返 Po |
| `mapper.xml` | MyBatis XML(放 `resources` 下对应路径,配 `mybatis-plus.mapper-locations`) |
| `domain.vo.reqVo` | 前端请求实体(带 Bean Validation) |
| `domain.vo.respVo` | 返回前端实体 |
| `domain.dto` | 模块内/跨模块传输实体 |
| `domain.po` | 与数据库表一一对应(`@TableName`) |
| `cache` | 缓存层(Redis 等) |
| `listener` | MQ 消费者 |
| `config` | 模块内配置 |
| `util` | 模块内公共类 |

跨模块共享(`Result`/`ErrorCode`/`BusinessException`/`GlobalExceptionHandler`/全局 `config`)放 `com.example.common` 或 `com.example.framework`,不属于任何业务模块。

## 对象流转(po ↔ dto ↔ vo)

```
前端 ─reqVo→ controller ─reqVo→ service
                              service 内部: mapper ─po→ service,转 dto/respVo
controller ←respVo─ service        他模块 ─(调 gateway)→ gateway ─dto→ 他模块
                                    gateway 内部: gateway → service(返回 dto)
```

- **po**:只在 mapper↔service 之间,不出去。
- **dto**:service 内部载体、跨模块经 gateway 传输(he模块只拿到 dto)。
- **reqVo**:controller 入参。
- **respVo**:controller 出参。被 controller 调用的 service 方法返回 respVo;被 gateway 调用的 service 方法返回 dto。
- 转换全部在 **serviceImpl**:po↔dto↔respVo,用静态 `of()` 或 MapStruct(字段 >8 个)。

## 调用规范(铁律)

1. **先业务分包,再技术分包**:禁止 `com.example.controller` / `com.example.service` 这种跨模块技术大包;每个模块自洽。
2. **模块内**:controller → service(接口) → mapper。controller、gateway、scheduler 都只调 service。
3. **跨模块**:本模块 service 调他模块的 **gateway**(返回 dto),**禁止**直调他模块的 service/mapper。
4. **gateway 只调 service**:gateway 方法体只能出现 `xxxService.` 调用;严禁调 mapper/cache/util/domain 转换以外的他类;gateway 是薄壳,不含业务逻辑。
5. **service 必须接口+Impl**:统一 `XxxService`+`XxxServiceImpl`(`@Service`),注入接口不注入 Impl。
6. **对象不出边界**:po 不出 mapper/service;respVo 不出 controller;dto 可经 gateway 出模块。
7. **Controller 不碰异常**:业务异常 `throw new BusinessException(ErrorCode.XXX)`,由 `@RestControllerAdvice` 兜底,Controller 方法体不得 try-catch。
8. **事务在 ServiceImpl 写方法**:`@Transactional(rollbackFor = Exception.class)`,查询不加(或 `readOnly = true`)。禁止加在 controller/gateway/scheduler/mapper/listener。
10. **scheduler 是非 Web 入口**:`@RestControllerAdvice` 兜不到它,scheduler 方法可 try-catch **仅用于记日志/告警**,不得吞异常后继续走业务流程;业务逻辑仍在 service。`@Scheduled` 注解只标在 scheduler,不标在 service/mapper。
9. **校验在 reqVo**:Bean Validation 注解放 reqVo,不放 po。
11. **Service 数据依赖优先走 service 层,少依赖非本功能的 mapper**:跨功能模块取数走对方 **gateway**(返 dto),不直接注入对方 mapper;同模块内需要兄弟 service 的逻辑时调 service,不绕过去用其 mapper。**例外**:关联表/中间表(与本功能强相关的)mapper 可直接注入使用,不必经 gateway 绕行。

## 统一返回 Result<T>

```java
@Data @AllArgsConstructor
public class Result<T> {
    private int code;        // 0=成功,非0=错误码
    private String message;
    private T data;
    public static <T> Result<T> success(T d) { return new Result<>(0, "success", d); }
    public static <T> Result<T> fail(ErrorCode e) { return new Result<>(e.getCode(), e.getMessage(), null); }
}
```

- 成功 `code=0`;错误码 5 位分段:`1000x` 业务、`4000x` 参数、`5000x` 系统。
- **HTTP 状态**:业务异常返 **200 + 业务码**(前端看 `code`);仅未捕获系统异常返 **500**。
- Controller **显式**声明 `Result<T>` 返回类型,不用 `ResponseBodyAdvice` 自动包装。

## 全局异常处理

`@RestControllerAdvice` 放 `common` 包,至少处理:`BusinessException`→`Result.fail`(200)、`MethodArgumentNotValidException`→参数错误(200)、`DuplicateKeyException`→业务码(200,并发兜底)、`Exception`→系统错误(500)。Controller 不得自行 catch 这些。

## Common Mistakes

| 借口 | 现实 |
|---|---|
| "跨模块要查用户,直接注入 UserService 省事" | 必须经 `UserGateway`;直调 service 让模块强耦合,改实现/拆服务时他模块全炸 |
| "gateway 里直接调 mapper 取数据更快" | gateway 只调 service,否则绕过业务/事务/缓存,防腐层失效 |
| "controller 调 gateway 复用跨模块逻辑" | controller 调本模块 service;gateway 是给他模块用的,不是给同模块 controller |
| "技术分包统一放 com.example.controller 多整齐" | 必须业务分包优先;技术大包让模块边界消失,无法独立演进 |
| "po 直接返回前端省得转 respVo" | po 出 controller = 表结构泄漏,加字段即暴露;respVo 是稳定契约 |
| "Service 就一个实现,不拆接口" | 统一接口+Impl;注入接口便于 Mock/AOP,不注入 Impl |
| "查询也加 @Transactional 保险" | 写方法才加,且 `rollbackFor = Exception.class`(否则受检异常不回滚) |
| "校验注解加 po 上" | 校验放 reqVo;po 是 DB 映射 |
| "在 serviceImpl 里手动 setCreateTime/setUpdateTime" | 审计字段由 `@TableField(fill=...)` + `MetaObjectHandler` 自动填充,手写 set 会漏(批量/其他入口未覆盖)、且重复 |
| "定时任务里直接调 mapper/写业务逻辑" | scheduler 是入口层,只调 service;业务在 service,事务在 service,scheduler 只负责"何时调" |
| "定时任务 try-catch 把异常吞了当没发生" | 非要 try-catch 只为记日志/告警;吞异常会导致任务静默失败、无监控、问题攒到爆 |
| "@Scheduled 加在 service 方法上,复用方便" | 调度入口放 scheduler 层;service 不感知调度方式,便于复用、单测与替换触发方式 |
| "两个模块 service 互相调" | 跨模块走 gateway;循环依赖是设计问题,抽公共模块或事件解耦 |
| "在 OrderService 里直接注入 UserMapper 查用户,省一次 gateway 调用" | 跨功能取数走 `UserGateway`;直注入 `UserMapper` 穿透模块边界,User 改表/拆服务时 Order 跟着炸 |
| "同模块 AdminService 要查用户,直接注入 UserMapper" | 调 `UserService` 复用其逻辑,不重复依赖 mapper;多个 service 各自注入同一 mapper 会散落查询、难统一 |
| "关联表也强行走 gateway 才算规范" | 关联表/中间表 mapper 可直接用,强走 gateway 是过度设计;但非关联的他表 mapper 仍禁止 |

## Red Flags — 出现即停并修正

- 包名 `com.example.controller` / `com.example.service`(技术大包,非模块化)
- 跨模块注入他模块的 `XxxService` / `XxxMapper`(应注入 `XxxGateway`)
- ServiceImpl 注入非本功能的 `XxxMapper`(关联表/中间表除外;应走 gateway 或本模块 service)
- gateway 方法体出现 `xxxMapper.` / `xxxCache.` / `new XxxDto()` 转换(只允许 `xxxService.`)
- controller 方法体出现 `xxxGateway.` 调用
- `XxxPo` 类型出现在 controller / gateway 出参,或跨模块返回
- controller 出现 `try { } catch`
- `@Transactional` 标在 controller/gateway/scheduler/mapper/listener 或查询方法
- scheduler 方法体出现 `xxxMapper.` 或业务逻辑(循环/计算/分支业务);`@Scheduled` 标在 service/mapper 上;scheduler try-catch 吞异常后继续
- ServiceImpl 注入 `XxxServiceImpl` 而非接口

## 完整示例

见 `layering-example.md`:`user` 模块(含 gateway)完整分层 + `order` 模块跨模块调 `UserGateway` 的演示 + 提交前自检清单。**实际写代码时加载参考**,不要凭记忆。