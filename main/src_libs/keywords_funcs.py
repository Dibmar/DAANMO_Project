import pandas as pd
import numpy as np

def df_creator (df, col_list):
    """
                        ---What it does---
    Creates a new df_new object using a list of 2 columns from another df object. Use these function when the cells of the original df are in       list format.
                        ---What it needs---
    A df object (df)
    A list of 2 columns from the df (col_list). These MUST correspond with those of the df.
                        ---What it returns---
    A new df object (df_new)
    """
    
    first_column = []
    second_column = []
    for e in range(df.shape[0]):

        for i in range(len(df.loc[e, col_list[1]])):
            value_1 = df.loc[e, col_list[0]]
            first_column.append(value_1)

            value_2 = df.loc[e, col_list[1]][i]
            second_column.append(value_2)
            
    df_new = pd.DataFrame({col_list[0] : value_1_col, col_list[1] : value_2_col})
    
    return df_new


def single_condition_separator (df, col_list, col_search, cond_1):
    """
                        ---What it does---
    Separates the lists of countries in a production from the container and stores them in a new df in list format.
                        
                        ---What it needs---
        - A df object (df) with a json column to be extracted
        - A list of columns to construct the new df with (col_list).
        - The column to be searched (col_search)
        - A condition for separation (cond_1)

                        ---What it returns---
    A df object (df3)
    """
    
    df_2 = df_2[col_list].copy()

    df_2[col_search] = df_2[col_search].fillna(np.NaN).apply(ast.literal_eval).apply(lambda x: [i[cond_1] for i in x] if isinstance(x, list) else np.NaN)
    
    return df_2