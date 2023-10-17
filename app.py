import pandas as pd
import streamlit as st
import plotly.express as px
from dashboard import montarDash
from Modules.dados import pegar_dados

# Função para alternar entre os temas claro e escuro
def toggle_theme():
    theme = st.selectbox("Escolha o tema:", ["Claro", "Escuro"])
    if theme == "Claro":
        st.write("Ativando o Modo Claro")
        st.set_page_config(
            page_title="Análise de Dados Oral Care",
            page_icon="✅",
            layout="centered",
            initial_sidebar_state="expanded",
            theme="light",
        )
    else:
        st.write("Ativando o Modo Escuro")
        st.set_page_config(
            page_title="Análise de Dados Oral Care",
            page_icon="✅",
            layout="wide",
            initial_sidebar_state="expanded",
            theme="dark",
        )

df = pegar_dados()

st.title("Análise de Dados Oral Care")
st.write("Aqui você pode visualizar e analisar os dados da pesquisa Oral Care.")
df

# Adicione o seletor de tema
toggle_theme()

montarDash(st, df)
