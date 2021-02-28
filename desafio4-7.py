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
# Asi puedo visualizar el array de structs
MPE1004 = pd.read_json(filename, typ='series')

# Creo el dataframe desde la estructura deseada
MPE1004 = pd.json_normalize(MPE1004.loc["results"])

# Selecciono solo la información de interés y lo grabo en un nuevo dataframe
products_info = MPE1004.loc[:, ["id", "sold_quantity", "available_quantity"] ]
products_info.insert(0, "rowId", np.arange(1, 40, 1), True)

# "products_info" es el resultado del desafío 4


#%% DESAFÍO 5 - Agregar las visitas al DataFrame con datos de ventas

# Leo los datos del archivo cvs
filename = "visits.csv"
data_visits = pd.read_csv(filename)

# Uno los datos de visits al dataframe del desafío 4 usando la columna idItem para el join
visits_info = products_info.loc[ : , ["id", "sold_quantity"] ].join(data_visits.set_index("itemId"), on="id")

# Filtro los elementos sin ventas
visits_with_sold = visits_info.iloc[ visits_info.index[visits_info['sold_quantity'] != 0] , : ]

# "visits_with_sold" es el resultado del desafío 5


#%% DESAFÍO 6 - Agregar métricas a un DataFrame

# Copio el dataframe
conversion_data = visits_with_sold.copy(deep=False)

# Le inserto una nueva columna con el encabezado "conversionRate" y los datos requeridos
conversion_data.insert(3,"conversionRate", conversion_data['sold_quantity'] / conversion_data['visits'], True)

# Ordeno los datos del dataframe de manera que descendente respecto a "conversionRate"
conversion_sort = conversion_data.sort_values('conversionRate',ascending=False)

# Agrego la columna del ranking
conversion_sort['conversionRanking'] = np.arange(len(conversion_data))+1

# "conversion_sort" es el resultado del desafío 6


#%% DESAFÍO 7 - Porcentaje de Stock

# Copio el dataframe
percentage_stock = products_info.copy(deep=False)

# Selecciono las columnas indicadas
percentage_stock  = percentage_stock .loc[ : , ["id", "available_quantity"] ]

# Agrego la columna del stock, con el cálculo del porcentaje de stock de cada articulo
percentage_stock['stockPercentage'] = ( percentage_stock.loc[:, "available_quantity" ] / sum(percentage_stock.loc[:, "available_quantity" ]) ) *100

# Ordeno los datos del dataframe de manera que descendente respecto a "stockPercentage"
percentage_stock_sort = percentage_stock.sort_values('stockPercentage',ascending=False)

# "percentage_stock_sort" es el resultado del desafío 7
