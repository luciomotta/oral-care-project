import pandas as pd
import streamlit as st
import plotly.express as px
from dashboard import montarDash
from Modules.dados import pegar_dados

# Para executar:
# streamlit run main.py
#Recarregamento autmatico== streamlit run --server.runOnSave main.py

df = pegar_dados()

montarDash(st, df)
