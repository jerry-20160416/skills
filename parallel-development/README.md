# 并行开发 Skill

> 🚀 同时启动多个 agent 处理需求文档，分别生成设计文档、代码实现和测试用例

## 📖 简介

这是一个利用 CoPaw 多 agent 协作能力实现的**并行开发** skill。通过后台模式同时启动三个专业 agent，大幅缩短从需求到交付的周期。

### 核心优势

- ⚡ **并行执行**：三个任务同时运行，节省时间
- 🎯 **专业分工**：每个 agent 专注自己的领域
- 📦 **完整交付**：一次性输出设计、代码、测试
- 🔄 **标准流程**：统一的工作流程和输出格式

## 🚀 快速开始

### 方式一：使用脚本（推荐）

```bash
# Windows
parallel-dev.bat <需求文档路径> [项目名称]

# 示例
parallel-dev.bat .\docs\用户管理模块需求.md 用户管理模块
```

### 方式二：手动执行

查看 [GUIDE.md](./GUIDE.md) 了解详细的手动执行步骤。

### 方式三：交互式使用

直接告诉你的 agent：

```
我有一份需求文档在 ./requirements/订单系统.md，
请启动并行开发流程，生成设计文档、代码和测试用例
```

## 📂 文件说明

```
parallel-development/
├── SKILL.md              # Skill 定义文件（Agent 自动读取）
├── GUIDE.md              # 详细实施指南（手动执行参考）
├── TEMPLATE.md           # 需求文档模板
├── parallel-dev.bat      # Windows 启动脚本
├── parallel-dev.sh       # Linux/Mac 启动脚本（待创建）
└── README.md             # 本文件
```

## 🔄 工作流程

```
┌──────────────────────────────────────────────────────┐
│                   需求文档输入                        │
│              (Markdown/Word/PDF/TXT)                │
└────────────────────┬─────────────────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────────────────┐
│              并行启动三个 Agent                       │
│          (使用 --background 后台模式)                │
└──────┬───────────────┬───────────────┬───────────────┘
       │               │               │
       ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  📄 设计Agent │ │  💻 代码Agent │ │  ✅ 测试Agent │
└──────┬───────┘ └──────┬───────┘ └──────┬───────┘
       │               │               │
       ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  设计文档     │ │  源代码       │ │  测试用例     │
│  - 架构设计   │ │  - 业务逻辑   │ │  - 功能测试   │
│  - 数据库设计 │ │  - 接口实现   │ │  - 异常测试   │
│  - 接口设计   │ │  - 配置文件   │ │  - 边界测试   │
└──────────────┘ └──────────────┘ └──────────────┘
```

## 📋 输出结构

执行完成后，会在 `deliverables/<项目名称>_<时间戳>/` 目录下生成：

```
deliverables/
└── 用户管理模块_20260408_210000/
    ├── design/                      # 设计文档
    │   ├── 系统设计文档_v1.0.0.md
    │   ├── 数据库DDL.sql
    │   └── 接口文档.md
    │
    ├── code/                        # 源代码
    │   ├── src/
    │   │   ├── main/
    │   │   │   ├── java/
    │   │   │   │   ├── controller/
    │   │   │   │   ├── service/
    │   │   │   │   ├── repository/
    │   │   │   │   └── entity/
    │   │   │   └── resources/
    │   │   │       ├── application.yml
    │   │   │       └── mapper/
    │   │   └── test/
    │   └── pom.xml
    │
    └── testcases/                   # 测试用例
        ├── 功能测试用例.md
        ├── 接口测试用例.md
        └── 边界值测试用例.md
```

## ⚙️ 配置要求

### 必需的 Agent

确保你的 CoPaw 系统中有以下 agent（或类似功能）：

| Agent 名称 | 功能 | 输出 |
|-----------|------|------|
| `design_agent` | 编写设计文档 | 系统设计、数据库设计、接口设计 |
| `code_agent` | 实现代码 | 完整的 Spring Boot 项目代码 |
| `test_agent` | 编写测试用例 | 功能测试、接口测试用例 |

### 查看可用 Agent

```bash
copaw agents list
```

如果 agent 名称不同，可以在执行脚本时自定义。

## 📝 需求文档要求

### 必需内容

需求文档应该包含：

- ✅ **功能需求**：明确的功能点和业务流程
- ✅ **数据需求**：数据实体和字段定义
- ✅ **接口需求**：接口列表和参数定义
- ✅ **约束条件**：技术栈、编码规范等

### 推荐格式

使用 [TEMPLATE.md](./TEMPLATE.md) 模板编写需求文档，确保内容完整。

### 示例需求文档

```markdown
# 用户管理模块需求文档

## 1. 业务背景
实现用户信息的增删改查功能...

## 2. 功能需求
### 2.1 用户列表查询
- 输入：pageNum, pageSize, keyword
- 输出：用户列表（分页）
- 处理：...

### 2.2 用户新增
- 输入：用户信息（name, email, phone）
- 输出：新增用户ID
- 处理：...

## 3. 数据需求
### 用户表 (user)
| 字段 | 类型 | 说明 |
|------|------|------|
| id | Long | 主键 |
| name | String | 姓名 |
| email | String | 邮箱 |

## 4. 接口需求
GET /api/v1/users - 查询用户列表
POST /api/v1/users - 新增用户
...
```

## 🎯 使用场景

### ✅ 适合的场景

- 需求文档明确清晰
- 标准的 CRUD 功能
- Spring Boot 项目
- 需要快速原型开发
- 团队协作开发

### ❌ 不适合的场景

- 需求不明确，需要反复讨论
- 复杂的业务算法
- 特殊技术栈要求
- 需要人工审核设计的场景

## ⚠️ 注意事项

### 1. 需求文档质量

需求文档越详细，输出质量越高。建议：
- 功能点描述清楚
- 数据结构定义完整
- 接口参数明确
- 异常处理说明

### 2. 任务监控

提交任务后，可以通过以下方式监控：

```bash
# 查询任务状态（使用返回的 TASK_ID）
copaw agents chat --background --task-id <TASK_ID>

# 建议等待时间
# - 设计文档：30-60秒
# - 代码开发：60-120秒
# - 测试用例：30-60秒
```

### 3. 结果验证

并行开发完成后，建议：
- 检查设计文档的完整性
- 验证代码能否编译运行
- 审核测试用例覆盖率

### 4. 资源消耗

同时运行三个 agent 会消耗：
- CPU：多线程处理
- 内存：建议 8GB+
- API 调用：确保配额充足

## 🔧 高级用法

### 仅执行单个任务

如果只需要特定输出：

```bash
# 仅生成设计文档
copaw agents chat --background \
  --from-agent default \
  --to-agent design_agent \
  --text "[Agent default requesting] 根据需求文档 xxx 编写设计文档..."

# 仅生成代码
copaw agents chat --background \
  --from-agent default \
  --to-agent code_agent \
  --text "[Agent default requesting] 根据需求文档 xxx 实现代码..."

# 仅生成测试用例
copaw agents chat --background \
  --from-agent default \
  --to-agent test_agent \
  --text "[Agent default requesting] 根据需求文档 xxx 编写测试用例..."
```

### 自定义 Agent

如果 agent 名称不同：

```bash
# 修改脚本中的 agent 名称
set DESIGN_AGENT=your_design_agent
set CODE_AGENT=your_code_agent
set TEST_AGENT=your_test_agent
```

### 指定输出目录

修改脚本中的 `OUTPUT_DIR` 变量：

```bash
set OUTPUT_DIR=D:\projects\%PROJECT_NAME%
```

## 📊 性能对比

| 开发方式 | 耗时 | 说明 |
|---------|------|------|
| 串行开发 | 3-5 小时 | 依次完成设计→代码→测试 |
| 并行开发 | 1-2 小时 | 同时进行，节省 60%+ 时间 |

## 🔗 相关资源

- [GUIDE.md](./GUIDE.md) - 详细实施指南
- [TEMPLATE.md](./TEMPLATE.md) - 需求文档模板
- [Multi-Agent Collaboration Skill](../multi_agent_collaboration/) - 多 agent 协作基础

## 📝 版本历史

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0.0 | 2026-04-08 | 初始版本 |

## 💬 反馈与建议

如果你在使用过程中遇到问题或有改进建议，欢迎反馈！

---

**快速开始**：准备好需求文档，运行 `parallel-dev.bat <需求文档路径>` 即可启动并行开发！🚀
