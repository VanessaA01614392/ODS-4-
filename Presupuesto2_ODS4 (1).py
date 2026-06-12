# Importar librerías necesarias
import numpy as np
import streamlit as st
import pandas as pd
# Insertamos título
st.write(''' # ODS 4: Educación de calidad ''')
# Insertamos texto con formato
st.markdown("""Optimización de Recursos para el Fortalecimiento Educativo.""")
# Insertamos una imagen
st.image("ODS 4.webp", caption="Impacto de diversos factores sobre la tasa de graduación.")
# Usaremos un deslizador
st.sidebar.header("Presupuesto")
# Definimos los parámetros de nuestro deslizador:
# Límite inferior: 20000000000
# Límite superior: 64000000000
# Valor inicial: 40000000000
presupuesto = st.sidebar.slider("Presupuesto", 10000000, 45000000, 20000000)
st.sidebar.header("Porcentaje de Becas")
porcentaje_becas = st.sidebar.slider("Porcentaje de Becas", 0.2, 1.0, 0.5)
st.sidebar.header("Porcentaje de Infraestructura")
porcentaje_infra = st.sidebar.slider("Porcentaje de Infraestructura", 0.0, 0.5, 0.25)
st.sidebar.header("Porcentaje de Docentes")
porcentaje_docentes = st.sidebar.slider("Porcentaje de Docentes", 0.15, 1.0, 0.35)
# Cargamos el archivo con los datos (.csv)
datos = pd.read_csv('India_ODS4 (1).csv', encoding='latin-1')
# Seleccionamos las variables
X = pd.DataFrame(datos, columns=['Upper secondary_x'])
y = datos['Upper secondary_y']
# Creamos y entrenamos el modelo
from sklearn.linear_model import LinearRegression
LR = LinearRegression()
LR.fit(X,y)
# Extraemos los coeficientes de la regresión
b1 = LR.coef_
b0 = LR.intercept_
# Especificamos datos por población
numero = 28000000
prep_alumno = presupuesto/numero
# Calculamos el presupuesto asignado a cada rubro
presupuesto_becas = presupuesto * porcentaje_becas
presupuesto_infra = presupuesto * porcentaje_infra
presupuesto_docentes = presupuesto * porcentaje_docentes
# Presentamos loa resultados
total_gastado = presupuesto*(porcentaje_becas + porcentaje_infra +porcentaje_docentes)
# Validar restricciones
st.subheader('Impacto alcanzado')
impacto = b0 + prep_alumno*b1[0] + presupuesto_infra/100000000*0.15 +presupuesto_docentes/100000000*.14
st.metric("Impacto Proyectado ODS 4", f"+{float(impacto):.3f}%")
# Presentamos el tipo de filosofía
if porcentaje_becas >= 0.40:
  filosofia = "Bienestar Primero (Equidad y Movilidad Social)"
elif porcentaje_infra >= 0.45:
  filosofia = "Rendimiento Estructural (Desarrollo Sostenible)"
elif porcentaje_docentes >= 0.35:
  filosofia = "Efecto Multiplicador (Excelencia Académica)"
else:
  filosofia = "Gobernanza Equilibrada (Modelo Balanceado)"
st.subheader("Clasificación Estratégica del Modelo")
st.info(f"Su propuesta óptima califica como un enfoque de: **{filosofia}**")
