# NEXA TechHelp

> Assistente Inteligente de Suporte à Informática

O **NEXA TechHelp** é um protótipo de assistente virtual baseado em Inteligência Artificial para auxiliar usuários iniciantes na identificação e resolução de problemas básicos de informática.

O projeto foi desenvolvido como atividade prática do Lab **“Construa Seu Assistente Virtual Com Inteligência Artificial”**, adaptando o desafio para o contexto de suporte tecnológico.

## Problema

Usuários iniciantes frequentemente sabem descrever o sintoma de um problema, mas não sabem quais informações são relevantes para identificar sua causa ou quais procedimentos podem executar com segurança.

## Solução

O NEXA TechHelp utiliza:

- uma base de conhecimento estruturada;
- engenharia de prompts;
- uma LLM;
- uma interface de conversa;
- critérios de avaliação e segurança.

Seu princípio central é:

> **Diagnosticar antes de orientar.**

## Escopo

O protótipo contempla:

- Windows;
- hardware e software;
- arquivos e pastas;
- internet e conectividade;
- segurança digital;
- Google Workspace;
- LibreOffice;
- manutenção básica.

## Estrutura

```text
NEXA-TechHelp/
├── README.md
├── data/
│   └── base_conhecimento.json
├── docs/
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
└── src/
    ├── app.py
    ├── agente.py
    ├── config.py
    └── requirements.txt
```

## Fluxo

```text
Problema → investigação → conhecimento → orientação → verificação
```

## Segurança

O agente não deve solicitar senhas, códigos de autenticação ou outros dados confidenciais. Também deve evitar procedimentos destrutivos e admitir limitações quando não houver informação suficiente.

## Estado

Protótipo em desenvolvimento. As métricas finais dependem da execução dos cenários de teste definidos na documentação.

## Tecnologias

Python · Streamlit · OpenAI API · JSON · python-dotenv

## Lab de origem

[Digital Innovation One — dio-lab-bia-do-futuro](https://github.com/digitalinnovationone/dio-lab-bia-do-futuro)

## Autor

**SayjinBlackBelt — Filipe Gimenes de Morais**

Projeto do ecossistema **NEXA**.
