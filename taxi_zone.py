# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:42:31 2020

@author: geomc
"""

import csv
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i","--input_data", help="",
                    type=str, default='./data/yellow_tripdata_2020-04.csv')

parser.add_argument("-i1","--input_data1", help="",
                    type=str, default='./data/taxi+_zone_lookup.csv')


args = parser.parse_args()

#Database Completo Aprile
A1_data_df = pd.read_csv((args.input_data))

#Database di Aprile (20 righe)
A2_data_df = A1_data_df.head(100)

#Database delle borough
B_data_df = pd.read_csv((args.input_data1))

#Ampliato il database iniziale, aggiungendo informazioni attraverso il Location ID in merito al Distretto di inizio corsa(PULocation)
C_data_df = A2_data_df.join(B_data_df.set_index('LocationID'), on='PULocationID')

#Rimozione delle colonne superflue dal C_data_df
C_data_df.drop(['Zone', 'service_zone'], axis=1, inplace=True)

