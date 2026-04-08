@echo off
REM ================================================================
REM 并行开发启动脚本 (Windows)
REM 功能：同时启动三个agent处理需求文档
REM 用法：parallel-dev.bat <需求文档路径> [项目名称]
REM ================================================================

setlocal enabledelayedexpansion

REM 参数检查
if "%~1"=="" (
    echo 错误：缺少需求文档路径
    echo 用法：parallel-dev.bat ^<需求文档路径^> [项目名称]
    echo 示例：parallel-dev.bat .\docs\需求文档.md 用户管理模块
    exit /b 1
)

set REQUIREMENT_DOC=%~1
set PROJECT_NAME=%~2
if "%PROJECT_NAME%"=="" set PROJECT_NAME=project

REM 获取时间戳
for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set datetime=%%I
set TIMESTAMP=%datetime:~0,8%_%datetime:~8,6%

echo ================================================================
echo 并行开发任务启动
echo ================================================================
echo 需求文档: %REQUIREMENT_DOC%
echo 项目名称: %PROJECT_NAME%
echo 时间戳: %TIMESTAMP%
echo ================================================================
echo.

REM 检查需求文档是否存在
if not exist "%REQUIREMENT_DOC%" (
    echo 错误：需求文档不存在 - %REQUIREMENT_DOC%
    exit /b 1
)

REM 创建输出目录
echo 创建输出目录...
set OUTPUT_DIR=deliverables\%PROJECT_NAME%_%TIMESTAMP%
mkdir "%OUTPUT_DIR%\design" 2>nul
mkdir "%OUTPUT_DIR%\code" 2>nul
mkdir "%OUTPUT_DIR%\testcases" 2>nul
echo 输出目录: %OUTPUT_DIR%
echo.

REM 查询可用agents
echo 查询可用的 Agents...
copaw agents list
echo.

REM 提示用户输入agent名称
set /p DESIGN_AGENT="请输入设计文档Agent名称 (默认: design_agent): "
if "%DESIGN_AGENT%"=="" set DESIGN_AGENT=design_agent

set /p CODE_AGENT="请输入代码开发Agent名称 (默认: code_agent): "
if "%CODE_AGENT%"=="" set CODE_AGENT=code_agent

set /p TEST_AGENT="请输入测试用例Agent名称 (默认: test_agent): "
if "%TEST_AGENT%"=="" set TEST_AGENT=test_agent

echo.
echo ================================================================
echo 提交并行任务...
echo ================================================================
echo.

REM 提交设计文档任务
echo [1/3] 提交设计文档任务...
copaw agents chat --background ^
  --from-agent default ^
  --to-agent %DESIGN_AGENT% ^
  --text "[Agent default requesting] 根据需求文档 '%REQUIREMENT_DOC%' 编写详细设计文档。要求：1. 系统架构设计 2. 数据库表设计（包含ER图和DDL脚本） 3. 接口设计（包含请求参数和响应格式） 4. 业务流程设计。输出到 '%OUTPUT_DIR%\design\' 目录。请按照标准的软件设计文档格式编写。"

echo.
echo 设计任务已提交
echo.

REM 提交代码开发任务
echo [2/3] 提交代码开发任务...
copaw agents chat --background ^
  --from-agent default ^
  --to-agent %CODE_AGENT% ^
  --text "[Agent default requesting] 根据需求文档 '%REQUIREMENT_DOC%' 实现代码。要求：1. 使用 Spring Boot 框架 2. 遵循阿里巴巴Java开发规范 3. 实现完整的业务逻辑 4. 包含必要的注释和文档 5. 遵循分层架构（Controller-Service-Repository）。输出到 '%OUTPUT_DIR%\code\' 目录。"

echo.
echo 代码任务已提交
echo.

REM 提交测试用例任务
echo [3/3] 提交测试用例任务...
copaw agents chat --background ^
  --from-agent default ^
  --to-agent %TEST_AGENT% ^
  --text "[Agent default requesting] 根据需求文档 '%REQUIREMENT_DOC%' 编写测试用例。要求：1. 功能测试用例（正常流程） 2. 异常测试用例（异常流程和错误处理） 3. 边界值测试用例 4. 接口测试用例（包含请求参数和预期结果）。输出到 '%OUTPUT_DIR%\testcases\' 目录。使用Markdown表格格式。"

echo.
echo 测试任务已提交
echo.

echo ================================================================
echo 所有任务已提交！
echo ================================================================
echo.
echo 三个 Agent 正在后台并行执行...
echo.
echo 输出目录: %OUTPUT_DIR%\
echo   - design/       (设计文档)
echo   - code/         (源代码)
echo   - testcases/    (测试用例)
echo.
echo 提示：任务可能需要 1-5 分钟完成
echo       请使用 'copaw agents chat --background --task-id ^<TASK_ID^>' 查询状态
echo.
echo ================================================================
echo 按任意键退出...
pause >nul
