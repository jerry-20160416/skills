# Agent Skills Collection

这是一个 Agent Skills 仓库，包含各种实用的技能包，用于扩展 AI Agent 的能力。

## 📦 Skills 列表

### alibaba-java-manual

**阿里巴巴 Java 开发手册（黄山版 1.7.1）**

> 🏆 Java 社区集体智慧结晶，经历多次大规模一线实战检验

**包含内容：**
- 📝 **编程规约** - 命名风格、代码格式、OOP规约、并发处理等 11 个子分类
- ⚠️ **异常日志** - 错误码、异常处理、日志规约
- ✅ **单元测试** - 测试用例编写规范，100% 覆盖率要求
- 🔒 **安全规约** - 权限控制、SQL注入防护、敏感数据处理
- 🗄️ **MySQL 数据库** - 建表规约、索引设计、SQL语句规范
- 🏗️ **工程结构** - 应用分层、依赖管理、服务器配置
- 🎨 **设计规约** - 系统设计原则、模块划分规范

**快速安装：**
```bash
npx skills add jerry-20160416/skills@alibaba-java-manual
```

**详细文档：** [alibaba-java-manual/README.md](./skills/alibaba-java-manual/README.md)

**在线浏览：** https://github.com/jerry-20160416/skills/tree/master/skills/alibaba-java-manual

---

## 🚀 如何使用 Skills

### 安装 Skill

```bash
# 从本仓库安装
npx skills add jerry-20160416/skills@<skill-name>

# 查看已安装的 skills
npx skills list

# 全局安装
npx skills add jerry-20160416/skills@<skill-name> -g
```

### 使用 Skill

安装后，Agent 会自动加载相关 Skill，你可以直接询问问题：

```
"Java 类名应该怎么命名？"
"MySQL 建表有哪些规范？"
"如何正确处理异常？"
```

## 📚 更多资源

- **Skills 官网**：https://skills.sh/
- **Skills CLI 文档**：https://skills.sh/docs
- **阿里巴巴 Java 开发手册**：https://github.com/alibaba/p3c

## 🤝 贡献

欢迎提交 Issue 和 Pull Request 来贡献新的 Skill 或改进现有 Skill。

## 📄 License

MIT License
