# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 18:17:43 2021

@author: Alvaro Gabriel Pizá
"""
#%%
import pandas as pd
import numpy as np

#%% DESAFÍO 4 - Trabajo con los dataframes

#Creo un string con el nombre del archivo
filename = "MPE1004.json"

# Leo el archivo de formato json y lo almaceno en una serie
# Asi puedo visualizar el arrar de structs
data = pd.read_json(filename, typ='series')

# Creo el dataframe desde la estructura deseada
data2 = pd.json_normalize(data.loc["results"])

# Selecciono solo la información de interés y lo grabo en un nuevo dataframe
output = data2.loc[:, ["id", "sold_quantity", "available_quantity"] ]
output.insert(0, "rowId", np.arange(1, 40, 1), True)

# "output" es el resultado del desafío 4


#%% DESAFÍO 5 - Agregar las visitas al DataFrame con datos de ventas

# Selecciono las columnas indicadas
data3 = output.loc[ : , ["id", "sold_quantity"] ]

# Leo los datos del archivo cvs
filename = "visits.csv"
data_visits = pd.read_csv(filename)

# Uno los datos de visits al dataframe "data3" usando la columna idItem para el join
data4 = data3.join(data_visits.set_index("itemId"), on="id")

# Filtro los elementos sin ventas
output2 = data4.iloc[ data4.index[data4['sold_quantity'] != 0] , : ]

# "output2" es el resultado del desafío 5


#%% DESAFÍO 6 - Agregar métricas a un DataFrame

# Copio el dataframe
data5 = output2.copy(deep=False)

# Le inserto una nueva columna con el encabezado "conversionRate" y los datos requeridos
data5.insert(3,"conversionRate", data5['sold_quantity'] / data5['visits'], True)

# Ordeno los datos del dataframe de manera que descendente respecto a "conversionRate"
output3 = data5.sort_values('conversionRate',ascending=False)

# Agrego la columna del ranking
output3['conversionRanking'] = np.arange(len(data5))+1

# "output3" es el resultado del desafío 6


#%% DESAFÍO 7 - Porcentaje de Stock

# Copio el dataframe
data6 = output.copy(deep=False)

# Selecciono las columnas indicadas
data6 = data6.loc[ : , ["id", "available_quantity"] ]

# Agrego la columna del stock, con el cálculo del porcentaje de stock de cada articulo
data6['stockPercentage'] = ( data6.loc[:, "available_quantity" ] / sum(data6.loc[:, "available_quantity" ]) ) *100

# Ordeno los datos del dataframe de manera que descendente respecto a "stockPercentage"
output4 = data6.sort_values('stockPercentage',ascending=False)

# "output4" es el resultado del desafío 7
