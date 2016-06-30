"""
Analyzes one's VK audios.
Input: csv.
Output: ???
"""

import os
import pandas as pd

# input_filename = 'output.csv'
list_of_csvs = [] # get the names of all csvs in the current dir
# print them all, example: #1 - one.csv; #2 - two.csv; #3 - asdasd.csv

# # ask the user what number they like the most
# filenumber = input('# of the required .csv-file:')

# filename = list_of_csvs[filenumber]
filename = "output_20160630_021254.csv"
df = pd.read_csv(filename, header=None, names=['artist', 'track', \
                                               'length', 'link'])

df.artist = [a.lower() for a in df.artist]

artists = df.iloc[:, 0:2].groupby('artist').count()
artists.rename(columns = ['artist', 'n_songs'])