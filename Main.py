# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 17:31:41 2020

@author: danie
"""
# questo è il file iniziale

from abc import ABC, abstractmethod
# import csv
# import argparse
from os.path import splitext
import pandas as pd
import json
from tqdm import tqdm

# classe che viene istanziata dal main nel momento in cui si vuole effettuare
# il conteggio dei tipi di pagamento relativi alle corse dei taxi di NY 
# come input riceve una lista di file che devono
# trovarsi nella cartella C:/Documents/Log_Elearning/taxi_project/data

class file_list_features:
    
    def __init__(self,list_of_file):
        self.list_of_file = list_of_file
         
    
    def list_features(self,Borough = []):
        Borough_df = pd.read_csv('./data/taxi+_zone_lookup.csv')
        elenco_corse_df = pd.DataFrame()
        i = 0
        for filename in self.list_of_file:
            reader = Reader.create_instance(filename)      
            temp_df = reader.get_lista_delle_corse()
            i += 1
            elenco_corse_df = pd.concat([elenco_corse_df,temp_df])
        
        #Ampliato il database iniziale, aggiungendo informazioni attraverso 
        # il Location ID in merito al Distretto di inizio corsa(PULocation)
        input_data_df = elenco_corse_df.join(Borough_df.set_index('LocationID'), on='PULocationID')
        
        # istanziato un oggetto della classe Standardizator relativo al Dataframe
        # in input
        std = Standardizator(input_data_df)
        input_data_df = std.elimina_Nan()
        
        #Tipi di pagamento
        type_payment=input_data_df['payment_type'].unique()
        
        # se non è stata inserita in ingresso una lista di Borough desiderati
        # di default il programma analizza tutte le corse su tutti i distretti
        if Borough == []:
            Borough = input_data_df['Borough'].unique()              
            #Modo in cui vengono eseguiti i pagamenti in ogni distretto 
            df_out= pd.DataFrame(0,index=Borough, columns=type_payment)
            for i in tqdm(range(len(input_data_df))): 
                df_out.loc[(input_data_df.loc[i,'Borough'],input_data_df.loc[i,'payment_type'])] += 1 

        else:
        # se è stata inerita una lista di Borough si riduce il Dataframe
        # in input eliminando tutti gli indici corrispondenti ai distretti non
        # richiesti e poi si procede con il conteggio dei payments type
            input_data_df = std.elimina_Borough(Borough)
            df_out= pd.DataFrame(0,index=Borough, columns=type_payment)
            
            for i in tqdm(range(len(input_data_df))): 
                df_out.loc[(input_data_df.loc[i,'Borough'],input_data_df.loc[i,'payment_type'])] += 1 

        df_out.to_excel('./results/Payment_type.xls')
        return df_out
  
    # ---------------------------------------------------------------------
    # lettura dei file in input
    
class Reader(ABC):
   # interfaccia che a seconda dell'estensione del file d'ingresso
   # chiama il reader in grado di leggerlo
    
    @abstractmethod
    def get_lista_delle_corse(self):
        # Metodo astratto che deve essere sviluppato
        # nelle sottoclassi di tipo Reader
        pass

    @staticmethod
    def create_instance(filename):
            
            # Interfaccia per il riconoscimento dell'estenzione del file
            # in input del metodo di lettura corretto
 
            suffix = splitext(filename)[1][1:].lower()
            if suffix == 'json':
                return JSONReader(filename)
            elif suffix == 'csv':
                return CSVReader(filename)
            else:
                raise ValueError('unknown file type')
            
                   
# sottoclassi di Reader che leggono i file delle corse
# e restituiscono un dataframe 
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


     # -------------------------------------------------------------------

# classe chiamata nel momento in cui il df di input deve essere
# pulito da righe non utili ai fini del conteggio
class Standardizator():

    def __init__(self,df):
        self.df = df
           
    def elimina_Nan(self):
            #Rimozione dalla colonna payment_type di tutte le righe con valori Nan
            self.df = self.df.dropna(subset=['payment_type'])
            return self.df
        
    def elimina_Borough(self,Borough):
        #Rimozione degli indici dei distretti no richiesti dall'utente
        self.df = self.df.set_index('Borough')
        self.df = self.df.loc[Borough]
        self.df = self.df.reset_index()
        return self.df
     