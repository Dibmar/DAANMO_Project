# Data wrangling libraries
import pandas as pd
import numpy as np
import ast
import sys, os

# Visualization libraries
import matplotlib as plt

# Custom libraries
import src_libs.data_hunter as dh
import src_libs.explorer as exp
import src_libs.movie_meta_funcs as movie_funcs


# Importing df
movie_meta_data = pd.read_csv(r'..\data\the-movies-dataset\movies_metadata.csv')

# Slicing
profit = movie_meta_data[['id', 'budget', 'revenue']]
popularity_df = movie_meta_data[['id', 'popularity']]
genres = pd.DataFrame(movie_meta_data[['id', 'genres']])
votes = movie_meta_data[['id', 'vote_average', 'vote_count']]

dataframes = [profit, popularity_df, genres, votes]

# OPERATIONS
for dataframe in dataframes:
    exp.general_info(dataframe)
    
    if dataframe.isnull().any == True:
        dataframe = dataframe.fillna(0)

# OPERATIONS/Profit
for column in profit.columns:
    if profit[column].dtype == 'O':
        to_nuke = dict(profit[pd.to_numeric(profit['budget'],errors='coerce').isnull()]['budget'])
        print (f'{to_nuke}\n')

        for e in to_nuke.keys():
            print(f'Deleting {e}')
            profit = profit.drop(e)
            
        print('\n... columns dropped')




