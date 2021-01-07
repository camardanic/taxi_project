# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:42:31 2020

@author: geomc
"""

import csv
import pandas as pd
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser()

#type list = specifico una lista di file
parser.add_argument("-i","--input_data", help="",
                    type=str, default='./data/yellow_tripdata_2020-04.csv')


#modificare, inserirlo sempre senza la possibilità di cambiarlo
parser.add_argument("-i1","--input_data1", help="",
                    type=str, default='./data/taxi+_zone_lookup.csv')


args = parser.parse_args()

#Database Completo Aprile
A1_data_df = pd.read_csv((args.input_data))

#Database di Aprile (100 righe)
A2_data_df = A1_data_df.head(100)

#Database delle borough
B_data_df = pd.read_csv((args.input_data1))

#Ampliato il database iniziale, aggiungendo informazioni attraverso il Location ID in merito al Distretto di inizio corsa(PULocation)
C_data_df = A2_data_df.join(B_data_df.set_index('LocationID'), on='PULocationID', how='inner')


#Rimozione delle colonne superflue dal C_data_df
C_data_df.drop(['Zone', 'service_zone'], axis=1, inplace=True)

#Rimozione dalla colonna payment_type di tutte le righe con valoeri Nan
C_data_df.dropna(subset=['payment_type'], inplace=True)

#Numero di pagamenti per ogni tipologia
num_type_payment=C_data_df['payment_type'].value_counts()

#Tipi di pagamento
type_payment=C_data_df['payment_type'].unique()

#Elenco dei Borough
Borough=C_data_df['Borough'].unique()

#Modo in cui vengono eseguiti i pagamenti in ogni distretto 
df_out= pd.DataFrame(0,index=Borough, columns=type_payment)
for i in tqdm(range(len(C_data_df))): 
    df_out.loc[(C_data_df.loc[i,'Borough'],C_data_df.loc[i,'payment_type'])] += 1 


A2_data_df['payment_type'].describe()



#Elenco dei Borough richiesti dall'utente(non tutti,esempio Manhattan)
Borough=['Manhattan']
C_data_df=C_data_df.set_index('Borough')
C_data_df=C_data_df.loc[Borough]
C_data_df=C_data_df.reset_index()

#Modo in cui vengono eseguiti i pagamenti in ogni distretto 
df_out= pd.DataFrame(0,index=Borough, columns=type_payment)
for i in tqdm(range(len(C_data_df))): 
    df_out.loc[(C_data_df.loc[i,'Borough'],C_data_df.loc[i,'payment_type'])] += 1 



