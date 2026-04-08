# 并行开发实施指南

本文档详细说明如何使用 `copaw agents chat` 命令实现多个 agent 并行处理需求文档。

## 核心原理

使用 `--background` 后台模式同时启动多个 agent，实现真正的并行处理。

## 实施步骤

### 第一步：查询可用 Agents

```bash
copaw agents list
```

记录可用的 agent ID，通常需要：
- `design_agent` - 设计文档编写
- `code_agent` - 代码开发
- `test_agent` - 测试用例编写

### 第二步：准备需求文档

将需求文档放在可访问的路径，例如：
```
./requirements/用户管理模块需求.md
```

### 第三步：并行启动三个 Agent

**关键**：使用 `--background` 模式，三个命令**同时提交**，不等待结果。

```bash
# 提交设计文档任务（后台）
copaw agents chat --background \
  --from-agent default \
  --to-agent design_agent \
  --text "[Agent default requesting] 根据需求文档 ./requirements/用户管理模块需求.md 编写详细设计文档，包含：
1. 系统架构设计
2. 数据库表设计（ER图）
3. 接口设计（API定义）
4. 业务流程设计
输出到 ./deliverables/design/ 目录"

# 提交代码开发任务（后台）
copaw agents chat --background \
  --from-agent default \
  --to-agent code_agent \
  --text "[Agent default requesting] 根据需求文档 ./requirements/用户管理模块需求.md 实现代码，要求：
1. 使用 Spring Boot 框架
2. 遵循阿里巴巴Java开发规范
3. 实现完整的业务逻辑
4. 包含必要的注释
输出到 ./deliverables/code/ 目录"

# 提交测试用例任务（后台）
copaw agents chat --background \
  --from-agent default \
  --to-agent test_agent \
  --text "[Agent default requesting] 根据需求文档 ./requirements/用户管理模块需求.md 编写测试用例，包含：
1. 功能测试用例（正常流程）
2. 异常测试用例（异常流程）
3. 边界值测试用例
4. 接口测试用例
输出到 ./deliverables/testcases/ 目录"
```

### 第四步：记录任务 ID

每个命令会返回任务 ID，记录下来：

```bash
# 设计任务
[TASK_ID: design-task-xxx-xxx]
[SESSION: default:to:design_agent:...]

# 代码任务
[TASK_ID: code-task-xxx-xxx]
[SESSION: default:to:code_agent:...]

# 测试任务
[TASK_ID: test-task-xxx-xxx]
[SESSION: default:to:test_agent:...]
```

### 第五步：等待并查询结果

**重要**：不要立即查询，等待合理时间后再查。

```bash
# 等待 30 秒后查询设计任务
sleep 30 && copaw agents chat --background --task-id design-task-xxx-xxx

# 等待 30 秒后查询代码任务
sleep 30 && copaw agents chat --background --task-id code-task-xxx-xxx

# 等待 30 秒后查询测试任务
sleep 30 && copaw agents chat --background --task-id test-task-xxx-xxx
```

### 第六步：汇总结果

所有任务完成后，整理输出文件：

```bash
# 查看生成的文件
ls ./deliverables/design/
ls ./deliverables/code/
ls ./deliverables/testcases/
```

## 完整脚本示例

### parallel-dev.sh

```bash
#!/bin/bash

# 并行开发脚本
# 用法: ./parallel-dev.sh <需求文档路径> [项目名称]

REQUIREMENT_DOC=$1
PROJECT_NAME=${2:-"project"}
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

echo "================================"
echo "并行开发任务启动"
echo "需求文档: $REQUIREMENT_DOC"
echo "项目名称: $PROJECT_NAME"
echo "时间戳: $TIMESTAMP"
echo "================================"

# 创建输出目录
mkdir -p ./deliverables/$PROJECT_NAME/{design,code,testcases}

# 提交设计任务
echo "提交设计文档任务..."
DESIGN_TASK=$(copaw agents chat --background \
  --from-agent default \
  --to-agent design_agent \
  --text "[Agent default requesting] 根据需求文档 $REQUIREMENT_DOC 编写详细设计文档，输出到 ./deliverables/$PROJECT_NAME/design/" \
  | grep -oP '\[TASK_ID: \K[^\]]+')

echo "设计任务ID: $DESIGN_TASK"

# 提交代码任务
echo "提交代码开发任务..."
CODE_TASK=$(copaw agents chat --background \
  --from-agent default \
  --to-agent code_agent \
  --text "[Agent default requesting] 根据需求文档 $REQUIREMENT_DOC 实现代码，输出到 ./deliverables/$PROJECT_NAME/code/" \
  | grep -oP '\[TASK_ID: \K[^\]]+')

echo "代码任务ID: $CODE_TASK"

# 提交测试任务
echo "提交测试用例任务..."
TEST_TASK=$(copaw agents chat --background \
  --from-agent default \
  --to-agent test_agent \
  --text "[Agent default requesting] 根据需求文档 $REQUIREMENT_DOC 编写测试用例，输出到 ./deliverables/$PROJECT_NAME/testcases/" \
  | grep -oP '\[TASK_ID: \K[^\]]+')

echo "测试任务ID: $TEST_TASK"

echo "================================"
echo "所有任务已提交，后台并行执行中..."
echo "================================"

# 等待任务完成
echo "等待 60 秒后查询结果..."
sleep 60

echo "================================"
echo "查询设计任务状态..."
copaw agents chat --background --task-id $DESIGN_TASK

echo "================================"
echo "查询代码任务状态..."
copaw agents chat --background --task-id $CODE_TASK

echo "================================"
echo "查询测试任务状态..."
copaw agents chat --background --task-id $TEST_TASK

echo "================================"
echo "任务完成！请检查 ./deliverables/$PROJECT_NAME/ 目录"
echo "================================"
```

### parallel-dev.bat (Windows)

```batch
@echo off
REM 并行开发脚本 (Windows)
REM 用法: parallel-dev.bat <需求文档路径> [项目名称]

set REQUIREMENT_DOC=%1
set PROJECT_NAME=%2
if "%PROJECT_NAME%"=="" set PROJECT_NAME=project

echo ================================
echo 并行开发任务启动
echo 需求文档: %REQUIREMENT_DOC%
echo 项目名称: %PROJECT_NAME%
echo ================================

REM 创建输出目录
mkdir deliverables\%PROJECT_NAME%\design 2>nul
mkdir deliverables\%PROJECT_NAME%\code 2>nul
mkdir deliverables\%PROJECT_NAME%\testcases 2>nul

REM 提交设计任务
echo 提交设计文档任务...
copaw agents chat --background --from-agent default --to-agent design_agent --text "[Agent default requesting] 根据需求文档 %REQUIREMENT_DOC% 编写详细设计文档，输出到 ./deliverables/%PROJECT_NAME%/design/"

REM 提交代码任务
echo 提交代码开发任务...
copaw agents chat --background --from-agent default --to-agent code_agent --text "[Agent default requesting] 根据需求文档 %REQUIREMENT_DOC% 实现代码，输出到 ./deliverables/%PROJECT_NAME%/code/"

REM 提交测试任务
echo 提交测试用例任务...
copaw agents chat --background --from-agent default --to-agent test_agent --text "[Agent default requesting] 根据需求文档 %REQUIREMENT_DOC% 编写测试用例，输出到 ./deliverables/%PROJECT_NAME%/testcases/"

echo ================================
echo 所有任务已提交，后台并行执行中...
echo ================================

echo 等待 60 秒后查询结果...
timeout /t 60 /nobreak

echo 请手动查询任务状态（使用返回的 TASK_ID）
```

## 进度监控函数

### 查询所有任务状态

```bash
# 定义函数
check_all_tasks() {
    local task_ids=("$@")

    for task_id in "${task_ids[@]}"; do
        echo "查询任务: $task_id"
        copaw agents chat --background --task-id $task_id
        echo "---"
    done
}

# 使用
check_all_tasks "design-task-xxx" "code-task-xxx" "test-task-xxx"
```

### 轮询直到完成

```bash
wait_for_task() {
    local task_id=$1
    local max_wait=300  # 最大等待时间（秒）
    local interval=10   # 查询间隔（秒）
    local elapsed=0

    while [ $elapsed -lt $max_wait ]; do
        result=$(copaw agents chat --background --task-id $task_id)

        if echo "$result" | grep -q "STATUS: finished"; then
            echo "任务完成: $task_id"
            echo "$result"
            return 0
        fi

        echo "任务进行中... 已等待 ${elapsed} 秒"
        sleep $interval
        elapsed=$((elapsed + interval))
    done

    echo "任务超时: $task_id"
    return 1
}

# 使用
wait_for_task "design-task-xxx"
```

## 注意事项

### 1. 不要频繁查询

```bash
# ❌ 错误：查询太频繁
while true; do
    copaw agents chat --background --task-id $task_id
    sleep 1
done

# ✅ 正确：合理间隔
sleep 30 && copaw agents chat --background --task-id $task_id
```

### 2. 避免阻塞

```bash
# ❌ 错误：顺序提交（失去并行优势）
copaw agents chat --background --to-agent design_agent --text "..." --wait
copaw agents chat --background --to-agent code_agent --text "..." --wait
copaw agents chat --background --to-agent test_agent --text "..." --wait

# ✅ 正确：并行提交
copaw agents chat --background --to-agent design_agent --text "..." &
copaw agents chat --background --to-agent code_agent --text "..." &
copaw agents chat --background --to-agent test_agent --text "..." &
```

### 3. 资源管理

同时运行多个 agent 会消耗较多资源，确保：
- 系统内存充足（建议 8GB+）
- 网络连接稳定
- API 配额充足

### 4. 错误处理

```bash
# 检查任务是否失败
result=$(copaw agents chat --background --task-id $task_id)

if echo "$result" | grep -q "Task failed"; then
    echo "任务失败，查看错误信息："
    echo "$result"
    # 处理错误...
fi
```

## 性能优化

### 1. 任务依赖处理

如果有依赖关系（比如代码需要等设计完成），可以：

```bash
# 先提交设计任务
design_task=$(copaw agents chat --background ...)

# 等待设计完成
wait_for_task $design_task

# 再提交代码任务
code_task=$(copaw agents chat --background ...)
```

### 2. 批量处理

如果有多份需求文档：

```bash
for doc in ./requirements/*.md; do
    project_name=$(basename $doc .md)
    ./parallel-dev.sh $doc $project_name &
done

wait  # 等待所有项目完成
```

## 故障排查

### 任务卡住

```bash
# 查看任务状态
copaw agents chat --background --task-id <task_id>

# 如果长时间 running，可以：
# 1. 等待更长时间
# 2. 检查 agent 日志
# 3. 重新提交任务
```

### 任务失败

```bash
# 查看错误详情
copaw agents chat --background --task-id <task_id>

# 常见原因：
# 1. 需求文档路径错误
# 2. 输出目录无权限
# 3. Agent 超时
# 4. API 错误
```

---

**提示**：并行开发的核心优势是**同时执行**，确保使用 `--background` 模式并且不要等待单个任务完成再提交下一个。
