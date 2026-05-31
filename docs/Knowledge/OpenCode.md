# OpenCode

## Overview
OpenCode 指开源代码智能体/编码助手生态，强调可控、可扩展和本地化集成能力。

## Key Concepts
- Code Generation（代码生成）
- Code Review（代码审查）
- Tool Invocation（工具调用）
- Local Execution（本地执行）

## Architecture
- 模型层：代码模型或通用大模型
- 代理层：任务分解、上下文管理、执行控制
- 工具层：终端、Git、测试、静态分析

## Workflow
1. 输入任务目标与约束
2. 生成候选实现
3. 运行测试与静态检查
4. 回归修复并形成交付

## Best Practices
- 人机协作而非全自动盲执行
- 先小范围验证再扩大改动面
- 固化“生成-验证-回归”闭环

## Related Topics
- [AI-Coding MOC](../MOCs/AI-Coding-MOC.md)
- [Codex](../llm-wiki/wiki/concepts/Codex.md)
- [AI-Agent知识维护](../llm-wiki/wiki/concepts/AI-Agent知识维护.md)

## Further Reading
- [Reasonix](../llm-wiki/wiki/concepts/Reasonix.md)
- [HyperFrames](../llm-wiki/wiki/concepts/HyperFrames.md)
