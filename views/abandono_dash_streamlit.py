import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo Excel
df = pd.read_excel(r"C:\Users\daleb\Downloads\abandono_con_scoring (1).xlsx")

# Convertir columnas relevantes a tipo numérico si es necesario
df["scoring_abandono"] = pd.to_numeric(df["scoring_abandono"], errors="coerce")
df["Salario"] = pd.to_numeric(df["impacto_abandono"], errors="coerce")

# Verificar si hay valores nulos en la columna 'departamento' y llenarlos o eliminarlos
df["departamento"].fillna("Desconocido", inplace=True)

# Crear el dashboard en Streamlit
st.title("Dashboard de Riesgo de Abandono")

# Segmentador de Departamento
departamentos = df["departamento"].unique()
departamento_seleccionado = st.multiselect(
    "Selecciona el Departamento",
    options=departamentos,
    default=departamentos,  # Por defecto, seleccionamos todos
)

# Filtramos los datos por los departamentos seleccionados
df_filtrado = df[df["departamento"].isin(departamento_seleccionado)]


# KPIs con datos filtrados
tasa_abandono = df_filtrado["scoring_abandono"].mean()
empleados_en_riesgo = df_filtrado[df_filtrado["scoring_abandono"] > 0.5].shape[0]
quetzales_en_riesgo = df_filtrado[df_filtrado["scoring_abandono"] > 0.5][
    "impacto_abandono"
].sum()


# Mostrar KPIs como tarjetas
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Tasa de Abandono", f"{tasa_abandono:.2%}")
with col2:
    st.metric("Empleados en Riesgo", empleados_en_riesgo)
with col3:
    st.metric("Quetzales en Riesgo", f"Q{quetzales_en_riesgo:,.2f}")


# Tabla con empleados en riesgo filtrados
st.subheader("Empleados en Riesgo")
empleados_riesgo_df = df_filtrado[df_filtrado["scoring_abandono"] > 0.5][
    ["id", "departamento", "scoring_abandono", "impacto_abandono"]
]  # Puedes ajustar las columnas que deseas mostrar
st.dataframe(empleados_riesgo_df)

# Gráfica de Caja y Bigotes (Boxplot) por Departamento con colores
st.subheader("Distribución de Riesgo por Puesto")
plt.figure(figsize=(12, 8))
sns.boxplot(x="puesto", y="scoring_abandono", data=df_filtrado)
plt.xticks(rotation=45)
plt.title("Distribución del Scoring de Abandono por Puesto")
st.pyplot(plt)

# Conclusiones basadas en los datos
st.write(
    """
1. **Tasa de Abandono Relativamente Alta**: La tasa promedio de abandono de los empleados es significativa, con un promedio del {:.2%}. Esto indica un riesgo importante que debe ser abordado.
   
2. **Empleados en Riesgo**: {} empleados están clasificados como en riesgo de abandono, lo que representa una porción considerable de la fuerza laboral en los departamentos seleccionados. Las empresas deben considerar un plan de retención para estos empleados.

3. **Impacto Financiero Potencial**: El valor total en riesgo debido a empleados en posible abandono asciende a Q{:.2f}, lo que podría resultar en un alto costo de reemplazo y pérdida de conocimiento corporativo si no se toman medidas inmediatas.

4. **Distribución por Departamento**: Algunos departamentos muestran una mayor concentración de riesgo en comparación con otros. La gráfica de caja y bigotes muestra que ciertos departamentos tienen empleados con puntajes de abandono consistentemente altos.
""".format(tasa_abandono, empleados_en_riesgo, quetzales_en_riesgo)
)

# Comentarios o recomendaciones adicionales
st.subheader("Recomendaciones")
st.write("""
1. **Monitorear de cerca a los empleados en departamentos con mayor riesgo de abandono.**
2. **Tomar medidas preventivas, como mejorar las condiciones laborales, para reducir la tasa de abandono.**
3. **Aumentar los incentivos o las oportunidades de crecimiento para los empleados en riesgo.**
""")
