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
import src_libs.credit_funcs as cred_func


#  Importing dfs
full_credits = dh.csv_opener_from_path('..\\data\\the-movies-dataset\\credits.csv')
dfnu = dh.csv_opener_from_path(r'..\\data\\the-movies-dataset\\ready_dfs\\dfnu_ready.csv')

# OPERATIONS
exp.general_info(full_credits)
exp.general_info(dfnu)

cast = pd.DataFrame(full_credits[['id', 'cast']])
crew = pd.DataFrame(full_credits[['id', 'crew']])

# OPERATIONS/CAST

cast = cred_func.actor_separator(cast, ['id', 'cast_order', 'name', 'gender'])

top_10_actors = cast['name'].value_counts().head(10)                           # Values to save


# OPERATIONS/CREW
crew['crew'] = crew['crew'].apply(ast.literal_eval)
crew['crew_len'] = crew['crew'].apply(lambda x: len(x))

## Creation of PRODUCERS, DIRECTORS and WRITERS dataframes
cred_func.json_extractor(crew, 'director', 'Directing', ['name', 'gender'])
cred_func.json_extractor(crew, 'producer', 'Production', ['name', 'gender'])
cred_func.json_extractor(crew, 'writer', 'Writing', ['name', 'gender'])

directors = cred_func.personnel_separator(crew, ['id', 'name', 'gender'])
producers = cred_func.personnel_separator(crew, ['id', 'name', 'gender'])
writers = cred_func.personnel_separator(crew, ['id', 'name', 'gender'])



# FINAL OPERATIONS
dfs = [cast, producers, directors, writers]


for dataframe in dfs:
    df_report = exp.general_info(dataframe)

    # Assigning gender values (1 for male, 2, for female)
    dataframe['gender'] = dataframe['gender'].apply(cred_func.gender)
    gender_report_1 = dataframe['gender'].value_counts()                                              # Values to save

    # Searching 0 values still in gender in the dfnu dataframe
    cred_func.gender_search(dataframe, dfnu, 'name', 'gender')
    gender_report_2 = dataframe['gender'].value_counts()                                              # Values to save

    # Dropping missing gender values (gender = 0)
    dataframe = dataframe.replace(0, np.nan).dropna()
    gender_report_3 = dataframe['gender'].value_counts()                                              # Values to save

    exp.save_df(dataframe, name)



