# NEXA TechHelp — Pitch

## Problema

Usuários iniciantes frequentemente sabem apenas descrever o sintoma de um problema de informática.

## Solução

O NEXA TechHelp combina IA generativa, base de conhecimento e engenharia de prompts para conduzir um diagnóstico inicial e oferecer orientações simples e seguras.

## Diferencial

> Diagnosticar antes de orientar.

O agente deve evitar respostas inventadas e reconhecer quando não possui informação suficiente.

## Fluxo

```text
Problema
↓
Investigação
↓
Base de conhecimento
↓
LLM
↓
Orientação
↓
Verificação
```

## Avaliação

O protótipo será avaliado em 10 cenários com seis dimensões, totalizando 120 pontos possíveis.

Os resultados finais serão inseridos após a execução dos testes.

## Tecnologias

Python, Streamlit, OpenAI API, JSON e python-dotenv.

## Evolução

Possíveis evoluções incluem recuperação semântica/RAG, base de conhecimento expandida, histórico, feedback do usuário e métricas automatizadas.
