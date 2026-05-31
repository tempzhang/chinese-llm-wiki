# Llama

## Overview
Llama 是 Meta 推出的开源大模型系列，广泛用于研究、企业私有化部署与二次训练。

## Key Concepts
- 开源权重与许可证
- 基础模型与指令版本
- 本地部署与推理优化
- 下游微调与对齐

## Architecture
- 预训练模型层
- 指令对齐层
- 推理服务层（API / 本地部署）
- 应用层（Agent / RAG / Automation）

## Workflow
1. 选择版本与许可策略
2. 部署推理服务
3. 对接检索或工具系统
4. 评测与迭代

## Best Practices
- 先做任务基线评测再选模型
- 控制上下文和提示词长度
- 与检索增强结合提升事实性

## Related Topics
- [LLM-Wiki](../llm-wiki/wiki/concepts/LLM-Wiki.md)
- [RAG](../llm-wiki/wiki/concepts/RAG.md)
- [MCP](../llm-wiki/wiki/concepts/MCP.md)

## Further Reading
- [RAG MOC](../MOCs/RAG-MOC.md)
