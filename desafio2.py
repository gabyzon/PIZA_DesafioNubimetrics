# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 02:46:50 2021

@author: Alvaro Gabriel Pizá
"""
#%% 
import urllib3
import requests
import json

#%% DESAFÍO 2 usando librería "request"

# Solicito la busqueda de la palabra linterna
search_response = requests.request('GET', 'https://api.mercadolibre.com/sites/MLA/search?q=linterna')

# A la respuesta la convierto en un diccionario
search_linterna = search_response.json()

# Almaceno el diccionario en un archivo JSON en la carpeta "searchjson202102"
with open('searchjson202102/search_linterna.json', 'w') as f:
    json.dump(search_linterna, f)


#%% DESAFÍO 2 usando librería "urllib3"

# Solicito la busqueda de la palabra linterna
http = urllib3.PoolManager()
search_response = http.request('GET', 'https://api.mercadolibre.com/sites/MLA/search?q=linterna')

# A la respuesta la convierto en un diccionario
search_linterna = json.loads(search_response.data.decode('utf-8'))

# Almaceno el diccionario en un archivo JSON en la carpeta "searchjson202102"
with open('searchjson202102/search_linterna.json', 'w') as f:
    json.dump(search_linterna, f)