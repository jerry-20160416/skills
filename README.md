# Skills

个人技能仓库，包含 CoPaw Agent 可用的各类技能模块。

## 目录

| Skill | 描述 | 状态 |
|-------|------|------|
| [v2x-cc-design](./v2x-cc-design) | 车路云项目模块设计文档生成 - 按照10章节标准模板撰写详细设计文档 | ✅ 可用 |
| [alibaba-java-manual](./alibaba-java-manual) | 阿里巴巴 Java 开发手册（黄山版）- 包含编程规约、异常日志、单元测试、安全规约、MySQL数据库、工程结构、设计规约七大维度 | ✅ 可用 |
| [multi_agent_collaboration](./multi_agent_collaboration) | 多智能体协作 - 当需要其他 agent 的专长/上下文时，使用 copaw agents chat 进行双向通信 | ✅ 可用 |

---

## Skill 说明

### v2x-cc-design

**用途：** 按车路云项目标准模板生成模块详细设计文档

**触发词：** 设计文档、详细设计、模块设计、v2x设计

**包含章节：**
1. 变更历史
2. 文档目录
3. 技术栈
4. 模块与文档对应关系
5. 用例设计（角色定义、功能矩阵、数据权限矩阵）
6. 数据库设计（表清单、表结构、约束对照表）
7. 接口设计（接口概览、详细设计、错误码）
8. 业务逻辑设计（流程图、异常处理）
9. 安全设计（整体安全、模块安全、脱敏字段）
10. 性能设计（指标要求、优化策略）

---

### alibaba-java-manual

**用途：** Java 开发规范参考，代码审查标准

**触发词：** Java规范、命名规范、代码审查、阿里规范

**包含维度：**
- 编程规约（命名风格、常量定义、代码格式、OOP规约等）
- 异常日志（错误码、异常处理、日志规约）
- 单元测试
- 安全规约
- MySQL 数据库（建表规约、索引规约、SQL语句）
- 工程结构（应用分层、二方库依赖）
- 设计规约

---

### multi_agent_collaboration

**用途：** 多智能体协作，调用其他 agent 的专长

**触发词：** 调用agent、多智能体、协作

**核心命令：**
```bash
# 查询可用 agents
copaw agents list

# 发起对话
copaw agents chat --from-agent <your_agent> --to-agent <target_agent> --text "..."

# 后台任务
copaw agents chat --background --from-agent <your_agent> --to-agent <target_agent> --text "..."
```

---

## 使用方式

将 Skill 目录复制到 CoPaw workspace 的 `skills/` 目录下即可自动识别。

```bash
# 安装到 workspace
cp -r <skill-name> ~/.copaw/workspaces/<workspace>/skills/

# 启用 skill
copaw skills config
```

---

## 维护者

- jerry-20160416
