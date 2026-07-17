---
name: alibaba-java-manual
description: "阿里巴巴Java开发手册（黄山版 1.7.1）- 当编写/审查 Java 代码、制定编码规范、处理异常日志、编写单元测试、设计数据库表与索引、规划工程分层或系统架构时，按场景定位应遵守的规约。详细规约正文见 references/ 目录。"
origin: Alibaba
version: 1.7.1
---

# 阿里巴巴 Java 开发手册（黄山版）

> 码出高效，码出质量。本 Skill 只描述**什么情况下需要什么规范**及对应参考文档；规约正文（含说明/正例/反例）见 `references/` 目录各文件。

## 何时激活此 Skill

- 编写或审查 Java 代码时（命名、格式、OOP、集合、并发、控制语句、注释）
- 处理异常、日志、错误码时
- 编写单元测试、评估测试覆盖率时
- 做安全审计、权限校验、敏感数据脱敏时
- 设计 MySQL 表结构、索引、编写 SQL、使用 ORM 时
- 规划工程分层、二方库依赖、服务器配置时
- 进行系统设计、用例/状态/时序/类/活动图选型时
- 制定项目编码规范、团队开发标准、Code Review 时

## 规约等级

| 等级 | 标识 | 含义 |
|------|------|------|
| **强制** | 【强制】 | 必须遵守，违反将导致故障或严重问题 |
| **推荐** | 【推荐】 | 建议遵守，提升质量与可维护性 |
| **参考** | 【参考】 | 可选遵守，按实际情况灵活处理 |

---

## 场景速查：什么情况查什么规范

按场景定位需要遵守的规约及对应参考文档。**审查/编写代码时对照下表，命中即去对应 `references/` 文件查阅正例反例。**

### 1. 命名

| 场景 | 规约要点 | 参考文档 |
|------|----------|----------|
| 给类/接口命名 | UpperCamelCase；DO/PO/DTO/BO/VO/UID 例外 | [01 § 命名风格](references/01-coding-conventions.md) |
| 给方法/变量/参数命名 | lowerCamelCase | [01 § 命名风格](references/01-coding-conventions.md) |
| 给常量命名 | 全大写+下划线，语义完整不嫌长（MAX_STOCK_COUNT） | [01 § 命名风格](references/01-coding-conventions.md) |
| 命名是否可用下划线/美元符开头结尾 | 禁止 | [01 § 命名风格](references/01-coding-conventions.md) |
| 命名是否可拼音英文混用/纯中文 | 禁止；国际通用名（taobao/hangzhou）可视同英文 | [01 § 命名风格](references/01-coding-conventions.md) |
| 命名是否可用歧视性词语 | 禁止（blackList→blockList，slave→secondary） | [01 § 命名风格](references/01-coding-conventions.md) |
| 布尔变量是否加 is 前缀 | POJO 禁止加 is（防框架序列化错误） | [01 § 命名风格](references/01-coding-conventions.md) |
| 抽象类/异常类/测试类命名 | 抽象类 Abstract/Base 开头；异常 Exception 结尾；测试 Test 结尾 | [01 § 命名风格](references/01-coding-conventions.md) |
| 数组定义方式 | `int[] arrayDemo`（类型紧挨中括号） | [01 § 命名风格](references/01-coding-conventions.md) |
| 包名规范 | 全小写、点分隔单数、单词 | [01 § 命名风格](references/01-coding-conventions.md) |
| Service/DAO 接口与实现命名 | 实现类用 Impl 后缀与接口区分 | [01 § 命名风格](references/01-coding-conventions.md) |
| 枚举类与成员命名 | 类名带 Enum 后缀；成员全大写下划线 | [01 § 命名风格](references/01-coding-conventions.md) |
| 各层方法命名 | get/list/count/save·insert/remove·delete/update 前缀 | [01 § 命名风格](references/01-coding-conventions.md) |
| 领域模型命名 | xxxDO/xxxDTO/xxxVO；禁止 xxxPOJO | [01 § 命名风格](references/01-coding-conventions.md) |

### 2. 常量

| 场景 | 规约要点 | 参考文档 |
|------|----------|----------|
| 代码中出现未定义的字面量 | 禁止魔法值，必须预定义常量 | [01 § 常量定义](references/01-coding-conventions.md) |
| long 赋值后缀 | 大写 L，禁止小写 l | [01 § 常量定义](references/01-coding-conventions.md) |
| 浮点数后缀 | 统一大写 D/F | [01 § 常量定义](references/01-coding-conventions.md) |
| 常量类组织 | 按功能归类分开维护，禁止一个大而全常量类 | [01 § 常量定义](references/01-coding-conventions.md) |
| 固定范围取值变量 | 优先用 enum | [01 § 常量定义](references/01-coding-conventions.md) |

### 3. 代码格式

| 场景 | 规约要点 | 参考文档 |
|------|----------|----------|
| 大括号/缩进/空格/换行 | 非空块左括号前不换行后换行；4 空格缩进禁 Tab | [01 § 代码格式](references/01-coding-conventions.md) |
| 运算符/关键词空格 | 二目三目运算符两边加空格；if/for/while 与括号间加空格 | [01 § 代码格式](references/01-coding-conventions.md) |
| 单行长度 | 不超 120 字符，超长按规则换行 | [01 § 代码格式](references/01-coding-conventions.md) |
| 方法行数 | 单方法不超 80 行 | [01 § 代码格式](references/01-coding-conventions.md) |
| 文件编码/换行符 | UTF-8；Unix 换行 | [01 § 代码格式](references/01-coding-conventions.md) |
| 方法参数逗号后 | 必须加空格 | [01 § 代码格式](references/01-coding-conventions.md) |

### 4. OOP

| 场景 | 规约要点 | 参考文档 |
|------|----------|----------|
| 覆写父类方法 | 必须 @Override | [01 § OOP 规约](references/01-coding-conventions.md) |
| equals 调用 | 常量或确定有值对象调 equals；推荐 Objects#equals | [01 § OOP 规约](references/01-coding-conventions.md) |
| 整型包装类比较 | 用 equals 不用 == | [01 § OOP 规约](references/01-coding-conventions.md) |
| 浮点数等值判断 | 禁 == 与 equals；用误差范围或 BigDecimal | [01 § OOP 规约](references/01-coding-conventions.md) |
| BigDecimal 比较 | 用 compareTo 不用 equals | [01 § OOP 规约](references/01-coding-conventions.md) |
| BigDecimal 构造 | 禁 BigDecimal(double)；用 String 构造或 valueOf | [01 § OOP 规约](references/01-coding-conventions.md) |
| DO 属性类型与字段类型 | 必须匹配（bigint→Long） | [01 § OOP 规约](references/01-coding-conventions.md) |
| POJO/局部变量基本类型 vs 包装类型 | POJO 与 RPC 必须包装类型；局部变量推荐基本类型 | [01 § OOP 规约](references/01-coding-conventions.md) |
| POJO 默认值/toString/serialVersionUID | 不设默认值；必须 toString；新增属性不改 serialVersionUID | [01 § OOP 规约](references/01-coding-conventions.md) |
| POJO 是否同时有 isXxx/getXxx | 禁止并存 | [01 § OOP 规约](references/01-coding-conventions.md) |
| 构造方法是否含业务逻辑 | 禁止，放 init 方法 | [01 § OOP 规约](references/01-coding-conventions.md) |
| 循环内字符串拼接 | 用 StringBuilder.append | [01 § OOP 规约](references/01-coding-conventions.md) |
| 访问控制从严 | 工具类无私有构造；成员最小可见性 | [01 § OOP 规约](references/01-coding-conventions.md) |

### 5. 日期时间

| 场景 | 规约要点 | 参考文档 |
|------|----------|----------|
| 日期格式化年份 | 小写 y（禁 YYYY 跨年） | [01 § 日期时间](references/01-coding-conventions.md) |
| 月/分/时大小写 | 月=M，分=m，24时=H，12时=h | [01 § 日期时间](references/01-coding-conventions.md) |
| 取毫秒数 | System.currentTimeMillis()，禁 new Date().getTime() | [01 § 日期时间](references/01-coding-conventions.md) |
| java.sql.Date/Time/Timestamp | 禁止使用 | [01 § 日期时间](references/01-coding-conventions.md) |
| 硬编码一年 365 天 | 禁止，用 LocalDate.lengthOfYear() | [01 § 日期时间](references/01-coding-conventions.md) |

### 6. 集合

| 场景 | 规约要点 | 参考文档 |
|------|----------|----------|
| 覆写 equals 是否覆写 hashCode | 必须同时覆写 | [01 § 集合处理](references/01-coding-conventions.md) |
| 判集合是否空 | isEmpty()，禁 size()==0 | [01 § 集合处理](references/01-coding-conventions.md) |
| Stream toMap 重复 key | 必须传 mergeFunction | [01 § 集合处理](references/01-coding-conventions.md) |
| Stream toMap value 为 null | 会抛 NPE，注意防范 | [01 § 集合处理](references/01-coding-conventions.md) |
| subList 强转 ArrayList | 禁止 | [01 § 集合处理](references/01-coding-conventions.md) |
| 集合转数组 | toArray(new T[0]) | [01 § 集合处理](references/01-coding-conventions.md) |
| Arrays.asList 修改 | 禁 add/remove/clear | [01 § 集合处理](references/01-coding-conventions.md) |
| foreach 中 remove/add | 禁止，用 Iterator | [01 § 集合处理](references/01-coding-conventions.md) |
| 集合初始化容量 | 指定初始大小（HashMap 默认 16） | [01 § 集合处理](references/01-coding-conventions.md) |
| 遍历 Map | entrySet 或 forEach | [01 § 集合处理](references/01-coding-conventions.md) |
| ConcurrentHashMap 存 null | 禁止（抛 NPE） | [01 § 集合处理](references/01-coding-conventions.md) |

### 7. 并发

| 场景 | 规约要点 | 参考文档 |
|------|----------|----------|
| 单例线程安全 | 必须保证 | [01 § 并发处理](references/01-coding-conventions.md) |
| 创建线程命名 | 指定有意义线程名 | [01 § 并发处理](references/01-coding-conventions.md) |
| 显式 new Thread | 禁止，必须用线程池 | [01 § 并发处理](references/01-coding-conventions.md) |
| 线程池创建方式 | 用 ThreadPoolExecutor，禁 Executors（OOM 风险） | [01 § 并发处理](references/01-coding-conventions.md) |
| SimpleDateFormat 线程安全 | 线程不安全，禁 static 或加锁；JDK8 用 DateTimeFormatter | [01 § 并发处理](references/01-coding-conventions.md) |
| ThreadLocal 回收 | 线程池场景必须 try-finally remove | [01 § 并发处理](references/01-coding-conventions.md) |
| 锁的性能 | 无锁优先；锁区块尽量小；对象锁优于类锁 | [01 § 并发处理](references/01-coding-conventions.md) |
| 多资源加锁顺序 | 必须一致，防死锁 | [01 § 并发处理](references/01-coding-conventions.md) |
| lock 与 try 块位置 | lock 在 try 之外 | [01 § 并发处理](references/01-coding-conventions.md) |
| tryLock 释放前 | 必须判断是否持锁 | [01 § 并发处理](references/01-coding-conventions.md) |
| 并发更新防丢失 | 加锁或乐观锁（version） | [01 § 并发处理](references/01-coding-conventions.md) |
| 资金敏感信息锁策略 | 悲观锁 | [01 § 并发处理](references/01-coding-conventions.md) |
| 多线程随机数 | 用 ThreadLocalRandom | [01 § 并发处理](references/01-coding-conventions.md) |
| 双重检查锁 | 目标属性须 volatile | [01 § 并发处理](references/01-coding-conventions.md) |

### 8. 控制语句

| 场景 | 规约要点 | 参考文档 |
|------|----------|----------|
| switch 缺 break/default | 必须终止或注释说明；必须含 default | [01 § 控制语句](references/01-coding-conventions.md) |
| switch 入参 String 为 null | 必须先判空 | [01 § 控制语句](references/01-coding-conventions.md) |
| if/else/for/while 大括号 | 必须用大括号 | [01 § 控制语句](references/01-coding-conventions.md) |
| 三目运算符 NPE | 注意自动拆箱 | [01 § 控制语句](references/01-coding-conventions.md) |
| 高并发等值判断退出 | 禁用等于，用区间判断 | [01 § 控制语句](references/01-coding-conventions.md) |
| if-else 层级 | 不超 3 层；用卫语句/策略/状态模式 | [01 § 控制语句](references/01-coding-conventions.md) |
| 批量接口入参保护 | 必须做 | [01 § 控制语句](references/01-coding-conventions.md) |
| 参数校验时机 | 低频/高开销/高可用/开放接口/敏感入口须校验 | [01 § 控制语句](references/01-coding-conventions.md) |

### 9. 注释

| 场景 | 规约要点 | 参考文档 |
|------|----------|----------|
| 类/属性/方法注释 | Javadoc `/** */`，禁 `//` | [01 § 注释规约](references/01-coding-conventions.md) |
| 抽象方法注释 | 必须说明做什么、实现要求 | [01 § 注释规约](references/01-coding-conventions.md) |
| 创建者与创建日期 | 所有类必须加 | [01 § 注释规约](references/01-coding-conventions.md) |
| 枚举字段注释 | 必须有 | [01 § 注释规约](references/01-coding-conventions.md) |
| TODO/FIXME | 注明标记人、时间、预计处理时间 | [01 § 注释规约](references/01-coding-conventions.md) |
| 注释掉代码 | 上方说明原因或直接删除 | [01 § 注释规约](references/01-coding-conventions.md) |

### 10. 前后端

| 场景 | 规约要点 | 参考文档 |
|------|----------|----------|
| API 协议/路径/方法 | 生产 HTTPS；路径名词复数小写下划线；禁后缀 | [01 § 前后端规约](references/01-coding-conventions.md) |
| 列表接口空返回 | 返回空数组[]/{}，禁 null | [01 § 前后端规约](references/01-coding-conventions.md) |
| 错误响应体 | 含 HTTP 状态码+errorCode+errorMessage+用户提示 | [01 § 前后端规约](references/01-coding-conventions.md) |
| JSON key 命名 | lowerCamelCase | [01 § 前后端规约](references/01-coding-conventions.md) |
| 超大整数返回前端 | 用 String，禁 Long（精度丢失） | [01 § 前后端规约](references/01-coding-conventions.md) |
| URL 参数长度 | 不超 2048 字节 | [01 § 前后端规约](references/01-coding-conventions.md) |
| 时间格式 | yyyy-MM-dd HH:mm:ss，GMT | [01 § 前后端规约](references/01-coding-conventions.md) |
| 翻页越界 | 前端<1 返首页；后端>总页数返末页 | [01 § 前后端规约](references/01-coding-conventions.md) |

### 11. 异常

| 场景 | 规约要点 | 参考文档 |
|------|----------|----------|
| 可预检查的 RuntimeException | 预检查规避，禁 catch（如 NPE） | [02 § 异常处理](references/02-exception-logging.md) |
| 异常做流程控制 | 禁止 | [02 § 异常处理](references/02-exception-logging.md) |
| 捕获后不处理 | 禁止抛弃，须处理或向上抛 | [02 § 异常处理](references/02-exception-logging.md) |
| 事务中 catch 后回滚 | 必须手动回滚 | [02 § 异常处理](references/02-exception-logging.md) |
| finally 关闭资源 | 必须；JDK7 用 try-with-resources | [02 § 异常处理](references/02-exception-logging.md) |
| finally 中 return | 禁止 | [02 § 异常处理](references/02-exception-logging.md) |
| RPC/二方包/动态类异常 | 用 Throwable 拦截（NoSuchMethodError） | [02 § 异常处理](references/02-exception-logging.md) |
| 防 NPE 场景 | 拆箱/DB结果/集合元素/远程调用/Session/级联调用 | [02 § 异常处理](references/02-exception-logging.md) |
| 自定义异常 | 有业务含义，禁直接抛 RuntimeException/Exception/Throwable | [02 § 异常处理](references/02-exception-logging.md) |
| 跨应用 RPC 返回 | 优先 Result+isSuccess() | [02 § 异常处理](references/02-exception-logging.md) |

### 12. 日志

| 场景 | 规约要点 | 参考文档 |
|------|----------|----------|
| 日志 API 选择 | 用 SLF4J 门面，禁直接用 Log4j/Logback | [02 § 日志规约](references/02-exception-logging.md) |
| 日志保存期限 | 至少 15 天；敏感操作相关不少于 6 个月 | [02 § 日志规约](references/02-exception-logging.md) |
| 字符串拼接 | 用占位符 `{}` | [02 § 日志规约](references/02-exception-logging.md) |
| trace/debug/info 输出前 | 必须日志级别开关判断 | [02 § 日志规约](references/02-exception-logging.md) |
| 重复打印 | additivity=false | [02 § 日志规约](references/02-exception-logging.md) |
| System.out/printStackTrace | 生产环境禁止 | [02 § 日志规约](references/02-exception-logging.md) |
| 异常日志内容 | 案发现场+堆栈信息 | [02 § 日志规约](references/02-exception-logging.md) |
| 日志输出对象 | 禁直接 JSON 工具转 String，用 toString | [02 § 日志规约](references/02-exception-logging.md) |
| 敏感信息日志 | 脱敏 | [02 § 日志规约](references/02-exception-logging.md) |

### 13. 错误码

| 场景 | 规约要点 | 参考文档 |
|------|----------|----------|
| 错误码格式 | 字符串 5 位 = 来源(A/B/C)+4位数字 | [02 § 错误码](references/02-exception-logging.md) |
| 全部正常 | 返回 00000 | [02 § 错误码](references/02-exception-logging.md) |
| 错误码是否含版本/等级 | 不体现 | [02 § 错误码](references/02-exception-logging.md) |
| 错误码直接给用户 | 禁止 | [02 § 错误码](references/02-exception-logging.md) |
| 第三方错误码转义 | C→B，带原错误码 | [02 § 错误码](references/02-exception-logging.md) |
| 错误码完整列表 | 175 条 | [08 § 错误码列表](references/08-appendix.md) |

### 14. 单元测试

| 场景 | 规约要点 | 参考文档 |
|------|----------|----------|
| 测试基本原则 | AIR（自动化/独立/可重复） | [03 单元测试](references/03-unit-testing.md) |
| 测试验证方式 | 用 assert，禁 System.out 人肉验证 | [03 单元测试](references/03-unit-testing.md) |
| 测试独立性 | 用例间禁互相调用/依赖顺序 | [03 单元测试](references/03-unit-testing.md) |
| 测试粒度 | 类级，一般方法级 | [03 单元测试](references/03-unit-testing.md) |
| 测试目录 | src/test/java | [03 单元测试](references/03-unit-testing.md) |
| 覆盖率目标 | 语句覆盖 70%；核心模块语句+分支 100% | [03 单元测试](references/03-unit-testing.md) |
| 测试用例设计 | BCDE（边界/正确/设计/错误） | [03 单元测试](references/03-unit-testing.md) |
| DB 相关测试 | 程序准备数据/自动回滚/前后缀标识 | [03 单元测试](references/03-unit-testing.md) |

### 15. 安全

| 场景 | 规约要点 | 参考文档 |
|------|----------|----------|
| 用户页面/功能权限 | 必须校验（防水平越权） | [04 安全规约](references/04-security.md) |
| 敏感数据展示 | 必须脱敏（手机 139****1219） | [04 安全规约](references/04-security.md) |
| SQL 参数 | 参数绑定，禁字符串拼接（防注入） | [04 安全规约](references/04-security.md) |
| 请求参数校验 | 必须有效性验证（防 OOM/慢查询/SSRF/注入） | [04 安全规约](references/04-security.md) |
| HTML 输出用户数据 | 必须过滤转义（防 XSS） | [04 安全规约](references/04-security.md) |
| 表单/AJAX 提交 | 必须 CSRF 校验 | [04 安全规约](references/04-security.md) |
| URL 外部重定向 | 必须白名单过滤 | [04 安全规约](references/04-security.md) |
| 短信/邮件/支付等平台资源 | 防重放（数量/频率/验证码） | [04 安全规约](references/04-security.md) |
| 文件上传 | 校验大小与类型 | [04 安全规约](references/04-security.md) |
| 配置文件密码 | 必须加密 | [04 安全规约](references/04-security.md) |

### 16. 建表

| 场景 | 规约要点 | 参考文档 |
|------|----------|----------|
| 是否字段命名 | is_xxx，unsigned tinyint | [05 § 建表规约](references/05-mysql-database.md) |
| 表名/字段名 | 小写或数字，禁大写、禁数字开头、禁两下划线间仅数字 | [05 § 建表规约](references/05-mysql-database.md) |
| 表名复数 | 禁止 | [05 § 建表规约](references/05-mysql-database.md) |
| 保留字 | 禁用（desc/range/match 等） | [05 § 建表规约](references/05-mysql-database.md) |
| 索引命名 | pk_/uk_/idx_ | [05 § 建表规约](references/05-mysql-database.md) |
| 小数类型 | decimal，禁 float/double | [05 § 建表规约](references/05-mysql-database.md) |
| varchar 长度 | 不超 5000，超则 text 独立表 | [05 § 建表规约](references/05-mysql-database.md) |
| 必备字段 | id/create_time/update_time | [05 § 建表规约](references/05-mysql-database.md) |
| 物理删除 | 禁止，用逻辑删除 | [05 § 建表规约](references/05-mysql-database.md) |
| 分库分表时机 | 单表超 500 万行或 2GB | [05 § 建表规约](references/05-mysql-database.md) |

### 17. 索引

| 场景 | 规约要点 | 参考文档 |
|------|----------|----------|
| 唯一业务字段 | 必须建唯一索引（含组合字段） | [05 § 索引规约](references/05-mysql-database.md) |
| join 表数量 | 不超 3 表 | [05 § 索引规约](references/05-mysql-database.md) |
| varchar 索引 | 必须指定索引长度 | [05 § 索引规约](references/05-mysql-database.md) |
| 左模糊/全模糊查询 | 禁止，走搜索引擎 | [05 § 索引规约](references/05-mysql-database.md) |
| order by 利用索引 | 排序字段放组合索引最后 | [05 § 索引规约](references/05-mysql-database.md) |
| 覆盖索引 | 利用避免回表 | [05 § 索引规约](references/05-mysql-database.md) |
| 组合索引字段顺序 | 区分度最高最左；等号条件列前置 | [05 § 索引规约](references/05-mysql-database.md) |

### 18. SQL 语句

| 场景 | 规约要点 | 参考文档 |
|------|----------|----------|
| 统计行数 | count(*)，禁 count(列名)/count(常量) | [05 § SQL 语句](references/05-mysql-database.md) |
| 判 NULL | ISNULL() | [05 § SQL 语句](references/05-mysql-database.md) |
| sum() 的 NPE | 用 IFNULL(SUM(col),0) | [05 § SQL 语句](references/05-mysql-database.md) |
| 分页 count 为 0 | 直接返回 | [05 § SQL 语句](references/05-mysql-database.md) |
| 外键与级联 | 禁止，应用层解决 | [05 § SQL 语句](references/05-mysql-database.md) |
| 存储过程 | 禁止 | [05 § SQL 语句](references/05-mysql-database.md) |
| 数据订正 | 先 select 确认再 update/delete | [05 § SQL 语句](references/05-mysql-database.md) |
| 多表列名 | 必须加表别名限定 | [05 § SQL 语句](references/05-mysql-database.md) |
| in 集合数量 | 控制 1000 以内 | [05 § SQL 语句](references/05-mysql-database.md) |

### 19. ORM 映射

| 场景 | 规约要点 | 参考文档 |
|------|----------|----------|
| 查询字段 | 禁 select *，明确写明字段 | [05 § ORM 映射](references/05-mysql-database.md) |
| resultMap | 必须定义，禁 resultClass；布尔 is_→xxx 映射 | [05 § ORM 映射](references/05-mysql-database.md) |
| 参数占位符 | #{}，禁 ${}（注入风险） | [05 § ORM 映射](references/05-mysql-database.md) |
| queryForList(start,size) | 不推荐（OOM 风险） | [05 § ORM 映射](references/05-mysql-database.md) |
| 结果集载体 | 禁直接用 HashMap/Hashtable 接收 | [05 § ORM 映射](references/05-mysql-database.md) |
| 更新记录 | 必须同时更新 update_time | [05 § ORM 映射](references/05-mysql-database.md) |
| 大而全更新接口 | 禁止，只更新改动字段 | [05 § ORM 映射](references/05-mysql-database.md) |

### 20. 工程分层

| 场景 | 规约要点 | 参考文档 |
|------|----------|----------|
| 分层结构 | 开放API/终端显示/Web/Service/Manager/DAO | [06 § 应用分层](references/06-engineering-structure.md) |
| 分层异常处理 | DAO 不打日志；Service 记盘；Web 不上抛跳错误页；开放接口返错误码 | [06 § 应用分层](references/06-engineering-structure.md) |
| 领域模型 | DO/DTO/BO/Query/VO 各层职责 | [06 § 应用分层](references/06-engineering-structure.md) |
| 查询参数封装 | 超 2 参数用 Query，禁 Map | [06 § 应用分层](references/06-engineering-structure.md) |

### 21. 二方库依赖

| 场景 | 规约要点 | 参考文档 |
|------|----------|----------|
| GAV 命名 | GroupId 最多 4 级；ArtifactId 产品线-模块名 | [06 § 二方库依赖](references/06-engineering-structure.md) |
| 版本号 | 主.次.修订；起始 1.0.0 | [06 § 二方库依赖](references/06-engineering-structure.md) |
| 线上依赖 SNAPSHOT | 禁止 | [06 § 二方库依赖](references/06-engineering-structure.md) |
| 同 GAV 不同 Version | 禁止 | [06 § 二方库依赖](references/06-engineering-structure.md) |
| 统一版本变量 | 依赖群定义统一版本变量 | [06 § 二方库依赖](references/06-engineering-structure.md) |
| pom 依赖管理 | 依赖放 dependencies，版本仲裁放 dependencyManagement | [06 § 二方库依赖](references/06-engineering-structure.md) |
| 接口返回值用枚举 | 禁止 | [06 § 二方库依赖](references/06-engineering-structure.md) |

### 22. 服务器

| 场景 | 规约要点 | 参考文档 |
|------|----------|----------|
| 远程调用超时 | 必须设置 | [06 § 服务器](references/06-engineering-structure.md) |
| 高并发 time_wait | 调小 tcp_fin_timeout | [06 § 服务器](references/06-engineering-structure.md) |
| 文件句柄数 | 调大 fd | [06 § 服务器](references/06-engineering-structure.md) |
| OOM dump | -XX:+HeapDumpOnOutOfMemoryError | [06 § 服务器](references/06-engineering-structure.md) |
| Xms/Xmx | 生产环境设为相同 | [06 § 服务器](references/06-engineering-structure.md) |

### 23. 系统设计

| 场景 | 规约要点 | 参考文档 |
|------|----------|----------|
| 存储方案/数据结构设计 | 评审通过并沉淀文档 | [07 设计规约](references/07-design-conventions.md) |
| 用例图选用 | User>1 类且 UseCase>5 | [07 设计规约](references/07-design-conventions.md) |
| 状态图选用 | 业务对象状态>3 | [07 设计规约](references/07-design-conventions.md) |
| 时序图选用 | 调用链涉及对象>3 | [07 设计规约](references/07-design-conventions.md) |
| 类图选用 | 模型类>5 且依赖复杂 | [07 设计规约](references/07-design-conventions.md) |
| 活动图选用 | >2 对象协作且流程复杂 | [07 设计规约](references/07-design-conventions.md) |
| 弱依赖识别 | 必须设计降级/应急预案 | [07 设计规约](references/07-design-conventions.md) |
| 设计原则 | 单一职责/聚合优于继承/依赖倒置/开闭/DRY | [07 设计规约](references/07-design-conventions.md) |
| 敏捷开发误区 | ≠讲故事+编码+发布 | [07 设计规约](references/07-design-conventions.md) |
| 无障碍设计 | tab 聚焦/验证码多方式/自定义控件交互 | [07 设计规约](references/07-design-conventions.md) |

---

## 反模式红线（出现即停）

| 反模式 | 违反规约 | 参考 |
|--------|----------|------|
| 变量名拼音英文混用/中文 | 命名 | [01 § 命名风格](references/01-coding-conventions.md) |
| 代码出现魔法值 | 常量 | [01 § 常量定义](references/01-coding-conventions.md) |
| 用 Tab 缩进 / 单行超 120 | 格式 | [01 § 代码格式](references/01-coding-conventions.md) |
| `param.equals("test")` | OOP | [01 § OOP 规约](references/01-coding-conventions.md) |
| Integer 用 == 比较 | OOP | [01 § OOP 规约](references/01-coding-conventions.md) |
| `new BigDecimal(0.1)` | OOP | [01 § OOP 规约](references/01-coding-conventions.md) |
| POJO 布尔加 is 前缀 | OOP | [01 § OOP 规约](references/01-coding-conventions.md) |
| `new Date().getTime()` | 日期 | [01 § 日期时间](references/01-coding-conventions.md) |
| foreach 里 remove/add | 集合 | [01 § 集合处理](references/01-coding-conventions.md) |
| `Executors.newXxx` 建线程池 | 并发 | [01 § 并发处理](references/01-coding-conventions.md) |
| SimpleDateFormat 定义为 static 不加锁 | 并发 | [01 § 并发处理](references/01-coding-conventions.md) |
| finally 里 return | 异常 | [02 § 异常处理](references/02-exception-logging.md) |
| catch NPE 而非预检查 | 异常 | [02 § 异常处理](references/02-exception-logging.md) |
| 直接用 Log4j API | 日志 | [02 § 日志规约](references/02-exception-logging.md) |
| 生产环境 System.out/printStackTrace | 日志 | [02 § 日志规约](references/02-exception-logging.md) |
| SQL 字符串拼接参数 | 安全 | [04 安全规约](references/04-security.md) |
| select * 查询 | ORM | [05 § ORM 映射](references/05-mysql-database.md) |
| 用 ${} 传参 | ORM | [05 § ORM 映射](references/05-mysql-database.md) |
| 物理删除 | 建表 | [05 § 建表规约](references/05-mysql-database.md) |
| 用外键/级联/存储过程 | SQL | [05 § SQL 语句](references/05-mysql-database.md) |
| 线上依赖 SNAPSHOT | 依赖 | [06 § 二方库依赖](references/06-engineering-structure.md) |

---

## 参考文档索引

详细规约正文（含说明、正例、反例、完整条目）存放于 `references/` 目录：

| 文件 | 内容 | 子章节 |
|------|------|--------|
| [01-coding-conventions.md](references/01-coding-conventions.md) | 一、编程规约 | 命名风格/常量定义/代码格式/OOP 规约/日期时间/集合处理/并发处理/控制语句/注释规约/前后端规约/其他 |
| [02-exception-logging.md](references/02-exception-logging.md) | 二、异常日志 | 错误码/异常处理/日志规约 |
| [03-unit-testing.md](references/03-unit-testing.md) | 三、单元测试 | AIR/BCDE/覆盖率/数据准备 |
| [04-security.md](references/04-security.md) | 四、安全规约 | 权限/脱敏/注入/XSS/CSRF/上传/加密 |
| [05-mysql-database.md](references/05-mysql-database.md) | 五、MySQL 数据库 | 建表规约/索引规约/SQL 语句/ORM 映射 |
| [06-engineering-structure.md](references/06-engineering-structure.md) | 六、工程结构 | 应用分层/二方库依赖/服务器 |
| [07-design-conventions.md](references/07-design-conventions.md) | 七、设计规约 | 存储评审/各类图选型/设计原则 |
| [08-appendix.md](references/08-appendix.md) | 附录 | 前言/版本历史/专有名词解释/错误码列表(175条) |

---

**来源**：阿里巴巴集团技术团队 · 全球 Java 社区开发者  
**版本**：1.7.1 黄山版（2022.02.03）  
**愿景**：码出高效，码出质量
