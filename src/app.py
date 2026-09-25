import streamlit as st

from src.agente import gerar_resposta


# Configuração da página
st.set_page_config(
    page_title="NEXA TechHelp",
    page_icon="🛠️",
    layout="centered"
)


# Cabeçalho
st.title("🛠️ NEXA TechHelp")
st.caption("Assistente inteligente de suporte à informática")


# Inicializa o histórico da conversa
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []


# Exibe o histórico
for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])


# Campo para nova pergunta
pergunta = st.chat_input(
    "Descreva seu problema de informática..."
)


# Processa a pergunta
if pergunta:

    # Salva a pergunta do usuário
    st.session_state.mensagens.append({
        "role": "user",
        "content": pergunta
    })

    # Exibe a pergunta
    with st.chat_message("user"):
        st.markdown(pergunta)

    # Gera a resposta
    with st.chat_message("assistant"):

        try:
            resposta = gerar_resposta(
                pergunta,
                st.session_state.mensagens[:-1]
            )

            st.markdown(resposta)

            # Salva a resposta no histórico
            st.session_state.mensagens.append({
                "role": "assistant",
                "content": resposta
            })

        except Exception as e:

            # Exibe o erro técnico para diagnóstico
            st.error(
                "O NEXA encontrou um erro ao processar sua solicitação."
            )

            st.exception(e)