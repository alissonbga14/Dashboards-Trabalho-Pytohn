import streamlit as st
from datetime import datetime, timedelta
import plotly.graph_objs as go
import pandas as pd

st.set_page_config(
    page_title="Análise dos Preços de Combustíveis",
    layout="wide",
    initial_sidebar_state="expanded",
)

df = pd.read_csv(r'GasPricesinBrazil_2004-2019.csv', sep=';', index_col=0)


regiao = pd.DataFrame(df['REGIÃO'].drop_duplicates())
intervalo = ['DIÁRIO', 'SEMANAL', 'MENSAL']

data_inicial = datetime.today()-timedelta(days=30)
data_final = datetime.today()



# CRIANDO UMA BARRA LATERAL
barra_lateral = st.sidebar.empty()
regiao_selecionada = str(st.sidebar.selectbox("Selecione a região:", regiao))
produto = pd.DataFrame(df[(df['REGIÃO'] == regiao_selecionada)].groupby('PRODUTO'))

produto_selecionado = str(st.sidebar.selectbox("Selecione o Produto:", produto))



grafico_line = st.empty()
grafico_candle = st.empty()

# elementos centrais da página
st.title('Análise dos Preços de Combustíveis')

df_filtrado = pd.DataFrame(df.loc[(df['REGIÃO'] == regiao_selecionada) & (df['PRODUTO'] == produto_selecionado)])



linha = df_filtrado.groupby(['ESTADO'], as_index = False)['PREÇO MÉDIO REVENDA'].mean()



st.dataframe(df_filtrado.groupby(['REGIÃO','ESTADO', 'PRODUTO'], as_index = False)['PREÇO MÉDIO REVENDA'].mean(), )

st.line_chart(data=linha, x='ESTADO', y='PREÇO MÉDIO REVENDA')

