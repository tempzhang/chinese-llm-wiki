# LangGraph

## Overview
LangGraph 是面向 Agent 工作流编排的框架，强调“状态机 + 节点图”来组织复杂任务执行。

## Key Concepts
- State（状态对象）
- Node（执行节点）
- Edge（状态转移）
- Graph Execution（图执行）
- Checkpoint（恢复点）

## Architecture
- 编排层：定义图结构与节点关系
- 执行层：按状态流转触发节点
- 记忆层：状态持久化与恢复
- 观测层：执行日志、轨迹与调试

## Workflow
1. 定义状态模型
2. 注册节点与边
3. 运行图并流转状态
4. 在关键节点进行工具调用与结果校验
5. 输出结果并持久化

## Best Practices
- 先画最小可运行图，再逐步扩展节点
- 将工具调用封装为独立节点，便于复用
- 为失败路径设计回退边和重试策略

## Related Topics
- [Agent MOC](../MOCs/Agent-MOC.md)
- [MCP](../llm-wiki/wiki/concepts/MCP.md)
- [RAG](../llm-wiki/wiki/concepts/RAG.md)
- [AI-Agent知识维护](../llm-wiki/wiki/concepts/AI-Agent知识维护.md)

## Further Reading
- [MCP MOC](../MOCs/MCP-MOC.md)
- [RAG MOC](../MOCs/RAG-MOC.md)
