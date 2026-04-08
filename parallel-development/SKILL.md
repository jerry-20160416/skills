---
name: parallel-development
description: "并行开发流程 - 同时启动多个agent处理需求文档，分别生成设计文档、代码实现和测试用例。适用于快速开发场景。"
version: 1.0.0
---

# 并行开发流程 Skill

## 🎯 功能说明

当拿到需求文档后，**同时启动多个 agent 并行工作**，大幅缩短开发周期：

- 📄 **设计文档 Agent** - 编写详细设计文档
- 💻 **代码开发 Agent** - 实现代码逻辑
- ✅ **测试用例 Agent** - 编写测试用例

## 📋 使用场景

- 快速迭代开发
- 需求明确，可以并行处理的场景
- 希望缩短开发周期的项目
- 需要同时输出设计、代码、测试的完整交付物

## 🚀 工作流程

### 第一步：准备需求文档

确保需求文档路径清晰，内容完整。支持格式：
- Markdown (.md)
- Word (.docx)
- PDF (.pdf)
- 纯文本 (.txt)

### 第二步：启动并行开发

提供需求文档路径，系统将自动：
1. 解析需求文档内容
2. 同时启动三个后台任务
3. 分配给不同的专业 agent
4. 并行处理，互不阻塞

### 第三步：等待完成

系统会在后台并行执行，完成后输出：
- 设计文档路径
- 代码文件路径
- 测试用例路径

## 💡 核心命令

### 启动并行开发

```bash
# 基本用法
parallel-dev <需求文档路径>

# 指定输出目录
parallel-dev <需求文档路径> --output <输出目录>

# 指定项目名称
parallel-dev <需求文档路径> --project <项目名称>
```

### 示例

```bash
# 从需求文档启动并行开发
parallel-dev ./docs/需求文档.md

# 指定输出到项目目录
parallel-dev ./需求/用户管理模块.docx --output ./project/user-management

# 完整参数
parallel-dev ./需求/订单系统.md --project order-system --output ./deliverables
```

## 🔄 执行流程

```
需求文档
    ↓
┌───────────────────────────────────────┐
│         并行启动 3 个 Agent           │
├───────────────────────────────────────┤
│                                        │
│  📄 设计Agent    💻 代码Agent    ✅ 测试Agent  │
│      ↓              ↓              ↓        │
│  设计文档       代码实现      测试用例     │
│                                        │
└───────────────────────────────────────┘
    ↓
输出完整交付物
```

## 📂 输出结构

```
<输出目录>/
├── design/
│   └── <项目名称>_设计文档_v1.0.0.md
├── code/
│   ├── src/
│   │   ├── controller/
│   │   ├── service/
│   │   ├── repository/
│   │   └── entity/
│   └── test/
│       └── unit/
└── testcases/
    ├── 功能测试用例.md
    └── 接口测试用例.md
```

## 🎨 Agent 分工说明

### 📄 设计文档 Agent

**职责**：
- 分析需求，提取功能点
- 设计系统架构
- 设计数据库表结构
- 设计接口规范
- 编写详细设计文档

**输出**：
- 设计文档（包含架构图、ER图、接口定义）
- 数据库DDL脚本
- 接口文档

### 💻 代码开发 Agent

**职责**：
- 根据设计文档实现代码
- 遵循编码规范
- 实现业务逻辑
- 编写注释

**输出**：
- 完整的源代码
- 配置文件
- 部署脚本

### ✅ 测试用例 Agent

**职责**：
- 分析功能点
- 设计测试场景
- 编写测试用例
- 覆盖正常流程和异常流程

**输出**：
- 功能测试用例
- 接口测试用例
- 边界值测试用例

## ⚙️ 配置选项

### 在 SKILL_CONFIG.md 中配置

```yaml
# 默认输出目录
output_dir: ./deliverables

# Agent 配置
agents:
  design:
    timeout: 300  # 设计文档超时时间（秒）
  code:
    timeout: 600  # 代码开发超时时间（秒）
  test:
    timeout: 300  # 测试用例超时时间（秒）

# 模板配置
templates:
  design: ./templates/design_template.md
  code: ./templates/code_template/
  test: ./templates/test_template.md
```

## 🔧 高级用法

### 仅启动单个任务

```bash
# 仅生成设计文档
parallel-dev <需求文档> --task design

# 仅生成代码
parallel-dev <需求文档> --task code

# 仅生成测试用例
parallel-dev <需求文档> --task test
```

### 指定编码规范

```bash
# 使用阿里巴巴Java开发规范
parallel-dev <需求文档> --standard alibaba-java-manual

# 使用自定义规范
parallel-dev <需求文档> --standard ./coding-standards.md
```

### 指定技术栈

```bash
# Spring Boot 项目
parallel-dev <需求文档> --tech-stack spring-boot

# 微服务项目
parallel-dev <需求文档> --tech-stack spring-cloud

# 自定义技术栈
parallel-dev <需求文档> --tech-stack ./tech-stack-config.yaml
```

## 📊 进度查看

### 查看任务状态

```bash
# 查看所有并行任务状态
parallel-dev status

# 查看特定任务详情
parallel-dev status --task-id <task_id>
```

### 输出示例

```
┌─────────────────────────────────────────────┐
│  并行开发任务进度                              │
├─────────────────────────────────────────────┤
│  项目: 用户管理模块                           │
│  开始时间: 2026-04-08 21:00:00               │
├─────────────────────────────────────────────┤
│  📄 设计文档  [██████████] 100%  ✅ 完成     │
│  💻 代码开发  [████████░░]  80%  ⏳ 执行中   │
│  ✅ 测试用例  [██████████] 100%  ✅ 完成     │
└─────────────────────────────────────────────┘
```

## ⚠️ 注意事项

1. **需求文档质量**：需求文档越清晰，输出质量越高
2. **并行执行**：三个任务独立执行，互不影响
3. **资源消耗**：同时运行多个 agent，确保系统资源充足
4. **超时设置**：复杂项目建议增加超时时间
5. **结果验证**：完成后需要人工审核输出结果

## 🎯 最佳实践

### 1. 需求文档编写建议

```markdown
# 功能名称

## 业务背景
（描述业务场景）

## 功能需求
### 功能点1
- 输入：
- 处理：
- 输出：

### 功能点2
...

## 非功能需求
- 性能要求：
- 安全要求：

## 约束条件
- 技术栈：
- 编码规范：
```

### 2. 项目结构建议

```
project/
├── docs/
│   └── requirements/      # 需求文档
├── design/                # 设计文档
├── src/                   # 源代码
└── tests/                 # 测试用例
```

### 3. 迭代开发流程

```bash
# 第一轮：基础功能
parallel-dev ./需求/基础功能.md --project v1.0

# 第二轮：扩展功能
parallel-dev ./需求/扩展功能.md --project v1.1

# 第三轮：优化改进
parallel-dev ./需求/优化项.md --project v1.2
```

## 🔗 相关 Skills

- `alibaba-java-manual` - Java 编码规范
- `java-coding-standards` - Java 编码最佳实践
- `docx` - Word 文档处理
- `xlsx` - Excel 测试用例管理

## 📝 版本历史

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0.0 | 2026-04-08 | 初始版本，支持三agent并行开发 |

---

**💡 提示**：并行开发适合需求明确的场景。如果需求不够清晰，建议先进行需求分析和设计评审，再启动并行开发。
