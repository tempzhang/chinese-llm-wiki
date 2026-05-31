# CrewAI

## Overview
CrewAI 聚焦“多 Agent 协作”，通过角色分工与任务委派提升复杂任务完成质量。

## Key Concepts
- Role（角色）
- Task（任务）
- Crew（协作组）
- Delegation（委派）
- Coordination（协同）

## Architecture
- 角色层：定义不同 Agent 的职责
- 任务层：拆分目标为可执行子任务
- 协作层：协调上下游 Agent 的输入输出
- 评估层：汇总结果并做质量检查

## Workflow
1. 定义目标与角色
2. 拆分子任务并分配
3. 多 Agent 并行/串行执行
4. 聚合结果并评估
5. 交付最终产出

## Best Practices
- 角色边界清晰，减少职责重叠
- 对关键节点加入人工审阅点
- 为每个子任务定义可验证输出

## Related Topics
- [Agent MOC](../MOCs/Agent-MOC.md)
- [AI-Agent框架](../llm-wiki/wiki/comparisons/AI-Agent框架.md)
- [自动化工具对比](../llm-wiki/wiki/comparisons/自动化工具对比.md)

## Further Reading
- [Automation MOC](../MOCs/Automation-MOC.md)
