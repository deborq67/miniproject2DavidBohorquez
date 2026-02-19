import pandas as pd
import dask.dataframe
import os
import sys
import matplotlib.pyplot as plt


'''This class handles most of the aesthetics of my graphs, meaning all I
have to do is put in the mandatory information like title, x, and y fields.
The class handles the longer decorative parts.'''


class GraphFormat:
    def __init__(self, df, x=None, y=None, labels=None):
        self.df = df
        self.x = x
        self.y = y
        self.labels = labels

    # Get Top 10 items of a column and turn it into a pie chart.

    def pie_chart_top_10(self):
        top_10 = self.df[f'{self.x}'].value_counts().iloc[:10]
        top_10.plot(kind="pie", colormap='tab20c')
        plt.show()
        return top_10

# *series allows the field to have more than one argument if needed.
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
fish_database_unique=fish_database.dropna(subset=['scientificName'])
fish_database_unique=clean_df(fish_database_unique,'scientificName', uniq=True)

#Q1: What fish orders have the most species?

'''For some taxonomical context, orders are big groups of organisms with common traits.
  For example, butterflies and moths belong in the order Lepidoptera, catfish belong in
  the order Siluriformes, etc.'''

GraphFormat(fish_database_unique,'order').pie_chart_top_10()

