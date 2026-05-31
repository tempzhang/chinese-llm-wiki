# Qwen

## Overview
Qwen 是通义千问系列大模型，覆盖通用对话、代码、推理与多模态场景。

## Key Concepts
- Base / Instruct 模型
- 多语言能力
- 推理能力与工具调用能力
- 开源与商用生态

## Architecture
- 预训练层：大规模语料训练
- 对齐层：指令微调与偏好优化
- 应用层：Agent、RAG、自动化与代码助手

## Workflow
1. 选择场景对应模型版本
2. 设计提示与约束
3. 接入工具或检索系统
4. 评估输出质量并持续迭代

## Best Practices
- 明确任务边界，减少泛化误差
- 与 RAG/工具调用结合提升准确性
- 在生产环境建立评测基线

## Related Topics
- [LLM-Wiki](../llm-wiki/wiki/concepts/LLM-Wiki.md)
- [RAG](../llm-wiki/wiki/concepts/RAG.md)
- [MCP](../llm-wiki/wiki/concepts/MCP.md)

## Further Reading
- [RAG MOC](../MOCs/RAG-MOC.md)
- [MCP MOC](../MOCs/MCP-MOC.md)
