# Para multipage
import streamlit as st
def app():
    st.title(':symbols: Divergencia geométrica simple')
    # To make things easier later, we're also importing numpy and pandas for
    # working with sample data.
    import numpy as np
    import pandas as pd
    import time
    import plotly.express as px

    st.set_page_config(page_title='Divergencia geométrica simple')

    st.write("""
        Datos de entrada
        - Lw
        - Distancia
    
        El cálculo se realiza bajo el supuesto que es una fuente omnidireccional en un espacio libre.
        """)
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

    nivel_usuario = round(lw - 8 - 20*np.log10(distancia_usuario),5)

    df = df.append({
            'distancia': distancia_usuario,
            'nps': nivel_usuario
        }, ignore_index=True)

    # Ordenamos
    df2 = df.sort_values(by=['distancia'])

    """
    ### Resultado:
    """
    'Considerando una potencia sonora Lw = ', lw, ', el nivel calculado a una distancia de ',  distancia_usuario, ' metros es de ', round(nivel_usuario,1), ' dB'

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

    st.plotly_chart(fig, use_container_width=True)

    # --------------------------------
    # Informacion adicionalr
    # --------------------------------
    expander = st.beta_expander("Referencia")
    expander.write("Parámetro Adiv del estándar [ISO 9613-2](https://www.iso.org/standard/20649.html).")
    expander.write("De manera simplificada, se puede expresar de acuerdo a la siguiente ecuación.")
    expander.latex(r'''NPS = Lw - 8 - 20*log_{10}(d)''')