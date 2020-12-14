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

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--in_data", help="Complete path il file input_data.json",
                    type=str, default='./data/yellow_tripdata_2020-04.csv')

parser.add_argument("-i1", "--in_data1", help="Complete path il file input_data.json",
                    type=str, default='./data/taxi+_zone_lookup.csv')

parser.add_argument("-o", "--out_data", help="Complete path il file input_data.json",
                    type=str, default='./results/output_data.xlsx')

args = parser.parse_args()


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
    
    pass

class CSVReader(Reader):
     
    def __init__(self, filename):
        self.filename = filename

    def get_lista_delle_corse(self):        
        data = pd.read_csv(self.filename)
        
        return data




class join():
    pass


class decorator():
      df = pd.DataFrame(data, columns=[
            'pagamenti più frequenti',
            'pagamenti meno frequenti',
            'credit card',
            'cash',
            'no charge',
            'dispute',
            'unknown',
            'voided trip'])
     return df

class features():
    pass    



# ______________________________________________________________

reader = Reader.create_instance(args.in_data)
df_taxis = reader.get_lista_delle_corse()





