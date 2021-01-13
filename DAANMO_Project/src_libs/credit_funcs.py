import pandas as pd
import numpy as np
import ast
from datetime import datetime



def gender_search (df, df2, col_1, col_2):
    """
                        ---What it does---
    Searches for values equal to 0 in the df gender column and places them into a new df object. Then splits and searches the names of those values in df2. Lastly if it finds them, updates the new df object and merges its values with those of the original df.

                        ---What it needs---
    - A df with a 'name' (col_1) and 'gender' (col_2) column or equivalent
        * Gender column must contain 0 in the rows for the function to be effective.
    - A df2 for comparison (dfnu) with 'name' and 'gender' column
    """

    df3 = df.loc[df['gender'] == 0]   
    
    for e in range(df3.shape[0]):
        name = (df3[col_1].iloc[e]).split(' ')[0]   
        
        if name in list(df2['name']):
           df3[col_2].iloc[e] = list(df2.loc[df2['name'] == name, 'gender'])[0]

    df.loc[df[col_2] == 0] = df3


def cast_cleaner (df, col_1, col_list, cond_list):
    """
                        ---What it does---
    Cleans the cast df into a workable format. It returns the size of the cast, the actors names (in list format) and their gender (also as a list)
    
                        ---What it needs---
        - A df object (df)
        - A list of columns to check (col_list)
        - A list of conditions to check (cond_list)

                        ---What it returns---
    The updated df
    """
    def cast_size (df, col_1):
        df['cast_size'] = df[col_1].apply(lambda x: len(x))

    def cast_info (df, col_1, col_2, condition):
        df[col_2] = df[col_1].apply(lambda x: [i[condition] for i in x] if isinstance(x, list) else [])
    

    df[col_1] = df[col_1].apply(ast.literal_eval)
    
    cast_size (df, col_1)

    for col_2 in range(len(col_list)):
        
        for condition in cond_list:
            
            column = col_list[col_2]

            print (f'Working on {column} with {condition} as filter...')
            cast_info (df= df, col_1= col_1, col_2= column, condition= condition)

            print (f'\n{col_2} done.\n')

    print (df.head())

    return df


def json_extractor (df, column, source, condition_list, function):
    """
                        ---What it does---
    This function applies a series of lambdas to a json string located in a dataframe, in order to extract it's values. Overwriting the original file in the process.

                        ---What it needs---
        - A dataframe object (df)
        - The name of the column to be searched (column)
        - The key searched in the json (source). Related to functions.
            E g. "department"
        - A noun for the name of the column (role_name)
        - An adjective (or a list of) for the contidion of the column name (condition_list)
        - One of the keys of the json (fucntion).
            E g. "Directing"

                        ---What it returns---
    This function does not return anything.
    """
    condition = ''
    condition_extractor = lambda x: [i[condition] for i in x if i[source] == function]
    
    if type(condition_list) ==  list:

        for condition in condition_list:
            colum_name = f'{condition}'
            df[colum_name] = df.loc[:, column].apply(condition_extractor)
    
    else:
        colum_name = f'{condition_list}'
        df[colum_name] = df.loc[:, column].apply(condition_extractor)


def personnel_separator (df, col_list):
    """
                        ---What it does---
    Creates a new df_new object using a list of 3 columns from another df object. Use these function when the cells of the original df are in       list format.
                        ---What it needs---
    A df object (df)
    A list of 34 columns from the df (col_list). These MUST correspond with those of the df.
                        ---What it returns---
    A new df object (df_new)
    """

    value_1_col = []
    value_2_col = [] 
    value_3_col = []

    
    for e in range(df.shape[0]):
        for i in range(len(df.loc[e, col_list[1]])):
            value_1 = df.loc[e, col_list[0]]
            value_1_col.append(value_1)

            value_2 = df.loc[e, col_list[1]][i]
            value_2_col.append(value_2)
            
            value_3 = df.loc[e, col_list[2]][i]
            value_3_col.append(value_3)
            
    df_new = pd.DataFrame({col_list[0] : value_1_col, col_list[1] : value_2_col, col_list[2] : value_3_col})
    return df_new



def list_cleaner (df, col_list):
    """
                        ---What it does---
    Using a list of columns, this function creates a dataframe object and returns it. For it it iterates through the elements of the cells in the df of origin.
                        
                        ---What it needs---
        - A df object (df)
        - A list of columns from the df (col_list).
                        
                        ---What it returns---
    A new df object (df_new)
    """

    final_dict = {}

    for column in col_list:
        append_list = []

        for i in range(df.shape[0]):
            value = df.loc[i, column]
            append_list.append(value)
        
        final_dict[column] = append_list

    df_new = pd.DataFrame(final_dict)
    
    return df_new


# LAMBDAS

gender = lambda x: "Female" if x == 1 else ("Male" if x == 2 else x)
rounder = lambda x: round(x)
todatetime = lambda e: datetime.utcfromtimestamp(e).strftime('%Y-%m-%d') # %H:%M:%S ommited

print('Credit functions library ready!')