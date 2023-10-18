import plotly.express as px
import pandas as pd
import streamlit as st

# Ative o "wide mode" por padrão
st.set_page_config(layout="wide")

def montarDash(st, df: pd.DataFrame):
    st.sidebar.title("Navegação")
    page = st.sidebar.selectbox("Selecione uma página", ["Inicio", "Gráfico 1", "Gráfico 2"])

    if page == "Inicio":
        st.title("Análise de Dados Oral Care")

        # Tabela com os dados
        st.write("Aqui você pode visualizar e analisar os dados da pesquisa Oral Care. Tabela de Dados:")
        st.write(df)

    elif page == "Gráfico 1":
        st.title("Cidades que conhecem o Oral Care por Gênero")
        
        # Primeiro gráfico - Cidades que conhecem o oral care por gênero
        fig1 = px.bar(df,
                     x='cidade',
                     y='idade',
                     color='genero',
                     title='Cidades que Conhecem o Oral Care por Gênero',
                     text='idade')
        
        # Crie duas colunas, uma para o gráfico e outra para a explicação
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.plotly_chart(fig1)
        
        with col2:
            st.text("")  # Adicione um espaço em branco para centralizar o texto
            st.write("Aqui está a explicação do Gráfico 1.")

    elif page == "Gráfico 2":
        st.title("Exemplo de Segundo Gráfico")
        
        # Segundo gráfico - Outra análise (exemplo)
        fig2 = px.scatter(df,
                          x='idade',
                          y='frequencia_escova_dentes_diaria',
                          color='genero',
                          title='Exemplo de Segundo Gráfico')
        
        # Crie duas colunas, uma para o gráfico e outra para a explicação
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.text(".")  # Adicione um espaço em branco para centralizar o texto
            st.text(".")
            st.text(".")
            st.text(".")
            st.text(".")
            st.write("Aqui está a explicação do Gráfico 2.   lk r")
    
        with col2:
            st.plotly_chart(fig2)

if __name__ == '__main__':
    montarDash(st, df)
