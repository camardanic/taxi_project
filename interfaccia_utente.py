# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 20:47:18 2021

@author: geomc
"""
from Main import file_list_features

# ______________________________________________________________
#  INTERFACCIA UTENTE

# si istanzi la lista dei file da analizzare, questi devono essere salvati 
# nella cartella "data" che si trova sul path C:/Documents/taxi_project/
dati = file_list_features(['yellow_tripdata_2020-04.csv'])

# per ricevere la lista del conteggio di tutti i metodi di pagamento
# usare il metodo list_features 
dati = dati.list_features(['Queens'])




