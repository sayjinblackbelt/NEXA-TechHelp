import json
from pathlib import Path

from google import genai

from .config import GEMINI_API_KEY


BASE_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "base_conhecimento.json"
)


client = genai.Client(api_key=GEMINI_API_KEY)


SYSTEM_PROMPT = """
Você é o NEXA TechHelp, um assistente inteligente de suporte à informática.

Seu público são usuários iniciantes em tecnologia.

Princípio central:
Diagnosticar antes de orientar.

Regras:
- Faça perguntas quando faltarem informações.
- Use a base de conhecimento fornecida como referência.
- Não invente procedimentos.
- Diferencie hipóteses de diagnósticos.
- Priorize procedimentos simples, seguros e reversíveis.
- Nunca solicite senhas ou códigos de autenticação.
- Reconheça limitações e encaminhe casos avançados.
- Explique os procedimentos de maneira clara e passo a passo.
- Evite jargões desnecessários.
"""


def carregar_base():
    with open(BASE_PATH, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def buscar_conhecimento(pergunta, base):
    pergunta = pergunta.lower()
    resultados = []

    for item in base:
        texto = " ".join(
            [
                item.get("categoria", ""),
                item.get("problema", ""),
                " ".join(item.get("sintomas", [])),
            ]
        ).lower()

        palavras = [
            palavra
            for palavra in pergunta.split()
            if len(palavra) > 3
        ]

        if any(palavra in texto for palavra in palavras):
            resultados.append(item)

    return resultados[:3]


def gerar_resposta(pergunta, historico):
    base = carregar_base()
    conhecimento = buscar_conhecimento(pergunta, base)

    contexto = json.dumps(
        conhecimento,
        ensure_ascii=False,
        indent=2,
    )

    prompt = f"""
{SYSTEM_PROMPT}

BASE DE CONHECIMENTO:

{contexto}

HISTÓRICO DA CONVERSA:

{json.dumps(historico, ensure_ascii=False, indent=2)}

SOLICITAÇÃO DO USUÁRIO:

{pergunta}

Responda ao usuário seguindo as regras do NEXA TechHelp.
"""

    modelos = [
        "gemini-3.6-flash",
        "gemini-3.5-flash",
        "gemini-3.1-flash-lite",
    ]

    ultimo_erro = None

    for modelo in modelos:
        try:
            resposta = client.models.generate_content(
                model=modelo,
                contents=prompt,
            )

            if resposta.text:
                return resposta.text

        except Exception as erro:
            ultimo_erro = erro
            continue

    raise RuntimeError(
        f"Não foi possível obter resposta de nenhum modelo Gemini: {ultimo_erro}"
    )