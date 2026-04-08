# Skills 仓库结构最佳实践

## 📁 推荐的目录结构

### 方案一：扁平结构（推荐）✅

适合 skill 数量较少（<10个）的情况，结构清晰，易于管理。

```
skills/                          # 仓库根目录
│
├── README.md                    # 仓库总览
│
├── alibaba-java-manual/         # Skill 1
│   ├── SKILL.md                 # Skill 定义文件（必需）
│   ├── README.md                # Skill 说明文档
│   ├── MANUAL.md                # 详细手册（可选）
│   └── assets/                  # 资源文件（可选）
│       └── images/
│
├── parallel-development/        # Skill 2
│   ├── SKILL.md
│   ├── README.md
│   ├── GUIDE.md
│   ├── TEMPLATE.md
│   └── parallel-dev.bat
│
├── another-skill/              # Skill 3
│   ├── SKILL.md
│   └── README.md
│
└── .github/                    # GitHub 配置（可选）
    └── workflows/
        └── test-skills.yml
```

**优点**：
- ✅ 结构简单清晰
- ✅ 安装命令简单：`npx skills add user/repo@skill-name`
- ✅ 易于查找和维护
- ✅ 符合 skills CLI 的默认预期

---

### 方案二：分类结构

适合 skill 数量较多（>10个）或有明显分类的情况。

```
skills/                          # 仓库根目录
│
├── README.md                    # 仓库总览
│
├── coding-standards/            # 分类：编码规范
│   ├── alibaba-java-manual/
│   │   └── SKILL.md
│   ├── spring-boot-guide/
│   │   └── SKILL.md
│   └── README.md               # 分类说明
│
├── development/                 # 分类：开发工具
│   ├── parallel-development/
│   │   └── SKILL.md
│   ├── code-generator/
│   │   └── SKILL.md
│   └── README.md
│
├── database/                    # 分类：数据库
│   ├── mysql-best-practices/
│   │   └── SKILL.md
│   └── README.md
│
└── testing/                     # 分类：测试
    ├── test-case-template/
    │   └── SKILL.md
    └── README.md
```

**优点**：
- ✅ 易于分类管理
- ✅ 结构化组织
- ✅ 便于扩展

**安装方式**：
```bash
npx skills add user/repo@alibaba-java-manual
# 或指定分类路径
npx skills add user/repo@coding-standards/alibaba-java-manual
```

---

### 方案三：多仓库结构

适合每个 skill 都比较复杂、独立维护的情况。

```
# 仓库 1: alibaba-java-manual
https://github.com/user/alibaba-java-manual
├── SKILL.md
├── README.md
└── MANUAL.md

# 仓库 2: parallel-development
https://github.com/user/parallel-development
├── SKILL.md
├── GUIDE.md
└── parallel-dev.bat

# 索引仓库: skills-index
https://github.com/user/skills-index
├── README.md
└── index.json              # Skills 索引
```

**优点**：
- ✅ 每个 skill 独立维护
- ✅ 版本控制独立
- ✅ 权限管理灵活

**缺点**：
- ❌ 管理多个仓库
- ❌ 安装时需要记住多个仓库名

---

## 🎯 推荐方案

根据你的情况，我推荐 **方案一：扁平结构**

### 完整示例

```
jerry-20160416/skills/          # 你的 GitHub 仓库
│
├── README.md                   # 仓库主 README
│   ├── Skills 列表
│   ├── 安装说明
│   └── 贡献指南
│
├── alibaba-java-manual/        # Skill 1
│   ├── SKILL.md               # ✅ 必需
│   ├── README.md              # 推荐添加
│   ├── MANUAL.md              # 详细内容
│   └── examples/              # 示例（可选）
│
├── parallel-development/       # Skill 2
│   ├── SKILL.md               # ✅ 必需
│   ├── README.md
│   ├── GUIDE.md
│   ├── TEMPLATE.md
│   └── parallel-dev.bat
│
├── mysql-design-guide/        # Skill 3（未来添加）
│   ├── SKILL.md
│   └── README.md
│
└── .gitignore                 # Git 忽略文件
```

---

## 📋 必需文件

每个 skill 目录下必须包含：

| 文件 | 必需性 | 说明 |
|------|--------|------|
| `SKILL.md` | ✅ 必需 | Skill 定义文件，包含 YAML 前置数据 |
| `README.md` | ⭐ 推荐 | Skill 使用说明 |
| 其他文件 | 📝 可选 | 手册、模板、脚本等 |

---

## 🔧 SKILL.md 标准格式

```yaml
---
name: skill-name
description: "Skill 描述"
version: 1.0.0
author: Your Name
tags: [tag1, tag2, tag3]
---

# Skill 标题

## 何时激活
[触发条件说明]

## 功能说明
[详细说明]

## 使用方法
[使用示例]
```

---

## 📝 README.md 模板

### 仓库主 README

```markdown
# Agent Skills Collection

这个仓库包含多个实用的 Agent Skills。

## 📦 Skills 列表

| Skill | 描述 | 安装命令 |
|-------|------|---------|
| [alibaba-java-manual](./alibaba-java-manual) | 阿里巴巴Java开发规范 | `npx skills add jerry-20160416/skills@alibaba-java-manual` |
| [parallel-development](./parallel-development) | 并行开发流程 | `npx skills add jerry-20160416/skills@parallel-development` |

## 🚀 快速开始

\`\`\`bash
# 安装 skill
npx skills add jerry-20160416/skills@<skill-name>

# 查看已安装的 skills
npx skills list
\`\`\`

## 📖 如何贡献

欢迎贡献新的 Skill！

1. Fork 本仓库
2. 创建新的 skill 目录
3. 添加 `SKILL.md` 和 `README.md`
4. 提交 Pull Request

## 📄 License

MIT
```

### Skill README

```markdown
# Skill 名称

> 简短描述

## 📖 简介

[详细说明]

## 🚀 安装

\`\`\`bash
npx skills add jerry-20160416/skills@skill-name
\`\`\`

## 💡 使用方法

[使用示例]

## 📂 文件说明

- `SKILL.md` - Skill 定义
- `README.md` - 本文件
- `MANUAL.md` - 详细手册

## 📝 版本历史

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0.0 | YYYY-MM-DD | 初始版本 |
```

---

## 🚀 安装命令对应关系

### 扁平结构

```bash
# 安装 skill
npx skills add jerry-20160416/skills@alibaba-java-manual
npx skills add jerry-20160416/skills@parallel-development

# 安装所有 skills
npx skills add jerry-20160416/skills
```

### 分类结构

```bash
# 安装 skill
npx skills add jerry-20160416/skills@alibaba-java-manual
npx skills add jerry-20160416/skills@coding-standards/alibaba-java-manual

# 安装某个分类下的所有 skills
npx skills add jerry-20160416/skills@coding-standards
```

---

## 🎨 最佳实践

### 1. 命名规范

```
✅ 推荐：
- alibaba-java-manual     # 清晰、描述性强
- parallel-development    # 连字符分隔
- mysql-best-practices

❌ 避免：
- skill1                  # 太通用
- AlibabaJavaManual       # 大驼峰（不利于命令行）
- parallel_dev           # 下划线（不统一）
```

### 2. 目录深度

```
✅ 推荐（扁平）：
skills/
└── alibaba-java-manual/
    └── SKILL.md

❌ 避免（过深）：
skills/
└── java/
    └── alibaba/
        └── manual/
            └── SKILL.md
```

### 3. 文件组织

```
✅ 推荐：
skill-name/
├── SKILL.md              # 必需
├── README.md             # 推荐添加
├── GUIDE.md              # 如果内容很多
├── assets/               # 资源文件单独目录
│   ├── images/
│   └── templates/
└── examples/             # 示例代码

❌ 避免：
skill-name/
├── SKILL.md
├── 1.md                  # 文件名不清晰
├── 2.md
├── image1.png           # 根目录文件混乱
├── image2.png
└── temp.txt
```

---

## 📊 规模建议

| Skills 数量 | 推荐方案 | 说明 |
|------------|---------|------|
| 1-5 个 | 扁平结构 | 简单直接 |
| 6-15 个 | 扁平结构 | 可考虑分类 README |
| 16+ 个 | 分类结构 | 按领域分类组织 |
| 大型独立 skill | 多仓库 | 每个 skill 独立仓库 |

---

## 🔄 迁移建议

如果你现在有不规范的结构，可以按以下步骤迁移：

### 步骤 1：整理现有 skills

```bash
# 当前结构
skills/
└── skills/
    └── alibaba-java-manual/
        └── SKILL.md

# 调整为
skills/
├── alibaba-java-manual/
│   └── SKILL.md
└── parallel-development/
    └── SKILL.md
```

### 步骤 2：更新 README

确保 README.md 中的链接和安装命令正确。

### 步骤 3：测试安装

```bash
# 测试每个 skill 是否可以正常安装
npx skills add jerry-20160416/skills@alibaba-java-manual -l
npx skills add jerry-20160416/skills@parallel-development -l
```

---

## 📌 你的仓库建议

根据当前情况，建议调整为：

```
jerry-20160416/skills/
│
├── README.md                        # 仓库主 README
│
├── alibaba-java-manual/             # Skill 1
│   ├── SKILL.md
│   ├── README.md
│   └── MANUAL.md
│
├── parallel-development/            # Skill 2
│   ├── SKILL.md
│   ├── README.md
│   ├── GUIDE.md
│   ├── TEMPLATE.md
│   └── parallel-dev.bat
│
└── .gitignore                       # Git 忽略配置
```

---

**总结**：使用扁平结构，每个 skill 一个目录，确保结构清晰、易于安装和维护！
