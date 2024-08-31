import random
import time

import streamlit as st


# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hola! ¿Buscas talento? Echa un vistazo a mi CV: está lleno de habilidades y experiencia.",
            "¡Hey! ¿Necesitas una Analista de Datos? Mi CV te mostrará todo lo que puedo aportar.",
            "¡Hola! Mi CV está listo para impresionar, ¡échale un vistazo!",
            "¡Hola! Si buscas precisión y creatividad, mi CV es lo que necesitas ver.",
            "¡Hey! ¿Buscas a alguien que transforme datos en decisiones? Mira mi CV.",
            "¡Hola! Mi CV está lleno de proyectos interesantes y experiencia en análisis de datos.",
            "¡Hola! Si necesitas un ojo analítico en tu equipo, no te pierdas mi CV.",
            "¡Hola! Mi CV está lleno de habilidades que podrían ser justo lo que tu equipo necesita.",
            "¡Hola! ¿Listo para conocer a tu próximo Analista de Datos? ¡Mira mi CV!",
            "¡Hola! Mi CV es el primer paso para llevar tus decisiones estratégicas al siguiente nivel.",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})