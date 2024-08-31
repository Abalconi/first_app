import streamlit as st
from pathlib import Path
from PIL import Image



# --- GENERAL SETTIGNS ---
# PAGE_TITLE = "Digital CV | Alessandra Balconi"
#PAGE_ICON = "🌷"
#NAME = "Alessandra Balconi"
#DESCRIPTION = """
# Analista de Datos con un talento para transformar datos en historias claras y útiles, listo para impulsar decisiones estratégicas con un toque de creatividad y precisión.
# """
#EMAIL = "dalebv87@gmail.com"
#SOCIAL_MEDIA = { 
#    "LinkedIn": "https://www.linkedin.com/in/alessandra-balconi-5515a7182/", 
#    "GitHub": "https://github.com/Abalconi",
#} 

#st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON) 

# ---LOAD CSS, PDF & PROFILE PIC ---
# with open(css_file) as f:
#    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
# with open(resume_file, "rb") as pdf_file:
#    PDFbyte = pdf_file.read()
# profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
#col1, col2 = st.columns(2, gap="small")"
#with col1:
#   st.image(profile_pic, width=260)

#with col2:
#    st.title(NAME)
#    st.write(DESCRIPTION)
#    st.download_button(
#        label=" 📄 Descargar CV",
#        data=PDFbyte,
#        file_name=resume_file.name,
#        mime="application/octet-stream",
#    )
#    st.write("📫", EMAIL)


SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/feed/",
    "GitHub": "https://github.com/Abalconi",
    }


# Definir el directorio actual (current directory)
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

# Ruta al archivo PDF del CV
css_file = "./styles/main.css"  
resume_file = Path("assets/CV_AB.pdf")

# Definir las rutas a los certificados
cert_ia_url = "https://raw.githubusercontent.com/Abalconi/first_app/main/assets/cert_ia.pdf"
cert_django_url = "https://raw.githubusercontent.com/Abalconi/first_app/main/assets/cert_django.pdf"
cert_programador_url = "https://raw.githubusercontent.com/Abalconi/first_app/main/assets/cert_programador.pdf"
cert_python_inicial_url = "https://raw.githubusercontent.com/Abalconi/first_app/main/assets/cert_python_inicial.pdf"

# Cargar el archivo PDF
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# Cargar el archivo CSS
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/profile_pic1.png", width=240)
    

with col2:
    st.title("Alessandra Balconi", anchor=False)
    st.write(
        "Analista de Datos con un talento para transformar datos en historias claras y útiles, listo para impulsar decisiones estratégicas con un toque de creatividad y precisión."
    )
    st.download_button(
        label=" 📄 Descargar CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", "dalebv87@gmail.com")


    #  --- REDES SOCIALES ---
    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")

    

# --- Experiencia y Calificaciones ---
st.write('\n')
st.subheader("Experiencia y Calificaciones")
st.write(



    """
- ► Estudiante de Economía en la Universidad Rafael Landívar (8vo Semestre)
- ► Conocimientos de Python y Excel para Machine Learning
- ► Amplia comprensión de conceptos estadísticos y su implementación en diversos contextos
- ► Proactiva ejecución de tareas, asegurando el cumplimiento eficiente de los objetivos del equipo.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Habilidades")
st.write(
    """
- 👩‍💻 Programación: Python (Scikit-learn, Pandas, Numpy)
- 📊 Visualización: PowerBi, MS Excel, Matplotlib, Seaborn, Plotly
- 📚 Modelos: Regresión, Segmentación, Clasificación, Redes Neuronales
- 🗄️ Bases de Datos: Postgres
"""
)


# --- EXPERIENCIA LABORAL ---
st.write('\n')
st.subheader("Experiencia Laboral")
st.write("---")

# --- TRABAJO 1
st.write("📈", "**Analista de Control de Calidad | Intouch CX**")
st.write("03/2021 - Presente")
st.write(
    """
- ► Monitoreo y evaluación de llamadas para asegurar el cumplimiento de los estándares de calidad en el departamento de ventas.
- ► Implementación de mejoras continuas en los procesos de ventas a través del análisis de datos y feedback.
- ► Colaboración con equipos de ventas para identificar áreas de oportunidad y desarrollar estrategias de capacitación.
"""
)

# --- TRABAJO 2
st.write('\n')
st.write("📊", "**Diseñadora de cursos E-Learing |  Strategia Virtual**")
st.write("01/2018 - 02/2021")
st.write(
    """
- ► Desarrollo de cursos de capacitación personalizados para empleados, directores y ejecutivos del sector público y privado.
- ► Creación de contenidos interactivos y visuales para mejorar la experiencia de aprendizaje.
- ► Provisión de soporte a empresas como Ingenio Pantaleón y SAT, asegurando la efectividad de los programas de formación.
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
        "nombre": "Excel y Power BI. Academia A2",
        "institución": "Academia A2, México",
        "año": 2020
    },
    {
        "nombre": "Certificación Python Analytics",
        "institución": "Inove Coding School",
        "año": 2024,
        "certificación": cert_ia_url # URL del archivo PDF
    },
    {
        "nombre": "Certificación Programador Django",
        "institución": "Inove Coding School",
        "año": 2023,
        "certificación": cert_django_url  # URL del archivo PDF
    },
    {
        "nombre": "Certificación Programador Python",
        "institución": "Inove Coding School",
        "año": 2023,
        "certificación": cert_programador_url  # URL del archivo PDF
    },
    {
        "nombre": "Certificación Python Inicial",
        "institución": "Inove Coding School",
        "año": 2023,
        "certificación": cert_python_inicial_url  # URL del archivo PDF
    }
]

# --- MOSTRAR CURSOS ---
for curso in cursos:
    st.write(f"**{curso['nombre']}**")
    st.write(f"{curso['institución']} ({curso['año']})")
    if 'certificación' in curso:
        st.markdown(f'<a href="{curso["certificación"]}" target="_blank" rel="noopener noreferrer">Ver Certificación</a>', unsafe_allow_html=True)
    st.write("---")