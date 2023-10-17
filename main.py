import pandas as pd
import streamlit as st
import plotly.express as px
from dashboard import montarDash
from Modules.dados import pegar_dados

# Para exeutar:
# streamlit run main.py
texto = "testando SSL"

df = pegar_dados()

st.write("# Análise de Dados Oral Care")
st.write("Aqui você pode visualizar e analisar os dados da pesquisa Oral Care.")
texto
df

montarDash(st, df)
