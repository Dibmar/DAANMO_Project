# Data wrangling libraries
import pandas as pd
import numpy as np

# Custom libraries
import data_hunter as dh
# import src_libs.explorer as exp
# import src_libs.dfnu_funcs as functions
# from DAANMO_Project.src_libs import data_hunter as dh
# from DAANMO_Project.src_libs import explorer as exp
# from DAANMO_Project.src_libs import dfnu_funcs as functions

# Loading frames
english = pd.read_csv(r'F:\Programacion\1.BOOTCAMP\data\the-movies-dataset\names_df\scots_names.csv')
exp.general_info(english)

spanish = pd.read_csv(r'F:\Programacion\1.BOOTCAMP\data\the-movies-dataset\names_df\spanish_female.csv', encoding= 'latin1',sep=";")
exp.general_info(spanish)

french = pd.read_csv(r'F:\Programacion\1.BOOTCAMP\data\the-movies-dataset\names_df\french_names.csv', encoding= 'latin1',sep=";")
exp.general_info(french)


# Woriking with the english df
english.columns = ['year', 'gender', 'name', 'number', 'rank', 'position']
english = english['name', 'gender']

# Grouping the frames together and processing them
frames = [english, spanish, french]

for data in frames:
    functions.gender_for_name(data)
    data['name'] = data['name'].drop_duplicates(keep = 'first')


# Final assembly
dfnu = pd.concat(frames)
dfnu = dfnu.dropna()

exp.save_df(dfnu)