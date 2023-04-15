import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
os.chdir('C:\\Users\\User.PC-ESTACAO\\Downloads')
df = pd.read_csv('SP_poluicao_dados.csv')

#poluente mais crítico

media_por_poluente = df.groupby('Poluente') ['Valor'].mean()
media_por_poluente = media_por_poluente.sort_values()
print (media_por_poluente)

print('Soma de poluição por poluente')
soma_por_poluente = df.groupby('Poluente') ['Valor'].sum()
soma_por_poluente = soma_por_poluente.sort_values()
print (soma_por_poluente)

#Localidade mais afetada pela poluição

media_poluicao_local = df.groupby('Estacao') ['Valor'].mean()
media_poluicao_local = media_poluicao_local.sort_values()
print(media_poluicao_local)

soma_poluicao_local = df.groupby ('Estacao') ['Valor'].sum()
soma_poluicao_local = soma_poluicao_local.sort_values()
print(soma_poluicao_local)
