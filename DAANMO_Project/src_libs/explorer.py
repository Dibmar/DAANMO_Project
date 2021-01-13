# EXPLORER

# Libraries
import pandas as pd
import numpy as np
import sys, os

helpful_reminder = ("""
                        ---POURPOSE---
This library is aimed towards general EDA.

                        ---IT USES---
    - pandas as pd
    - numpy as np
    - sys, os -> for adding the path to path directory
""")


# FUNCTIONS

def add_to_my_path_dir ():
    """
    TODO
                        ---What it does---
    This function adds the libraries current path to your pc path directory.

                        ---What it needs---
    - 
    
                        ---What it returns---
    This function does not return anything
    """
    CURR_DIR = os.path.dirname(os.path.abspath(__file__))
    print(CURR_DIR)
    sys.path.append(CURR_DIR)
    for path in sys.path:
        print(path)

def null_count (df):
    """
                        ---What it does---
    Counts all the NaN values present in a given dataframe, then prints the resutls in a short report.

                        ---What it needs---
        - A dataframe object (df)
    """
    is_null = df.isnull().sum()
    print (f'Number of null in columns:\n{is_null}')
    
def general_info (df):
    """
                        ---What it does--
    This function checks the info, columns and shape of the df, printing them. Also it checks the presence of NaNs values on the df and prints them in case it founds them.

                        ---What it needs---
    A df object
    """

    # df columns info
    print('\t\tGeneral information of the dataframe')
    print(f'{df.info()}\n')

    print("\n\t\tColumn's names:")
    print(f'{df.columns}\n')
    
    print("\n\t\tDataframe's shape:")
    print(f'\t- Rows: {df.shape[0]}')
    print(f'\t- Columns: {df.shape[1]}\n')

    # Presence of NaNs in df
    nulls = df.isnull().any()

    for n in nulls:
        if n == True:
            print("\n\t\tNaN's in dataframe")
            null_count(df)
            break



def time_indexer (df):
    """
                        What it does
    Groups your data by the time scale that you want (Year, Month, Day...) creating a new column in the process

                        What it needs
    A dataframe and your input
    """

    t_input = ''
    while t_input <= 3 and type(t_input) == int:
        t_input = int(input("""Select time scale: 
            1) Year
            2) Month
            3)Day>
        
        Please type only the relevant number!!! """))

    if t_input == 1:
        df['year'] = df.index.year

    elif t_input == 2:
        df['month'] = df.index.month

    elif t_input == 3:
        df['day'] = df.index.day


def save_df (df, name):
    """
                        ---What it does---
    Saves your dataframe of choice to a .csv file in the same directory of the parent file

                        ---What it needs---
        - A dataframe object to be saved (df)
        - A name for the file (name, asked by the function)

                        ---What it returns---
    This function does not return anything
    """
  
    df.to_csv(f'{name}_ready.csv', sep = ',')