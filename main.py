import pandas as pd
import dask.dataframe
import os
import sys
import matplotlib.pyplot as plt

def clean_df(data, *series, uniq=False):
    #Get the series string or strings.
    series=series[0]
    #Strip whitespace from series and sort.
    data[series] = data[series].str.strip()
    data = data.sort_values(by=series)
    #If uniq is True, drop duplicates.
    if uniq:
        data = data.drop_duplicates(subset=[series])
    return data

#If you do not have the text file in your current directory, download and extract it.

if not os.path.isfile('occurrence.txt'):
    print('\nFile not found. Please download or move occurrence.txt here.\n')
    print('Download ZIP file and extract occurrence.txt at https://www.gbif.se/ipt/archive.do?r=fishbase')
    sys.exit()

#This is a huge database so dask actually loads 3-4 times quicker than normal pandas.
#It has both numbers and letters so treating the db as a string type is the best option for now.

fish_database=pd.read_csv('occurrence.txt', sep='\t', dtype=str)
fish_database_unique=fish_database.drop_duplicates(subset=['scientificName'])
fish_database_unique=clean_df(fish_database_unique,'scientificName','country', uniq=True)
print(fish_database_unique[['scientificName','country']])

