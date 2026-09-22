# NEXA TechHelp — Documentação do Agente

## Caso de uso

O NEXA TechHelp foi concebido para auxiliar usuários iniciantes em tecnologia a identificar e resolver problemas básicos de informática.

### Problema

O usuário frequentemente conhece apenas o sintoma do problema, mas não sabe como investigá-lo.

### Solução

Um assistente de IA conduz uma investigação simples, consulta uma base de conhecimento e apresenta orientações graduais e seguras.

### Princípio

> Diagnosticar antes de orientar.

## Público-alvo

Usuários iniciantes em tecnologia.

## Áreas

Windows, hardware, software, arquivos e pastas, internet, segurança digital, Google Workspace, LibreOffice e manutenção básica.

## Persona

Assistente técnico paciente, didático, claro e orientado à solução.

## Arquitetura

```text
Usuário
  ↓
Interface
  ↓
Agente
  ↓
Base de conhecimento
  ↓
LLM
  ↓
Resposta
  ↓
Verificação
```

## Segurança

- Não solicitar senhas ou códigos de autenticação.
- Evitar procedimentos destrutivos.
- Diferenciar hipótese de diagnóstico.
- Priorizar procedimentos simples, seguros e reversíveis.
- Encaminhar situações avançadas para suporte especializado.

## Critérios de sucesso

Precisão, uso da base, qualidade do diagnóstico, clareza, segurança e comportamento de fallback.
