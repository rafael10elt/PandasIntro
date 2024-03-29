# -*- coding: utf-8 -*-
"""Overview of Colaboratory Features

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/basic_features_overview.ipynb
"""

#Introdução ao pandas
#DATAFRAMES
import pandas as pd

data = { 'Estado':['Pernambuco','Santa Catarina', 'Paraná','Goiás','Bahia', 'Minas Gerais'],
        'Ano': [2019,2002,2003,2004,2005,2006],
        'População': [1.4,1.5,1.7,3.6,2.4,2.9]}

frame = pd.DataFrame(data)

frame

pd.DataFrame(data, columns=['Ano','Estado','População']) # Indica a ordem de exibição no dataframe

# Criando outro dataframe com os mesmos dados anteriores mas adicionando uma coluna
frame2 = pd.DataFrame(data, columns= ['Ano','Estado','População','Débito'],
                      index = ['um','dois','tres','quatro','cinco','seis'])

#Imprimindo o Dataframe
frame2

#Imprimindo a penas a coluna Estado
frame2['Estado']

frame2.index  #Imprime os indices
frame2.columns #Imprimi as colunas
frame2.values #Imprime os valores em forma de array
frame2.dtypes # Mostra os tipos de dados
frame2['Ano']# Mostra apenas a coluna Ano
frame2.Ano # Mostra apenas a coluna Ano modo 2
frame2[:2] #Imprime o dataframe excluindo a posição 2