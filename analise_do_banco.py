import pandas as pd
import sqlite3 as sql
from IPython.display import display
import plotly.express as px

conn = sql.connect('banco.db')

tabela = pd.read_sql('SELECT * FROM Clientes', conn)
display(tabela.info())
conn.close()


def gerar_grafico(coluna, tabela):
    grafico_histograma = px.histogram(tabela, x=coluna, color='Categoria')
    grafico_histograma.show()

for coluna in tabela:
    gerar_grafico(coluna, tabela)