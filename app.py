from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTING ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV_AB.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"



# --- GENERAL SETTIGNS ---
PAGE_TITLE = "Digital CV | Alessandra Balconi"
PAGE_ICON = ":🌷:"
NAME = "Alessandra Balconi"
DESCRIPTION = """
Analista de Datos con un talento para transformar datos en historias claras y útiles, listo para impulsar decisiones estratégicas con un toque de creatividad y precisión.
"""
EMAIL = "dalebv87@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "Nan", 
    "LinkedIn": "https://www.linkedin.com/in/alessandra-balconi-5515a7182/",
    "GitHub": "Nan",
    "Twitter": "Nan"
}
PROJECTS = {
    "Sales Dashboard": "Nan",
    "Income and Expense Tracker": "Nan"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# ---LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- REDES SOCIALES ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- Experiencia y Calificaciones ---
st.write('\n')
st.subheader("Experiencia y Calificaciones")
st.write(
    """
- ✔️ Estudiante de Economía en la Universidad Rafael Landívar (8vo Semestre)
- ✔️ Conocimientos de Python y Excel para Machine Learning
- ✔️ Amplia comprensión de conceptos estadísticos y su implementación en diversos contextos
- ✔️ Proactiva ejecución de tareas, asegurando el cumplimiento eficiente de los objetivos del equipo.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Habilidades")
st.write(
    """
- 👩‍💻 Programación: Python (Scikit-learn, Pandas, Numpy)
- 📊 Visualización: PowerBi, MS Excel, Plotly, Seaborn
- 📚 Modelos: Segmentación, Clasificación, Redes Neuronales
- 🗄️ Bases de Datos: Postgres
"""
)


# --- EXPERIENCIA LABORAL ---
st.write('\n')
st.subheader("Experiencia Laboral")
st.write("---")

# --- TRABAJO 1
st.write("🚧", "**Analista de Control de Calidad | Intouch CX**")
st.write("03/2021 - Presente")
st.write(
    """
- ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)

# --- TRABAJO 2
st.write('\n')
st.write("🚧", "**Diseñadora de cursos E-Learing |  Strategia Virtual**")
st.write("01/2018 - 02/2021")
st.write(
    """
- ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
- ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
- ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
"""
)


# --- Cursos y Certificaciones ---
# --- Listado de Cursos ---
st.subheader("Cursos Realizados")

cursos = [
    {
        "nombre": "Curso de Fotografía",
        "institución": "Libera Accademia di Belle Arti, Italia",
        "año": 2009
    },
    {
        "nombre": "Certificación Programador Python, Django e Inteligencia Artificial",
        "institución": "Inove Coding School",
        "año": 2023,
        "certificación": "https://inovecode.com/"
    }
]

# --- Mostrar Cursos ---
for curso in cursos:
    st.write(f"**{curso['nombre']}**")
    st.write(f"{curso['institución']} ({curso['año']})")
    if 'certificación' in curso:
        st.write(f"[Ver Certificación]({curso['certificación']})")
    st.write("---")

        

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projectos & Logros")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")






