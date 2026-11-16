import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

st.set_page_config(page_title="AI Study & Work Assistant", page_icon="🤖", layout="centered")
st.title("🤖 AI Study & Work Assistant")
st.caption("Assistente conversacional com histórico de sessão e instruções personalizadas.")

api_key = os.getenv("OPENAI_API_KEY", "").strip()
model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
system_prompt = """Você é um assistente útil, claro e responsável.
Responda em português brasileiro por padrão.
Explique conceitos passo a passo quando o usuário estiver aprendendo.
Não invente fatos, fontes ou resultados. Quando não souber, diga isso.
Adapte o nível de detalhe ao pedido do usuário."""

with st.sidebar:
    st.header("Configurações")
    st.write(f"Modelo configurado: `{model}`")
    st.info("Para habilitar respostas com IA, configure OPENAI_API_KEY no arquivo .env.")
    if st.button("Limpar conversa"):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Digite sua pergunta...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        if not api_key:
            answer = (
                "O aplicativo está funcionando em modo de demonstração, mas ainda não há uma "
                "chave de API configurada. Crie um arquivo `.env` a partir de `.env.example`, "
                "adicione sua chave e reinicie o Streamlit para habilitar a IA."
            )
            st.info(answer)
        else:
            try:
                client = OpenAI(api_key=api_key)
                response = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "system", "content": system_prompt}]
                    + st.session_state.messages,
                    temperature=0.4,
                )
                answer = response.choices[0].message.content or "Não consegui gerar uma resposta."
                st.markdown(answer)
            except Exception as exc:
                answer = "Não foi possível consultar o serviço de IA. Verifique a chave, o modelo e sua conexão."
                st.error(answer)
                st.caption(f"Detalhe técnico: {type(exc).__name__}")
    st.session_state.messages.append({"role": "assistant", "content": answer})
