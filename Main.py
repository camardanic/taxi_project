# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 17:31:41 2020

@author: danie
"""
# questo è il file iniziale

from abc import ABC, abstractmethod
import csv
import argparse
from os.path import splitext
import pandas as pd
import json
from tqdm import tqdm

# classe che viene istanziata dal main nel momento in cui si vuole effettuare
# il conteggio dei tipi di pagamento relativi # le corse dei taxi di NY 
# in un determinato mese,come input riceve una lista di file che devono
# trovarsi della cartella C:/Documents/Log_Elearning/taxi_project/data

class file_list_features:
    
    def __init__(self):
         # self.Borough_df = pd.read_csv('./data/taxi+_zone_lookup.csv')
         pass
    
    def lista_features(self,list_of_file):
        Borough_df = pd.read_csv('./data/taxi+_zone_lookup.csv')
        elenco_corse_df = pd.DataFrame()
        i = 0
        for filename in list_of_file:
            reader = Reader.create_instance(filename)      
            temp_df = reader.get_lista_delle_corse()
            i +=1
            # temp_df = decorator().elimina_Nan(temp_df)
            elenco_corse_df = pd.concat([elenco_corse_df,temp_df])
            
        #Ampliato il database iniziale, aggiungendo informazioni attraverso il Location ID in merito al Distretto di inizio corsa(PULocation)
        input_data_df = elenco_corse_df.join(Borough_df.set_index('LocationID'), on='PULocationID')
        
        #Tipi di pagamento
        type_payment=input_data_df['payment_type'].unique()
        
        #Elenco dei Borough
        Borough=input_data_df['Borough'].unique()
                    
        #Modo in cui vengono eseguiti i pagamenti in ogni distretto 
        df_out= pd.DataFrame(0,index=Borough, columns=type_payment)
        for i in tqdm(range(len(input_data_df))): 
            df_out.loc[(input_data_df.loc[i,'Borough'],input_data_df.loc[i,'payment_type'])] += 1 


        return df_out
  
    
  
    
  
    
  
    
  

class Reader(ABC):
    """
    interface
    """
    
    @abstractmethod
    def get_lista_delle_corse(self):
        """
        abstract method
        """
        pass

    @staticmethod
    def create_instance(filename):
       
            suffix = splitext(filename)[1][1:].lower()
            if suffix == 'json':
                return JSONReader(filename)
            elif suffix == 'csv':
                return CSVReader(filename)
            else:
                raise ValueError('unknown file type')
            
              
        

class JSONReader(Reader):
      def __init__(self,filename):
          self.filename = filename
          

      def get_lista_delle_corse(self):        
        
          fin=open(('./data/'+self.filename),'r')
          text = fin.read()
          data = json.loads(text)
          data = pd.DataFrame(data)
          fin.close()
          return data


class CSVReader(Reader):
     
     def __init__(self,filename):
          self.filename = filename
          

     def get_lista_delle_corse(self): 
         
         data = pd.read_csv(('./data/' + self.filename))   
         return data


class join():
    
    pass


class decorator():
    pass
    
     # def elimina_Nan(self,df):
         
        # pass
        




# ______________________________________________________________


#crea lista dei file da analizzare,questi devono essere salvati nella cartella
#data che si trova sul path C:/Documents/taxi_project/
dati = file_list_features()
dati = dati.lista_features(['yellow_tripdata_2020-04.csv'])

# reader = Reader.create_instance(dati)

# df_taxi = reader.get_lista_delle_corse()





