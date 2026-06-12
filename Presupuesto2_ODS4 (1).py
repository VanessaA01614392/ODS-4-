# Importar librerías necearias
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
presupuesto = st.sidebar.slider("Presupuesto", 700, 2000, 1500)

# Cargamos el archivo con los datos (.csv)
  datos = pd.read_csv('India_ODS4.csv', encoding='latin-1')
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

impacto = b0 + prep_alumno*b1[0]
st.metric("Impacto Proyectado ODS 4", f"+{float(impacto):.3f}%")
