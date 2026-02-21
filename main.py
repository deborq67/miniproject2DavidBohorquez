# INF601 - Advanced Programming in Python
# David Bohorquez
# Mini Project 2

# This project will be using Pandas dataframes. This isn't intended to be full blown data science project. The goal here is to come up with some question and then see what API or datasets you can use to get the information needed to answer that question. This will get you familiar with working with datasets and asking questions, researching APIs and gathering datasets. If you get stuck here, please email me!

# (5/5 points) Initial comments with your name, class and project at the top of your .py file.
# (5/5 points) Proper import of packages used.
# (20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
# Think of some question you would like to solve such as:
# "How many homes in the US have access to 100Mbps Internet or more?"
# "How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
# Here are some other great datasets: https://www.kaggle.com/datasets
# (10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
# (10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this file with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.

import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
from matplotlib.pyplot import xlabel

#First step: Make charts folder with a single command:
os.makedirs(name="charts/", exist_ok=True)


'''This class handles most of the aesthetics of my graphs, meaning all I
have to do is put in the mandatory information like title, x, and y fields.
The class handles the longer decorative parts.'''

class GraphFormat:
    def __init__(self, df, x=None, y=None, xlabel='', ylabel ='', title=''):
        self.df = df
        self.x = x
        self.y = y
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title

#Get Top 10 items of a column and turn it into a pie chart.

    def pie_chart_top_10(self):
        top_10 = (self.df[f'{self.x}'].value_counts()).iloc[:10]
        top_10_plot = top_10.plot(kind="pie", colormap='tab20c', shadow=True)
        top_10_plot.title.set_text(f'{self.title}')
        plt.tight_layout()
        plt.show()
        return top_10

#Now do a bar chart.

    def bar_chart_top_10(self):
        top_10 = (self.df[f'{self.x}'].value_counts()).iloc[:10]
        top_10_plot=top_10.plot(kind="bar", color="maroon")
        top_10_plot.set_ylabel(f'{self.ylabel}')
        top_10_plot.set_xlabel(f'{self.xlabel}')
        top_10_plot.title.set_text(f'{self.title}')
        # Hide the right and top bars in the graph. Makes the graph look better.
        top_10_plot.spines[['top', 'right']].set_visible(False)
        plt.tight_layout()
        plt.show()
        top_10_plot.get_figure().savefig("charts/"+f'{self.title}.png')
        return top_10

#Strips nas & whitespace, sorts them (to make sure the program is working), and
#drops duplicate names of whatever column to ensure unique values if applicable.


def clean_df(data, *series, uniq=False, pair=False):
    #Keeps the original df from being modified, which happened to me when I saw 100,000
    #of my rows dropped because I forgot this.
    data=data.copy()
    #Get the series string or strings.
    for name in series:
    #Drop na from each series.
        data.dropna(subset=[name])
    #Strip whitespace from series and sort by last inputted column.
        data[name] = data[name].str.strip()
        data = data.sort_values(by=name)
    #If uniq is True, drop duplicates.
    if uniq:
        # for each series, drop duplicates or find pairs.:
        data = data.drop_duplicates(subset=series)
    return data


#If you do not have the text file, download and extract it.

if not os.path.isfile('occurrence.txt'):
    print('\nFile not found.\n')
    print('Download ZIP file and extract occurrence.txt at https://www.gbif.se/ipt/archive.do?r=fishbase')
    sys.exit()

fish_database=pd.read_csv('occurrence.txt', sep='\t', dtype=str)
fish_database_year=fish_database.copy()
fish_database_year['dateIdentified'] = pd.to_datetime(fish_database_year['dateIdentified'], errors='coerce')
fish_database_year['dateIdentified']=fish_database_year['dateIdentified'].dt.strftime('%Y')
fish_database_unique_species=clean_df(fish_database,'scientificName', uniq=True)
fish_database_unique_country=clean_df(fish_database,'scientificName','country', uniq=True)

#Q1: What fish orders have the most species

'''For some taxonomical context, orders are big groups of organisms with common traits.
  For example, butterflies and moths belong in the order Lepidoptera. Catfish belong in
  the order Siluriformes.'''

# print(fish_database['country'].value_counts(dropna=False))
print(fish_database_unique_species['country'].value_counts())
print(fish_database_unique_country['country'].value_counts())
# print(fish_database_year['dateIdentified'].value_counts())
# print(f"Raw Count: {len(fish_database)}")

#Make labels by arguments, very similar to how you would on R graphs.
GraphFormat(fish_database_unique_species,'order', title = 'Fish Orders with the Most Members' ).pie_chart_top_10()
GraphFormat(fish_database_unique_country,'country', title='Countries with the Most Species', xlabel='Country', ylabel='Species Count').bar_chart_top_10()