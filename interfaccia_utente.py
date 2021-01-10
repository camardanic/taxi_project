# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 20:47:18 2021

@author: geomc
"""
from Main import file_list_features

# ______________________________________________________________
#  INTERFACCIA UTENTE


# ANALISI DELLE TIPOLOGIE DI PAGAMENTO CORSE DEI TAXI DI NYC

# INSERIRE IN INPUT LISTA DEI FILE DA ANALIZZARE, questi devono essere salvati 
# nella cartella "data" che si trova sul path C:/Documents/taxi_project/
dati = file_list_features(['yellow_tripdata_2020-04.csv'])

# INSERIRE (facoltativo) LISTA DISTRETTI DESIDERATI fra i seguenti
# (Manhattan, Queens, Bronx, Brooklyn, Staten Island, EWR, Unknown)
dati = dati.list_features(['Queens'])


