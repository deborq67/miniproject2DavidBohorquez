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

    def pie_chart_top_5(self):
        #Get Top 5 of a series, everything else as your x-label
        #First, get counts of everything
        top_counts = (self.df[f'{self.x}'].value_counts())

        #Prevent df from getting modified.
        top_counts = top_counts.copy()

        #From those counts, get the Top 10 results, combine lower results into 1 slice:
        top_10 = top_counts.iloc[:5]
        misc_10 = top_counts.iloc[5:].sum()
        top_10[f'{self.xlabel}'] = misc_10

        #Make plots with percentages.
        top_10_plot = top_10.plot(kind="pie", colormap='tab20', shadow={'ox': -0.04, 'edgecolor': 'none', 'shade': 0.9}, autopct='%1.1f%%')

        #Place title and orient the text to where it does not get cut off.
        top_10_plot.title.set_text(f'{self.title}')
        plt.tight_layout()
        #Save plot as your title into "charts".
        top_10_plot.get_figure().savefig("charts/"+f'{self.title}.png')
        #Close the graph to prevent interference.
        plt.close()
        return top_10

#Now do a bar chart.

    def bar_chart_top_10(self):
        #Get Top 10 of X
        top_10 = (self.df[f'{self.x}'].value_counts()).iloc[:10]
        top_10_plot=top_10.plot(kind="bar", color=["aqua","teal","cadetblue"], edgecolor="black")
        top_10_plot.bar_label(top_10_plot.containers[0])

        #Set x,y, and title labels.
        top_10_plot.set_ylabel(f'{self.ylabel}')
        top_10_plot.set_xlabel(f'{self.xlabel}')
        top_10_plot.title.set_text(f'{self.title}')
        # Hide the right and top bars in the graph. Makes the graph look better.
        top_10_plot.spines[['top', 'right']].set_visible(False)
        plt.tight_layout()
        top_10_plot.get_figure().savefig("charts/"+f'{self.title}.png')
        #Close graph here too.
        plt.close()

        return top_10

#Strips nas & whitespace, sorts them (to make sure the program is working), and
#drops duplicate names of whatever column to ensure unique values if applicable.


def clean_df(data, *series, uniq=False):
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
        # for each series, drop duplicates or find pairs:
        data = data.drop_duplicates(subset=series)
    return data

#Cleans time-related columns.

'''NOTE: Pandas MAY give a warning in this section because the year in the column has both 2 and 4 digit
format. Ignore it since Pandas will fix this.'''

def clean_time(data, *series):
    #Don't modify the original import.
    data = data.copy()
    for name in series:
        # If field is blank, just NA it.
        data[name] = pd.to_datetime(data[name], errors='coerce')
        #Drop the NAs
        data = data.dropna(subset=name)
        data = data.sort_values(by=name)
    return data


#If you do not have the text file, download and extract it.

if not os.path.isfile('occurrence.txt'):
    print('\nFile not found.\n')
    print('Download ZIP file and extract occurrence.txt at https://www.gbif.se/ipt/archive.do?r=fishbase')
    sys.exit()

fish_database=pd.read_csv('occurrence.txt', sep='\t', dtype=str)

#Make 2 databases
fish_database_unique_species=clean_df(fish_database,'scientificName', uniq=True)
fish_database_unique_country=clean_df(fish_database,'scientificName','country', uniq=True)

#Q1: What fish orders have the most species?

'''For some taxonomical context, orders are big groups of organisms with common traits.
  For example, butterflies and moths belong in the order Lepidoptera. Catfish belong in
  the order Siluriformes.'''

#Make labels by arguments, very similar to how you would on R using ggplot2.

GraphFormat(fish_database_unique_species,'order', title = 'Top 5 Fish Orders with the Most Members', xlabel='Other Orders' ).pie_chart_top_5()

#Q2: What countries have the most species diversity?

#Same logic as the first graph:

GraphFormat(fish_database_unique_country,'country', title='Countries with the Most Species', xlabel='Country', ylabel='Species Count').bar_chart_top_10()

#Q3: Since 1980, what orders were the most frequently identified by year?

'''The line graphs were a bit more complex and I could not think of
any good way to write functions for them. Here is how they were made:'''

#Make a third database based on the cleaned species.

fish_time=clean_time(fish_database_unique_species,'dateIdentified')

#Make a subset with a count of each combination of year and order, call it ID_Year_Count.

fish_time=fish_time.groupby(['dateIdentified','order']).size().reset_index().rename(columns={0:'ID_Year_Count'})

#Extract only the top 5 orders in the table; in other words, the ones with the most data points.
#Only extract data after 1980.

top_5_orders=fish_time['order'].value_counts().iloc[:5]
#After counting, get list of all orders in index.
top_5_orders=list(top_5_orders.index.values)
#Extract rows with only the orders in the list, then filter only 1980 onward.
fish_time=fish_time.loc[fish_time['order'].isin(top_5_orders)]
fish_time =fish_time[fish_time['dateIdentified'] >= '1980-01-01']

#This part took me the longest to solve: the order themselves have to be turned into columns to plot them in 1 graph.

fish_time=fish_time.pivot(index="dateIdentified", columns="order", values="ID_Year_Count")

#Fill NaNs with 0 so lines do not appear broken.

fish_time = fish_time.fillna(0)

#Make the line graph.

ax=fish_time.plot(color=["aqua","teal","cadetblue","dodgerblue","deepskyblue"])

#Hide top and right lines for visual appeal. Make the lines touch the bottom and left.

ax.spines[['top', 'right']].set_visible(False)
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_bounds(0,max(fish_time.max())+1)

#Put legend on the top left of graph and put a title for it and the graph.

ax.legend(loc='upper left', title='Fish Orders')
graph_title=ax.title.set_text('Identified Species per Year by Top 5 Fish Orders')
ax.set_xlabel("")
ax.set_ylabel("Total Unique Species Identified")

#Take off minor ticks for visual appeal.
ax.minorticks_off()

#Save the final graph.
ax.get_figure().savefig("charts/"+ax.get_title()+'.png')
