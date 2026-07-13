---
name: update-knowledge
description: 知识库更新标准流程 - 新增或修改 specs/architecture/patterns/decisions/lessons 文档
---

# 知识库更新标准流程

## 触发条件

当需要把新知识沉淀到知识库时触发：
- 发现新的编码规范、约束 → `specs/`
- 设计新模块或架构调整 → `architecture/`
- 沉淀出可复用模式、代码模板 → `patterns/`
- 做了重要技术决策 → `decisions/`
- 复盘总结出经验教训 → `lessons/`

手动触发：`/update-knowledge 新增查询模式最佳实践`

---

## 更新流程（按顺序执行）

### 阶段 1：判定知识类型（3分钟）

按内容性质选择目标目录：

| 内容 | 目录 | 文件命名 |
|-----|------|---------|
| 编码规范、命名规则、约束 | `specs/` | `kebab-英文.md` |
| 模块关系、技术栈、架构图 | `architecture/` | `kebab-英文.md` |
| 常用模式、代码模板 | `patterns/` | `kebab-英文.md` |
| 技术决策（ADR） | `decisions/` | `NNN-决策标题.md` |
| 经验教训、复盘 | `lessons/` | `YYYY-MM-DD-关键词.md` |

**检查清单**：
```
□ 已确定目标目录
□ 已确认是否已有同类文档（避免重复）
```

先 Grep / Glob 同目录，命中则走「修改」流程，未命中走「新增」流程。

---

### 阶段 2：新增文档（8分钟）

**frontmatter 规范**：
```markdown
---
title: 文档标题
date: YYYY-MM-DD
tags: [分类1, 分类2]
---
```

**正文结构**参考各目录 README 的指引，最小集：
- 背景与目标
- 主体内容（规范条文 / 架构图 / 模式代码 / 决策上下文 / 教训）
- 适用范围与例外
- 相关链接（wiki-link）

**写入路径**：`knowledge-base/{目录}/{文件名}.md`

---

### 阶段 3：修改文档（5分钟）

**Read** 现有文档 → **Edit** 追加或修订内容：
- 新增条文追加到对应章节末尾，不破坏原有编号
- 修订条文保留原文并标注变更日期，或直接替换并在文末「变更记录」留痕
- 不删除已有内容除非明确作废

---

### 阶段 4：更新索引（3分钟）

**Edit** 该目录的 `README.md`，在文档列表中追加：
```
- [文档标题](文件名.md) — 一句话说明
```

保持分类分组，不破坏既有排序。

---

### 阶段 5：交叉引用（2分钟）

- 在新文档末尾用 wiki-link 关联相关文档（`[[../patterns/xxx]]`、`[[../specs/xxx]]`）
- 在被引用的旧文档里反向追加「相关：[[新文档]]」（仅当强相关时）
- 关联 Memory：`[[red-lines]]`、`[[logical-deletion]]` 等（按实际相关度）

确保 wiki-link 指向真实存在的文件。

---

## 关键约束

- ❌ 不在 `troubleshooting/` 写规范类文档（问题记录用 `/record-issue`）
- ❌ 不创建模板已覆盖的重复内容
- ❌ 不修改 `template.md` 模板文件
- ✅ 文档单一职责，避免一个大文件塞多种内容
- ✅ 命名 kebab 化、可检索（含关键词）

---

## 相关链接

- 索引：`knowledge-base/README.md`
- 配套 Skill：`/record-issue`（问题沉淀）、`/lookup-knowledge`（查找）
- Memory：`red-lines`、`logical-deletion`、`layer-standards`、`testing-requirements`、`database-audit-fields`

---

**Skill 版本**：v1.0
**更新日期**：2026-07-04
