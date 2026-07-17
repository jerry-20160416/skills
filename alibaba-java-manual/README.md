# 阿里巴巴 Java 开发手册 Skill

> 版本：1.7.1（黄山版）
> 来源：阿里巴巴集团技术团队 · 全球 Java 社区开发者
> 更新日期：2022.02.03

## 简介

本 Skill 基于阿里巴巴 Java 开发手册（黄山版 1.7.1）创建。手册以 Java 开发者为中心视角，划分为**编程规约、异常日志、单元测试、安全规约、MySQL 数据库、工程结构、设计规约**七大维度，依据约束力强弱分为【强制】【推荐】【参考】三类。

## 目录结构

```
alibaba-java-manual/
├── SKILL.md                      # 场景速查：什么情况需要什么规范（精简，先加载）
├── README.md                     # 本文件
└── references/                   # 规约正文（含说明/正例/反例，按需加载）
    ├── 01-coding-conventions.md   # 一、编程规约（命名/常量/格式/OOP/日期/集合/并发/控制/注释/前后端/其他）
    ├── 02-exception-logging.md    # 二、异常日志（错误码/异常处理/日志规约）
    ├── 03-unit-testing.md         # 三、单元测试
    ├── 04-security.md             # 四、安全规约
    ├── 05-mysql-database.md       # 五、MySQL 数据库（建表/索引/SQL/ORM）
    ├── 06-engineering-structure.md# 六、工程结构（应用分层/二方库依赖/服务器）
    ├── 07-design-conventions.md    # 七、设计规约
    └── 08-appendix.md             # 附录（前言/版本历史/专有名词/错误码列表 175 条）
```

## 设计说明

- **SKILL.md** 只描述「**什么情况下需要什么规范**」——以场景速查表将开发/审查情境映射到对应规约要点与参考文档，并附反模式红线。保持精简，适合 Agent 优先加载。
- **references/** 存放规约正文详细内容（完整条目、说明、正例、反例），按七大维度拆分为独立文件，命中场景后按需查阅，避免一次性加载全部内容。

## 参考文档索引

| 文件 | 内容 | 子章节 |
|------|------|--------|
| [01-coding-conventions.md](references/01-coding-conventions.md) | 编程规约 | 命名风格/常量定义/代码格式/OOP 规约/日期时间/集合处理/并发处理/控制语句/注释规约/前后端规约/其他 |
| [02-exception-logging.md](references/02-exception-logging.md) | 异常日志 | 错误码/异常处理/日志规约 |
| [03-unit-testing.md](references/03-unit-testing.md) | 单元测试 | AIR/BCDE/覆盖率/数据准备 |
| [04-security.md](references/04-security.md) | 安全规约 | 权限/脱敏/注入/XSS/CSRF/上传/加密 |
| [05-mysql-database.md](references/05-mysql-database.md) | MySQL 数据库 | 建表规约/索引规约/SQL 语句/ORM 映射 |
| [06-engineering-structure.md](references/06-engineering-structure.md) | 工程结构 | 应用分层/二方库依赖/服务器 |
| [07-design-conventions.md](references/07-design-conventions.md) | 设计规约 | 存储评审/各类图选型/设计原则 |
| [08-appendix.md](references/08-appendix.md) | 附录 | 前言/版本历史/专有名词解释/错误码列表 |

## 使用方式

安装后，Agent 会在相关场景自动加载此 Skill。可直接询问具体规范问题，Agent 会按场景速查表定位并按需读取 `references/` 正文：

**命名相关：**
```
"类名应该怎么命名？"
"常量的命名规范是什么？"
"布尔变量能不能加 is 前缀？"
```

**代码格式：**
```
"代码缩进用几个空格？"
"单行代码长度限制是多少？"
```

**异常处理 / 日志：**
```
"如何正确捕获和处理异常？"
"错误码应该如何定义？"
"日志该用哪个框架？"
```

**数据库：**
```
"MySQL 建表有哪些规范？"
"索引设计有哪些原则？"
"能不能用 select *？"
```

**并发编程：**
```
"线程池如何正确使用？"
"SimpleDateFormat 线程安全吗？"
```

## 规约等级

| 等级 | 标识 | 说明 |
|------|------|------|
| 强制 | 【强制】 | 必须遵守，违反将导致严重问题或故障 |
| 推荐 | 【推荐】 | 建议遵守，提升代码质量与可维护性 |
| 参考 | 【参考】 | 可选遵守，按实际情况灵活处理 |

## 版本历史

| 版本 | 版本名 | 发布日期 | 说明 |
|------|--------|----------|------|
| 1.7.1 | 黄山版 | 2022.02.03 | 新增 11 条新规约（浮点数后缀大写、枚举属性私有不可变、配置文件密码加密等） |
| 1.7.0 | 嵩山版 | 2020.08.03 | 新增前后端规约 14 条、禁止歧视性用语等 |
| 1.6.0 | 泰山版 | 2020.04.22 | 发布错误码统一解决方案，新增 34 条规约 |
| 1.5.0 | 华山版 | 2019.06.19 | 移除"阿里巴巴"限定词，新增 21 条规约 |

完整版本历史见 [references/08-appendix.md](references/08-appendix.md#附1版本历史)。

## 相关资源

- [阿里巴巴 Java 开发手册 P3C](https://github.com/alibaba/p3c)
- [IDE 插件 - Alibaba Java Coding Guidelines](https://plugins.jetbrains.com/plugin/10046-alibaba-java-coding-guidelines)

## License

本手册内容由阿里巴巴集团发布，遵循 Apache License 2.0。

---

**愿景**：码出高效，码出质量。  
**理念**：无规矩不成方圆，无规范难以协同——限制过度个性化，以普遍认可的统一方式做事，提升协作效率，降低沟通成本。
