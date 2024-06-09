import streamlit as st
import pandas as pd
from xgboost import XGBRegressor
import numpy as np
import os

sidebar_logo = "fortune.png"
main_logo = "logo_horizontal.jpg"
background_color = "#0a1931"

# Sidebar logo display
st.sidebar.image(sidebar_logo, width=250)

# Main logo display, centered
st.image(main_logo, width=700, use_column_width=True)

# Creating a colored top bar
st.markdown(f"""
    <div style="background-color:{background_color}; padding:15px; border-radius:10px; box-shadow: 0 16px 8px 0 rgba(0, 0, 0, 0.2);">
        <h1 style="color:yellow; font-size:50px; text-align:center;">Fortune Card</h1>
    </div>
""", unsafe_allow_html=True)

# Main content
st.markdown("""
    <h2 style="font-size:24px;">Nosso app serve para prever estatisticamente o número de cartões numa determinada partida</h2>
""", unsafe_allow_html=True)


# Tabs for content
tab1, tab2 = st.tabs(["Jogos", "Tabela"])

# Tab content
with tab1:
    times = ['Ath Paranaense', 'Atl Goianiense', 'Atlético Mineiro', 'Bahia', 'Botafogo (RJ)', 
             'Corinthians', 'Criciúma', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense', 
             'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Palmeiras', 
             'Red Bull Bragantino', 'São Paulo', 'Vasco da Gama', 'Vitória']
    times_ordenados = sorted(times)
    
    with st.form(key='form'):
        op_home = st.selectbox('Escolha uma opção p/ time da casa', times_ordenados)
        op_away = st.selectbox('Escolha outra opção p/ time visitante', times_ordenados)
        enviar = st.form_submit_button('Enviar')
    
    if enviar:
        if op_home == op_away:
            st.error('Erro: O mesmo time não pode ser escolhido como time da casa e visitante.')
        else:
            lista = [{'Home': op_home, 'Away': op_away, 'ano_x': 2024}]
            df = pd.DataFrame(lista)
            df['Home'] = df['Home'].astype('category')
            df['Away'] = df['Away'].astype('category')
            model = XGBRegressor()
            model.load_model('modelo.json') 
            resultado = model.predict(df)
            st.metric('Nº de cartões predito', int(np.round(resultado[0], 0)))

with tab2:
    st.write("Conteúdo da Tabela aqui.")


