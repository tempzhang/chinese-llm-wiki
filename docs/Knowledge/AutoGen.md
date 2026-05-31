# AutoGen

## Overview
AutoGen 强调多智能体对话与自动协作，通过消息驱动方式组织复杂任务执行。

## Key Concepts
- Agent Conversation（多 Agent 对话）
- Tool Use（工具使用）
- Planner / Worker（规划与执行分工）
- Termination Condition（终止条件）

## Architecture
- 会话层：Agent 间消息交换
- 调度层：任务路由与回合控制
- 工具层：外部系统调用
- 监控层：日志与执行可视化

## Workflow
1. 初始化角色与目标
2. 启动多 Agent 回合对话
3. 在回合中调用工具与外部资源
4. 依据终止条件收敛结果
5. 输出结构化结论

## Best Practices
- 预设最大回合数，防止无效循环
- 使用明确的终止条件与验收标准
- 对关键回合保留可审计日志

## Related Topics
- [Agent MOC](../MOCs/Agent-MOC.md)
- [MCP MOC](../MOCs/MCP-MOC.md)
- [Codex](../llm-wiki/wiki/concepts/Codex.md)

## Further Reading
- [AI-Agent知识维护](../llm-wiki/wiki/concepts/AI-Agent知识维护.md)
