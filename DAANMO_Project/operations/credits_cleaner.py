# Data wrangling libraries
import pandas as pd
import numpy as np
import ast

# Visualization libraries
import matplotlib as plt

# Custom libraries
import src_libs.data_hunter as dh
import src_libs.explorer as exp
import src_libs.credits_funcs as cred_func


#  Importing dfs
full_credits = dh.csv_opener_from_path('..\data\the-movies-dataset\credits.csv')
dfnu = dh.csv_opener_from_path(r'..\data\the-movies-dataset\ready_dfs\dfnu_ready.csv')

# OPERATIONS
exp.general_info(full_credits)
exp.general_info(dfnu)

cast = pd.DataFrame(full_credits[['id', 'cast']])
crew = pd.DataFrame(full_credits[['id', 'crew']])

# OPERATIONS/CAST
"""
TODO
"""


