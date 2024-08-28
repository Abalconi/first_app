import re

import streamlit as st
import requests  # pip install requests


WEBHOOK_URL = st.secrets["WEBHOOK_URL"]


def is_valid_email(email):
    # Basic regex pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None


def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Nombre")
        email = st.text_input("Email")
        message = st.text_area("Mensaje")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        if not WEBHOOK_URL:
            st.error("El servicio de correo no esta funcionando. Por favor intenta de nuevo más tarde.", icon="📧")
            st.stop()

        if not name:
            st.error("Por favor ingresa tu nombre.", icon="🧑")
            st.stop()

        if not email:
            st.error("Por favor ingresa tu correo electrónico.", icon="📨")
            st.stop()

        if not is_valid_email(email):
            st.error("Por favor ingresa un correo electrónico válido.", icon="📧")
            st.stop()

        if not message:
            st.error("Por favor escribe un mensaje.", icon="💬")
            st.stop()

        # Prepare the data payload and send it to the specified webhook URL
        data = {"email": email, "name": name, "message": message}
        response = requests.post(WEBHOOK_URL, json=data)

        if response.status_code == 200:
            st.success("¡Tu mensaje se ha envíado exitosamente! 🎉", icon="🚀")
        else:
            st.error("Error al enviar el mensaje.", icon="😨")