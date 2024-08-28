import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    "views/about_me.py",
    title="Sobre Mí",
    icon="🌻",
    default=True,
)

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/feed/",
    "GitHub": "https://github.com/Abalconi",
    }

# --- SOCIAL LINKS ---
st.sidebar.write("### Sígueme en")
for platform, link in SOCIAL_MEDIA.items():
    #emoji = {
    #   "LinkedIn": "🔗",
    #    "GitHub": "🐙"
    #}.get(platform, "🔗")  # Usa un emoji por defecto si la plataforma no está en el diccionario
    st.sidebar.markdown(f"[{platform}]({link})")

project_1_page = st.Page(
    "views/sales_dashboard.py",
    title="Dashboard de Ventas",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    "views/chatbot.py",
    title="ChatBot",
    icon=":material/smart_toy:",
)



# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page],
    }
)



# --- SHARED ON ALL PAGES ---
st.logo("assets/tekylab_logo.jpg")
st.sidebar.markdown("App desarrollada en Python.")

# --- RUN NAVIGATION ---
pg.run()


