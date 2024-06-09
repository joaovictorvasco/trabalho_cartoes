import streamlit as st
import pandas as pd
from xgboost import XGBRegressor
import numpy as np

# Criando a barra superior
st.write("""
    <div style="background-color:#f63366;padding:10px;border-radius:200px;">
        <h1 style="color:white;text-align:center;">Fortune Card</h1>
    </div>
""", unsafe_allow_html=True)

# Conteúdo principal
st.write("""
    # Nosso app serve para prever estatisticamente o número de cartões numa determinada partida
""")

# Criando abas
tab1, tab2 = st.tabs(["Jogos", "Tabela"])

# Conteúdo para a aba "Jogos"
with tab1:
    times = ['Ath Paranaense', 'Atl Goianiense', 'Atlético Mineiro', 'Bahia', 'Botafogo (RJ)', 
             'Corinthians', 'Criciúma', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense', 
             'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Palmeiras', 
             'Red Bull Bragantino', 'São Paulo', 'Vasco da Gama', 'Vitória']
    
    # Ordenando a lista de times
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
            st.metric('Nº de cartões predito', resultado)

# Conteúdo para a aba "Tabela"
with tab2:
    st.write("Conteúdo da Tabela aqui.")

