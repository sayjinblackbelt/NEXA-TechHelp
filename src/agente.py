import json
from pathlib import Path

from openai import OpenAI

from config import OPENAI_API_KEY

BASE_PATH = Path(__file__).resolve().parent.parent / "data" / "base_conhecimento.json"

client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = """
Você é o NEXA TechHelp, um assistente inteligente de suporte à informática.
Seu público são usuários iniciantes em tecnologia.
Princípio: Diagnosticar antes de orientar.

Faça perguntas quando faltarem informações.
Use a base de conhecimento.
Não invente procedimentos.
Diferencie hipóteses de diagnósticos.
Priorize procedimentos simples, seguros e reversíveis.
Nunca solicite senhas ou códigos de autenticação.
Reconheça limitações e encaminhe casos avançados.
"""


def carregar_base():
    with open(BASE_PATH, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def buscar_conhecimento(pergunta, base):
    pergunta = pergunta.lower()
    resultados = []

    for item in base:
        texto = " ".join([
            item.get("categoria", ""),
            item.get("problema", ""),
            " ".join(item.get("sintomas", []))
        ]).lower()

        palavras = [p for p in pergunta.split() if len(p) > 3]

        if any(palavra in texto for palavra in palavras):
            resultados.append(item)

    return resultados[:3]


def gerar_resposta(pergunta, historico):
    base = carregar_base()
    conhecimento = buscar_conhecimento(pergunta, base)

    contexto = json.dumps(
        conhecimento,
        ensure_ascii=False,
        indent=2
    )

    mensagens = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "system",
            "content": (
                "Use o seguinte conhecimento como referência. "
                "Não invente informações.\n\n" + contexto
            )
        }
    ]

    mensagens.extend(historico)
    mensagens.append({"role": "user", "content": pergunta})

    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=mensagens,
        temperature=0.2
    )

    return resposta.choices[0].message.content
