# Knowledge Graph

## Core Relationships

- LLM -> Agent: model intelligence is the core driver of agent reasoning.
- LLM -> MCP: LLM systems use MCP-style protocol layers for tool/context access.
- Agent -> RAG: agents use retrieval to improve factual grounding.
- RAG -> Vector DB: vector storage is the retrieval substrate.
- RAG -> Embedding: embedding quality determines retrieval quality.
- Agent -> Tools: agents call tools for execution beyond pure text.
- Agent -> Workflow: agents are embedded in repeatable workflows.
- Workflow -> Automation: stabilized workflows can be automated at scale.

## Ecosystem Map

- LLM Layer
  - [LLM-Wiki](llm-wiki/wiki/concepts/LLM-Wiki.md)
- Agent Layer
  - [AI-Agent知识维护](llm-wiki/wiki/concepts/AI-Agent知识维护.md)
- Protocol & Tool Layer
  - [MCP](llm-wiki/wiki/concepts/MCP.md)
  - [AI-Agent知识维护](llm-wiki/wiki/concepts/AI-Agent知识维护.md)
- Workflow & Automation Layer
  - [Wiki健康检查流程](llm-wiki/wiki/workflows/Wiki健康检查流程.md)
- Business Application Layer
  - [SEO工具](llm-wiki/wiki/concepts/SEO工具.md)

## Emerging Topics

- OpenAI (missing)
- ChatGPT (missing)
- GPT (missing)
- Claude (missing)
- Anthropic (missing)
- Gemini (missing)
- Google AI (missing)
- Qwen (missing)
- Alibaba (missing)
- Meta AI (missing)
- Llama (missing)
- Mistral (missing)
- Vector Database (missing)
- Embedding (missing)
- LangChain (missing)
- LangGraph (missing)
- CrewAI (missing)
- AutoGen (missing)
- OpenCode (missing)
- Claude Code (missing)
- n8n (missing)
- ComfyUI (missing)
- Stable Diffusion (missing)
- FLUX (missing)

## Relationship Table

| Source | Relation | Target | Note |
|---|---|---|---|
| [LLM-Wiki](llm-wiki/wiki/concepts/LLM-Wiki.md) | enables | [AI-Agent知识维护](llm-wiki/wiki/concepts/AI-Agent知识维护.md) | LLM capability powers agent cognition |
| [LLM-Wiki](llm-wiki/wiki/concepts/LLM-Wiki.md) | interfaces_via | [MCP](llm-wiki/wiki/concepts/MCP.md) | protocol layer for tool/context integration |
| [AI-Agent知识维护](llm-wiki/wiki/concepts/AI-Agent知识维护.md) | augments_with | [RAG](llm-wiki/wiki/concepts/RAG.md) | retrieval enhancement for factuality |
| [RAG](llm-wiki/wiki/concepts/RAG.md) | depends_on | Vector Database (missing) | foundational retrieval storage |
| [RAG](llm-wiki/wiki/concepts/RAG.md) | depends_on | Embedding (missing) | semantic vector representation |
| [AI-Agent知识维护](llm-wiki/wiki/concepts/AI-Agent知识维护.md) | executes_with | [AI-Agent知识维护](llm-wiki/wiki/concepts/AI-Agent知识维护.md) | tool invocation for actions |
| [AI-Agent知识维护](llm-wiki/wiki/concepts/AI-Agent知识维护.md) | orchestrated_in | [Wiki健康检查流程](llm-wiki/wiki/workflows/Wiki健康检查流程.md) | agent as workflow node |
| [Wiki健康检查流程](llm-wiki/wiki/workflows/Wiki健康检查流程.md) | evolves_to | (missing) | workflow standardization drives automation |