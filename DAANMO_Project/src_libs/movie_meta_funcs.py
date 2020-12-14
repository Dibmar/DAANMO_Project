import pandas as pd
import numpy as np


def genre_counter (df, df_2, col1):
    """
                        ---What it does---
    Counts the number of times the film genres appears in the df, and stores them into a new df object.
                        
                        ---What it needs---
        - A df object with the column to be counted (df)
        - A df object to be clone with the data to be searched in df (df2)
        - col1 the name of the column to be seached. It MUST be named the same in both dfs
                        ---What it returns---
    A new df (df3) with the counts stored in a new column called 'counts'.
    """
    df3 = df_2.copy()

    df3.insert(df3.shape[1], 'counts', 0)

    for e in df[col1]:

        for i in list(e):

            if i in list(df3[col1]):
                df3['counts'].loc[df3[col1] == i] +=  1

            else:
                pass

    df3 = pd.DataFrame(df3)

    return df3


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