import sqlite3 as sql
from numpy import append
import pandas as pd
from IPython.display import display
from pandas.core.indexes.base import Index

tabela_cliete = pd.read_csv('ClientesBanco.csv', encoding='latin1')

conexao = sql.connect('banco.db')
tabela_cliete.to_sql('Clientes', con=conexao, if_exists='append', index=False) #transfere um excel para um arquivo sqlite
conexao.close()

