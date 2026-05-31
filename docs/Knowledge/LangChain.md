# LangChain

## Overview
LangChain 是面向 LLM 应用开发的组件化框架，常用于构建 RAG、Agent 与工具链应用。

## Key Concepts
- Chain（链式执行）
- Retriever（检索器）
- Tool（工具）
- Agent（智能体）
- Memory（记忆）

## Architecture
- 组件层：Prompt、LLM、Retriever、Tool
- 编排层：Chain / Agent Workflow
- 集成层：向量库、外部 API、数据源

## Workflow
1. 定义输入与目标输出
2. 组装链式流程或 Agent
3. 接入检索和工具调用
4. 评估并迭代优化

## Best Practices
- 保持链路最小可解释
- 先验证检索质量，再扩展复杂编排
- 将可复用能力封装为组件

## Related Topics
- [RAG MOC](../MOCs/RAG-MOC.md)
- [Agent MOC](../MOCs/Agent-MOC.md)
- [RAG](../llm-wiki/wiki/concepts/RAG.md)

## Further Reading
- [知识编译](../llm-wiki/wiki/concepts/知识编译.md)
