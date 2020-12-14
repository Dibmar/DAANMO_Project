import pandas as import pd
iport numpy as np

def gender_for_name (df):
    """
                        ---What it does---
    Takes the 'name' column and the 'gender' column of your df and applies the gender and capper lambdas. This will return you a capitalized column of strings (name) and a Female/Male column.
                        
                        ---What it needs---
        - A dataframe with at leas two columns that MUST be named 'name' and 'gender' (df)

                        ---What it returns---
    This function does not return anything
    """

    gender = lambda x: "Female" if x == 'G' or x == 2 else ("Male" if x == 'B' or x == 1 else x)
    capper = lambda e: e.capitalize()

    df['gender'] = df['gender'].apply(gender)
    df['name'] = df['name'].astype(str)
    df['name'] = df['name'].apply(capper)
    df['name'] = df['name'].drop_duplicates(keep = 'first')