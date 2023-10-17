import plotly.express as px
import pandas as pd

def montarDash(st, df:pd.DataFrame):
    fig = px.bar(df, 
             x='cidade', 
             y='idade', 
             orientation='v',
             title='pesquisa < Cidades')
    st.plotly_chart(fig)

