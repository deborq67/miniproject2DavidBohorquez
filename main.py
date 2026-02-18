import pandas as pd
import dask.dataframe
import os
import sys
import matplotlib.pyplot as plt

#If you do not have the text file, download and extract it.

if not os.path.isfile('occurrence.txt'):
    print('\nFile not found.\n')
    print('Download ZIP file and extract occurrence.txt at https://www.gbif.se/ipt/archive.do?r=fishbase')
    sys.exit()

#This is a huge database so dask actually loads 3-4 times quicker than normal pandas.
#It has both numbers and letters so treating the db as a string type is the best option for now.

fish_database=dask.dataframe.read_csv('occurrence.txt', sep='\t', dtype=str)
fish_database_unique=fish_database.drop_duplicates(subset=['scientificName'])
print(fish_database_unique['scientificName'].head())

