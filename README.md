# Agent Skills Collection

这是一个 Agent Skills 仓库，包含各种实用的技能包，用于扩展 AI Agent 的能力。

## 📦 Skills 列表

| Skill | 描述 | 安装命令 |
|-------|------|---------|
| [alibaba-java-manual](./alibaba-java-manual) | 阿里巴巴Java开发手册（黄山版）- 编程规约、异常日志、单元测试、安全规约、MySQL数据库、工程结构、设计规约 | `npx skills add jerry-20160416/skills@alibaba-java-manual` |
| [parallel-development](./parallel-development) | 并行开发流程 - 同时启动多个agent处理需求文档，生成设计文档、代码实现和测试用例 | `npx skills add jerry-20160416/skills@parallel-development` |

## 🚀 快速开始

### 安装 Skill

```bash
# 安装单个 skill
npx skills add jerry-20160416/skills@<skill-name>

# 查看可用 skills
npx skills add jerry-20160416/skills -l

# 查看已安装的 skills
npx skills list

# 全局安装
npx skills add jerry-20160416/skills@<skill-name> -g
```

### 使用 Skill

安装后，Agent 会自动加载相关 Skill，你可以直接询问问题：

**alibaba-java-manual**:
```
"Java 类名应该怎么命名？"
"MySQL 建表有哪些规范？"
"如何正确处理异常？"
```

**parallel-development**:
```
"我有一份需求文档在 ./requirements/订单系统.md，
请启动并行开发流程，生成设计文档、代码和测试用例"
```

## 📁 仓库结构

```
jerry-20160416/skills/
│
├── README.md                        # 本文件
├── STRUCTURE_GUIDE.md              # 结构最佳实践指南
├── .gitignore                      # Git 忽略配置
│
├── alibaba-java-manual/            # Skill 1
│   ├── SKILL.md                    # Skill 定义文件
│   ├── README.md                   # 详细说明
│   └── MANUAL.md                   # 完整手册内容
│
└── parallel-development/           # Skill 2
    ├── SKILL.md                    # Skill 定义文件
    ├── README.md                   # 详细说明
    ├── GUIDE.md                    # 实施指南
    ├── TEMPLATE.md                 # 需求文档模板
    └── parallel-dev.bat            # 启动脚本
```

## 🎯 Skill 详细说明

### alibaba-java-manual

**阿里巴巴 Java 开发手册（黄山版 1.7.1）**

> 🏆 Java 社区集体智慧结晶，经历多次大规模一线实战检验

**包含七大维度**：
- 📝 编程规约 - 命名风格、代码格式、OOP规约、并发处理等
- ⚠️ 异常日志 - 错误码、异常处理、日志规约
- ✅ 单元测试 - 测试编写规范
- 🔒 安全规约 - 权限控制、SQL注入防护
- 🗄️ MySQL 数据库 - 建表规约、索引设计、SQL语句
- 🏗️ 工程结构 - 应用分层、依赖管理
- 🎨 设计规约 - 系统设计原则

**安装**：
```bash
npx skills add jerry-20160416/skills@alibaba-java-manual
```

**在线浏览**：https://github.com/jerry-20160416/skills/tree/master/alibaba-java-manual

---

### parallel-development

**并行开发流程 - 同时启动多个 Agent 处理需求**

> 🚀 大幅缩短从需求到交付的周期

**核心功能**：
- 📄 **设计 Agent** - 自动编写系统设计文档
- 💻 **代码 Agent** - 自动实现业务代码
- ✅ **测试 Agent** - 自动生成测试用例

**使用场景**：
- 快速迭代开发
- 需求明确的 CRUD 功能
- 需要完整交付物的项目

**安装**：
```bash
npx skills add jerry-20160416/skills@parallel-development
```

**在线浏览**：https://github.com/jerry-20160416/skills/tree/master/parallel-development

---

## 📖 如何贡献

欢迎贡献新的 Skill！

### 添加新 Skill

1. **Fork 本仓库**

2. **创建新的 skill 目录**
   ```bash
   mkdir my-new-skill
   ```

3. **创建必需文件**
   ```bash
   # SKILL.md (必需)
   ---
   name: my-new-skill
   description: "Skill 描述"
   ---

   # Skill 内容...

   # README.md (推荐)
   # Skill 使用说明
   ```

4. **更新主 README.md**
   - 在 Skills 列表中添加新 skill
   - 更新安装命令

5. **提交 Pull Request**

### Skill 开发指南

参考 [STRUCTURE_GUIDE.md](./STRUCTURE_GUIDE.md) 了解：
- 目录结构最佳实践
- 文件组织规范
- 命名约定

## 🔗 相关资源

- **Skills 官网**：https://skills.sh/
- **Skills CLI 文档**：https://skills.sh/docs
- **阿里巴巴 Java 开发手册**：https://github.com/alibaba/p3c

## 📝 更新日志

### 2026-04-08
- ✅ 添加 `alibaba-java-manual` skill
- ✅ 添加 `parallel-development` skill
- ✅ 优化仓库结构
- ✅ 添加 `.gitignore`
- ✅ 完善文档

## 📄 License

MIT License

---

**💡 提示**：使用 `npx skills add jerry-20160416/skills@<skill-name>` 安装你需要的 skill！
