import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time
import plotly.express as px

st.set_page_config(page_title='Divergencia Geometrica')

"""
# :symbols: Divergencia geometrica simple  :chart_with_upwards_trend: :chart_with_downwards_trend:
Datos de entrada
- Lw
- Distancia

El cálculo se realiza bajo el supuesto que es una fuente omnidireccional en un espacio libre.
"""
st.latex(r'''NPS = Lw - 8 - 20*log_{10}(d)''')

lw = st.number_input(
    'Nivel de potencia sonora (Lw), en decibeles',
    min_value=1,
    max_value=140,
    value = 100
)

distancia_usuario = st.number_input(
    'Distancia a proyectar, en metros',
    min_value=1,
    value = 50
)


# --------------------------------
# Calculo
# --------------------------------

df = pd.DataFrame()

distancia = distancia_usuario*1.05  # Distancia para graficar
puntos = 200
inicio = 1
pasos = (distancia - inicio) / puntos  # Pasos para calculo de distancia
la_distancia = inicio

for i in range(puntos):
    el_nivel = round(lw - 8 - 20*np.log10(la_distancia),1)
    df = df.append({
        'distancia': la_distancia,
        'nps': el_nivel
    }, ignore_index=True)
    la_distancia = la_distancia + pasos

nivel_usuario = round(lw - 8 - 20*np.log10(distancia_usuario),1)

df = df.append({
        'distancia': distancia_usuario,
        'nps': nivel_usuario
    }, ignore_index=True)

# Ordenamos
df2 = df.sort_values(by=['distancia'])

"""
### Resultado:
"""
#df[-1:]

# --------------------------------
# Despligue de información
# --------------------------------

import plotly.graph_objects as go

fig = go.Figure(
    data=go.Line(
        x=df2["distancia"],
        y=df2["nps"]
    )
)
fig.show()

fig.add_vrect(
    x0=distancia_usuario*0.99,
    x1=distancia_usuario*1.01,
    fillcolor="green",
    opacity=0.5,
    layer="below",
    line_width=0
)

st.plotly_chart(fig)

# --------------------------------
# Informacion adicionalr
# --------------------------------
expander = st.beta_expander("Referencia")
expander.write("Parametro Adiv del estandar [ISO 9613-2](https://www.iso.org/standard/20649.html).")
expander.write("De manera simplificada, se puede expresar de acuerdo a la siguiente ecuacion.")
expander.latex(r'''NPS = Lw - 8 - 20*log_{10}(d)''')