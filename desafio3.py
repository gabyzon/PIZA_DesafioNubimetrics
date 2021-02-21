# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 15:54:47 2021

@author: Alvaro Gabriel Pizá
"""
#%%
import pandas as pd
import os
import time

#%% Trabajo con los dataframes

#Creo un string con el nombre del archivo
filename = "Sellers.json"

# Leo el archivo de formato json y lo almaceno en un dataframe
sellers = pd.read_json(filename)

# Normalizo el dataframe
sellers = pd.json_normalize(sellers.loc[:,"body"])

# Selecciono solo la información de interés y lo grabo en un nuevo dataframe
output = sellers.loc[:, ["id", "site_id", "nickname", "points"] ]

# Creo un nuevo dataframe para los vendedores con puntaje positivo
positivo = output.iloc[ output.index[output['points'] > 0] , : ]

# Creo un nuevo dataframe para los vendedores con puntaje negativo
negativo = output.iloc[ output.index[output['points'] < 0] , : ]

# Creo un nuevo dataframe para los vendedores con puntaje cero
cero = output.iloc[ output.index[output['points'] == 0] , : ]

#%% Almaceno los resultados

fecha = time.strftime("%m/%Y/%d")
sitio = output.loc[0, "site_id"]
# Creo la estructura de carpetas necesaria

os.makedirs( str(sitio) + "/" + str(fecha) + "/positivo")
os.mkdir( str(sitio) + "/" + str(fecha) + "/negativo")
os.mkdir( str(sitio) + "/" + str(fecha) + "/cero")

# Guardo los resultados en archivos CVS

positivo.to_csv( str(sitio) + "/" + str(fecha) + "/positivo/positive_sellers.csv", index=False, sep=",")
negativo.to_csv( str(sitio) + "/" + str(fecha) + "/negativo/negative_sellers.csv", index=False, sep=",")
cero.to_csv( str(sitio) + "/" + str(fecha) + "/cero/zero_sellers.csv", index=False, sep=",")