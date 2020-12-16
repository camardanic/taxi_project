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

# parser = argparse.ArgumentParser()

# parser.add_argument("-i", "--in_data", help="Complete path il file input_data.json",
#                     type=str, default='./data/yellow_tripdata_2020-04.csv')

# parser.add_argument("-i1", "--in_data1", help="Complete path il file input_data.json",
#                     type=str, default='./data/taxi+_zone_lookup.csv')

# parser.add_argument("-o", "--out_data", help="Complete path il file input_data.json",
#                     type=str, default='./results/output_data.xlsx')

# args = parser.parse_args()



class file_list_features():
    
    def __init__(self,list_of_file):
        self.list_of_file = list_of_file
        
    
    def lista_features(list_of_file):
        file_letti=[]
        i = 0
        for filename in list_of_file:
            data_input_df = Reader.create_instance(filename)
            file_letti.append(data_input_df)
            i +=1
            df_out = features().get_features(data_input_df)
            
        'alla fine del ciclo si sommano tutte le features e si mandano come output'
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
      def __init__(self, filename):
        self.filename = filename


      def get_lista_delle_corse(self):        
        
          fin=open('./data/'+self.filename,'r')
          text = fin.read()
          data = json.loads(text)
          data = pd.DataFrame(data)
          return data


class CSVReader(Reader):
     
    def __init__(self, filename):
        self.filename = filename

    def get_lista_delle_corse(self):        
        data = pd.read_csv('./data/'+self.filename)
        
        return data


class features():
    
    def get_features(self,data_input):
       pass
       # df_corse = data_input.decorator(data_input['payment_type'])
    """
    classe incaricata di estrarre il dataframe contenente
    le informazioni richieste
    """
    pass    







class join():
    
    pass


class decorator():
    
        """
        classe che deve verificare se all'interno del
        database non ci siano valori come payment type
        al di fuori dell'intervallo di interi {1;6}'
        """
        pass
        




# ______________________________________________________________


#crea lista dei file da analizzare,questi devono essere salvati nella cartella
#data che si trova sul path C:/Documents/taxi_project/
dati = file_list_features.lista_features(['yellow_tripdata_2020-04.csv','yellow_tripdata_2020-04.csv'])

reader = Reader.create_instance(dati)

df_taxi = reader.get_lista_delle_corse()





