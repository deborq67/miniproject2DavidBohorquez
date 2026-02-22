### INF601 - Advanced Programming in Python
### David Bohorquez
### Mini Project 2
 
 
# Project Title
 
Mini Project 2: Fun Graphs About Fish

![Darter.png](https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/styles/full_width/public/etheostoma_brevirostrum_holiday_darter.jpg?itok=FOZxD5ov)
*Source: USGS*

## Description

**_DISCLAIMER:_** *There are much newer databases that contain more accurate information about the number of species of fishes as well as the countries they were found. Most of the species in this database were identified before 1999 and information is most likely outdated but this was the best freely-available fish database I could find that required no account to download.*

This program shows some different statistics on fish diversity using charts. It gives 3 different graphs each representing a different question:

* What fish orders have the most species? (pie chart)
* What countries have the most species diversity? (bar chart)
* Since 1980, what orders were the most frequently identified by year? (line graph)

## Getting Started

### Installing

This program was made using Python 3.13.11.
 
### Dependencies
 
You need the actual ZIP file the with database to start.

Download it [here.](https://www.gbif.se/ipt/archive.do?r=fishbase)

* ZIP file should be called `dwca-fishbase-v4.5.zip`. Put into your directory of execution.
* From it extract `occurrence.txt`, **file is over 300 MB.**
  * If you forget, the program would send you a friendly reminder to have it in your directory anyway.

All other dependencies needed are listed in the requirements.txt document. To install them, execute this command on Python:
 
```
pip install -r requirements.txt
```

### Executing program
 
* First, download `dwca-fishbase-v4.5.zip` and extract `occurrence.txt` from it in the directory of execution. 
* Download `main.py` and `requirements.txt` file. Keep them both in the same directory as `occurrence.txt`.
* Alternatively, you could download the ZIP and use the extracted directory as `occurrence.txt`.
* Run the command listed on the **Dependencies** section if you have not done so already.
* Depending on how your Python installation is set up, execute from the directory either of these commands:
```
python main.py
```
or
```
python3 main.py
```
If all is successful, you will see a folder called `charts` in your directory of execution with 3 graphs in a PNG format.
 
## Help
* **How accurate is this data?**

As a fish enthusiast, I can tell you that this dataset has many flaws. It was mainly compiled from data observations from as early as the 1890s! As such, many of these observations are biased towards North America but unfortunately this was the best fish data I could find freely available.

If you're interested in knowing about more accurate fish databases, please check out [fishbase.se](https://www.fishbase.se/) (one of my favorite scientific websites) or [Eschmeyer's Catalog of Fishes](https://researcharchive.calacademy.org/research/ichthyology/catalog/fishcatmain.asp?_gl=1*f99s5a*_gcl_au*MTUxMzk1MjY2LjE3NzE3OTc1MjY.*_ga*MTc0MjQ3NzYwNy4xNzcxNzk3NTI2*_ga_6Y72VP61VZ*czE3NzE3OTc1MjUkbzEkZzAkdDE3NzE3OTc1MjUkajYwJGwwJGg5MzEzOTcxMzQ.).

* **I downloaded the ZIP file but the program is telling me `Download ZIP file and extract occurrence.txt at https://www.gbif.se/ipt/archive.do?r=fishbase`.**

You might have forgotten to extract `occurrence.txt` from *within* the ZIP file and should do so within the same directory as the `main.py` file. Also, please do not tamper with the spaces in the text file as it is tab-delimited and doing so could corrupt the way Pandas reads it.
 
## Authors
 
David Bohorquez
 
## Version History

* Released as main.py
 
## License
 
This project is licensed under the GNU General Public License - see the LICENSE.md file for details
 
## Acknowledgments
 
* [Pandas Documentation](https://pandas.pydata.org/docs/user_guide/index.html)
* [Matplotlib Documentation](https://matplotlib.org/stable/api/matplotlib_configuration_api.html)
* [GBIF Sweden for providing this fish data set.](https://www.gbif.org/)
* [Stack Overflow post that helped filter orders.](https://stackoverflow.com/questions/18358938/get-row-index-values-of-pandas-dataframe-as-list)
* [This other post also assisted immensely in filtering orders.](https://stackoverflow.com/questions/17071871/how-do-i-select-rows-from-a-dataframe-based-on-column-values)
* [This source helped make the subset for the line graph.](https://stackoverflow.com/questions/35268817/unique-combinations-of-values-in-selected-columns-in-pandas-data-frame-and-count)
* 
