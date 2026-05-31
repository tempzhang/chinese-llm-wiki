# ComfyUI

## Overview
ComfyUI 是节点式 AIGC 工作流工具，常用于图像生成、模型组合与推理流程控制。

## Key Concepts
- Node Graph（节点图）
- Model Loader（模型加载）
- Prompt Pipeline（提示词管线）
- Sampler（采样器）
- Post-process（后处理）

## Architecture
- 可视化编排层：拖拽式节点连接
- 推理执行层：模型推理与中间结果传递
- 资源层：模型、LoRA、ControlNet 等资产管理

## Workflow
1. 选择基础模型
2. 组装提示词与采样节点
3. 运行推理并预览结果
4. 调整参数迭代
5. 导出最终产物

## Best Practices
- 将常用流程固化为模板图
- 控制节点复杂度，避免超大图难维护
- 为关键参数建立实验记录

## Related Topics
- [AI-Coding MOC](../MOCs/AI-Coding-MOC.md)
- [Automation MOC](../MOCs/Automation-MOC.md)

## Further Reading
- [工具导航站](../llm-wiki/wiki/concepts/工具导航站.md)
