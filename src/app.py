import streamlit as st
from rag import cargar_documentos, crear_vectorstore, crear_cadena_rag

st.set_page_config(
    page_title="Chatbot TechStore",
    page_icon="🤖"
)

st.title("🤖 Chatbot TechStore")
st.caption("Pregúntame sobre productos, precios y políticas de la tienda.")

@st.cache_resource
def inicializar_chatbot():
    documentos = cargar_documentos("../docs")
    vectorstore = crear_vectorstore(documentos)
    cadena = crear_cadena_rag(vectorstore)
    return cadena

cadena = inicializar_chatbot()

if "mensajes" not in st.session_state:
    st.session_state.mensajes = [
        {"role": "assistant", "content": "¡Hola! Soy el asistente de TechStore. ¿En qué puedo ayudarte?"}
    ]

for mensaje in st.session_state.mensajes:
    with st.chat_message(mensaje["role"]):
        st.write(mensaje["content"])

if pregunta := st.chat_input("Escribe tu pregunta..."):
    st.session_state.mensajes.append({"role": "user", "content": pregunta})
    with st.chat_message("user"):
        st.write(pregunta)

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            respuesta = cadena.invoke(pregunta)
            st.write(respuesta)

    st.session_state.mensajes.append({"role": "assistant", "content": respuesta})