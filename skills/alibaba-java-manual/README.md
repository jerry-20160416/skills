# 阿里巴巴 Java 开发手册 Skill

> 版本：1.7.1（黄山版）
> 来源：阿里巴巴集团技术团队
> 更新日期：2022.02.03

**📥 安装：** `npx skills add jerry-20160416/skills@alibaba-java-manual`

**🌐 在线浏览：** https://github.com/jerry-20160416/skills/tree/master/skills/alibaba-java-manual

## 📖 简介

本 Skill 基于阿里巴巴 Java 开发手册（黄山版）创建，是 Java 社区爱好者的集体智慧结晶和经验总结，经历了多次大规模一线实战的检验及不断完善。

手册以 Java 开发者为中心视角，涵盖从代码编写到系统设计的全方位规范，帮助你：
- ✅ 编写高质量、可维护的代码
- ✅ 提升团队协作效率，降低沟通成本
- ✅ 避免常见陷阱和错误
- ✅ 建立统一的编码标准

## 🎯 七大维度

### 一、编程规约
| 子分类 | 核心内容 |
|--------|----------|
| **命名风格** | 类名、方法名、变量名、常量名等命名规范 |
| **常量定义** | 常量的定义、使用、分层管理规范 |
| **代码格式** | 缩进、空格、换行、大括号等格式规范 |
| **OOP 规约** | 面向对象设计原则与实践 |
| **日期时间** | 日期时间的处理与格式化规范 |
| **集合处理** | 集合类的选择与使用规范 |
| **并发处理** | 多线程、锁、并发容器的使用规范 |
| **控制语句** | if/for/while/switch 等控制流规范 |
| **注释规约** | 类、方法、变量注释的编写规范 |
| **前后端规约** | API 设计、数据格式、命名约定 |
| **其他** | 其他编程相关最佳实践 |

### 二、异常日志
| 子分类 | 核心内容 |
|--------|----------|
| **错误码** | 错误码的定义、分类、管理规范 |
| **异常处理** | 异常捕获、抛出、转换的最佳实践 |
| **日志规约** | 日志级别、格式、输出的规范 |

### 三、单元测试
- 测试用例编写规范
- 测试覆盖率要求（100%）
- Mock 使用原则
- 测试命名约定

### 四、安全规约
- 权限控制与鉴权
- 敏感数据处理
- SQL 注入防护
- XSS/CSRF 防范

### 五、MySQL 数据库
| 子分类 | 核心内容 |
|--------|----------|
| **建表规约** | 表设计、字段类型、命名规范 |
| **索引规约** | 索引设计原则、使用规范 |
| **SQL 语句** | SQL 编写规范与性能优化 |
| **ORM 映射** | MyBatis 等 ORM 框架使用规范 |

### 六、工程结构
| 子分类 | 核心内容 |
|--------|----------|
| **应用分层** | 三层架构、领域模型设计 |
| **二方库依赖** | 依赖管理、版本控制 |
| **服务器** | 部署配置、性能调优 |

### 七、设计规约
- 系统设计原则
- 模块划分规范
- 接口设计最佳实践
- 设计模式应用

## 📊 规约等级

| 等级 | 标识 | 说明 |
|------|------|------|
| **强制** | 【强制】 | 必须遵守，违反将导致严重问题或故障 |
| **推荐** | 【推荐】 | 建议遵守，有助于提升代码质量和可维护性 |
| **参考** | 【参考】 | 可选遵守，根据实际情况灵活处理 |

## 🚀 安装使用

### 安装 Skill

```bash
npx skills add jerry-20160416/skills@alibaba-java-manual
```

### 使用方式

安装后，Agent 会自动加载此 Skill，你可以直接询问相关规范问题：

**命名相关：**
```
"类名应该怎么命名？"
"常量的命名规范是什么？"
"枚举类的命名规范是什么？"
```

**代码格式：**
```
"代码缩进用几个空格？"
"大括号的格式规范是什么？"
"单行代码长度限制是多少？"
```

**异常处理：**
```
"如何正确地捕获和处理异常？"
"错误码应该如何定义？"
"日志输出的规范是什么？"
```

**数据库：**
```
"MySQL 建表有哪些规范？"
"索引设计有哪些原则？"
"SQL 语句如何编写？"
```

**并发编程：**
```
"多线程编程有哪些注意事项？"
"线程池如何正确使用？"
"锁的使用规范是什么？"
```

## 📝 规约示例

### 命名风格示例

```java
// ✅ 正例：类名使用 UpperCamelCase
public class UserService {}
public class UserDO {}
public class OrderDTO {}

// ❌ 反例：类名不规范
public class userservice {}
public class userDo {}

// ✅ 正例：常量全大写，下划线分隔
public static final int MAX_STOCK_COUNT = 1000;
public static final String CACHE_EXPIRED_TIME = "3600";

// ❌ 反例：常量命名不规范
public static final int maxCount = 1000;

// ✅ 正例：方法名使用 lowerCamelCase
public void getUserById() {}
public void calculateTotalAmount() {}

// ❌ 反例：方法名不规范
public void GetUserById() {}
public void get_user_by_id() {}
```

### 常量定义示例

```java
// ❌ 反例：魔法值直接出现在代码中
if (user.getStatus() == 1) {
    // ...
}

// ✅ 正例：使用预定义常量
public static final int STATUS_ACTIVE = 1;
if (user.getStatus() == STATUS_ACTIVE) {
    // ...
}
```

### 代码格式示例

```java
// ✅ 正例：正确的代码格式
public static void main(String[] args) {
    // 缩进 4 个空格
    String say = "hello";
    // 运算符左右必须有空格
    int flag = 0;
    // 关键词 if 与括号之间必须有空格
    if (flag == 0) {
        System.out.println(say);
    }
    // 左大括号前加空格且不换行
    if (flag == 1) {
        System.out.println("world");
    } else {
        System.out.println("ok");
    }
}
```

### 集合处理示例

```java
// ❌ 反例：在 foreach 循环中进行 remove/add 操作
List<String> list = new ArrayList<>();
for (String item : list) {
    if (condition) {
        list.remove(item); // 会抛出 ConcurrentModificationException
    }
}

// ✅ 正例：使用 Iterator 进行删除
Iterator<String> iterator = list.iterator();
while (iterator.hasNext()) {
    String item = iterator.next();
    if (condition) {
        iterator.remove();
    }
}
```

### 并发处理示例

```java
// ✅ 正例：线程池的正确使用方式
public class ThreadPoolConfig {
    private static final int CORE_POOL_SIZE = 5;
    private static final int MAX_POOL_SIZE = 10;
    private static final int QUEUE_CAPACITY = 100;
    
    public static ThreadPoolExecutor getExecutor() {
        return new ThreadPoolExecutor(
            CORE_POOL_SIZE,
            MAX_POOL_SIZE,
            60L,
            TimeUnit.SECONDS,
            new LinkedBlockingQueue<>(QUEUE_CAPACITY),
            new ThreadFactoryBuilder().setNameFormat("my-thread-%d").build(),
            new ThreadPoolExecutor.CallerRunsPolicy()
        );
    }
}

// ❌ 反例： Executors 返回的线程池对象的弊端
ExecutorService executor = Executors.newFixedThreadPool(5); // 允许的请求队列长度为 Integer.MAX_VALUE，可能堆积大量请求
ExecutorService executor = Executors.newCachedThreadPool(); // 允许的创建线程数量为 Integer.MAX_VALUE，可能创建大量线程
```

## 🔍 快速检索

### 常见问题快速索引

| 问题 | 答案 |
|------|------|
| 类名命名规范？ | UpperCamelCase 风格，如 `UserService`、`UserDO` |
| 方法名命名规范？ | lowerCamelCase 风格，如 `getUserById()` |
| 常量命名规范？ | 全大写，下划线分隔，如 `MAX_COUNT` |
| 代码缩进？ | 4 个空格，禁止使用 Tab |
| 单行代码长度限制？ | 不超过 120 个字符 |
| 大括号格式？ | 左大括号前不换行，后换行；右大括号前换行 |
| 单元测试覆盖率？ | 要求 100% |
| 布尔类型变量命名？ | 不要加 is 前缀，如 `deleted` 而非 `isDeleted` |
| Long 类型赋值？ | 数值后使用大写 L，如 `2L` 而非 `2l` |

## 📚 相关资源

- [阿里巴巴 Java 开发手册官方网站](https://github.com/alibaba/p3c)
- [Java 开发手册 IDE 插件](https://plugins.jetbrains.com/plugin/10046-alibaba-java-coding-guidelines)
- [《码出高效》图书](https://book.douban.com/subject/30333948/)

## 🤝 贡献

本 Skill 基于阿里巴巴 Java 开发手册（黄山版）创建，内容由阿里巴巴官方团队维护。如有疑问或建议，请参考官方仓库。

## 📜 版本历史

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.7.1 | 2022.02.03 | 黄山版，新增 11 条新规约 |
| 1.7.0 | 2020.04.22 | 嵩山版，新增 21 条新规约 |
| 1.6.0 | 2019.06.19 | 泰山版，新增 34 条新规约 |
| 1.5.0 | 2018.06.15 | 华山版，新增 16 条新规约 |

## 📄 License

本手册内容由阿里巴巴集团发布，遵循 Apache License 2.0。

---

**愿景**：码出高效，码出质量。

**理念**：无规矩不成方圆，无规范难以协同。适当的规范和标准绝不是消灭代码内容的创造性、优雅性，而是限制过度个性化，以一种普遍认可的统一方式一起做事，提升协作效率，降低沟通成本。
