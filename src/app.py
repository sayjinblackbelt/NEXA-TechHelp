import streamlit as st

from agente import gerar_resposta

st.set_page_config(
    page_title="NEXA TechHelp",
    page_icon="🛠️",
    layout="centered"
)

st.title("🛠️ NEXA TechHelp")
st.caption("Assistente inteligente de suporte à informática")

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])

pergunta = st.chat_input("Descreva seu problema de informática...")

if pergunta:
    st.session_state.mensagens.append({
        "role": "user",
        "content": pergunta
    })

    with st.chat_message("user"):
        st.markdown(pergunta)

    with st.chat_message("assistant"):
        try:
            resposta = gerar_resposta(
                pergunta,
                st.session_state.mensagens[:-1]
            )
            st.markdown(resposta)

            st.session_state.mensagens.append({
                "role": "assistant",
                "content": resposta
            })
        except Exception:
            resposta = (
                "Não foi possível processar sua solicitação. "
                "Verifique a configuração da aplicação."
            )
            st.error(resposta)
