import pandas as pd
import streamlit as st
import plotly.express as px
from dashboard import montarDash
from Modules.dados import pegar_dados

# Para executar:
# streamlit run main.py
#Recarregamento autmatico== streamlit run --server.runOnSave main.py

df = pegar_dados()

st.title("Análise de Dados Oral Care")
st.write("Aqui você pode visualizar e analisar os dados da pesquisa Oral Care.")
df

montarDash(st, df)
