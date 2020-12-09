# FUNCTIONS
import pandas as pd
import numpy as np
import datetime
from datetime import datetime
from datetime import date
import ast
import time


def from_list_to_single (df, col_1, col_2):
    """
    ---What it does---
    Takes the elements embeded into a list within a df object and creates a single column df using those elements.
    ---What it needs---
        - A df object (df)
        - The name of the column containing the data (col_1) MUST contain lists for it to work properly.
        - Name of the new column for the new df (col_2)
    ---What it returns---
    A single column df with the separated data (df2)
    """
    df_copy = df[col_1].copy()
    df_copy = df_copy.dropna()
    
    a_list = []

    for e in df_copy:
        for i in e:
            a_list.append(i)
    
    df2 = pd.DataFrame({col_2: a_list}).drop_duplicates(keep='first')
    df2 = df2.reset_index(drop = True)
    return df2

def zscore_nuke (df, column_1, threshold = 3):
    """
                        ---What it does---
    This function creates a copy of the dataframe. Then calculates the zscore column to the dataframe of choice. And locates the values under the threshold and eliminates them. Finally, returns the copy.

                        ---What it needs---
        - A dataframe object (df)
        - A column to be calculated. Values must be operable (column_1)
        - A value for threshold. Set to 3 as default.
    """
    
    df['column1_zscore'] = np.abs(stats.zscore(df[column_1]))

    df2 = df[(df.column1_zscore <= threshold) & (df.column2_zscore <= threshold)]

    df = df.drop('column1_zscore', axis=1)
    df2 = df2.drop('column1_zscore', axis=1)

    return df2

### SPECIFIC TO CREDITS NOTEBOOK

def gender_search (df, df2, col_1, col_2):
    """
                        ---What it does---
    Searches for values equal to 0 in the df gender column and places them into a new df object. Then splits and searches the names of those values in df2. Lastly if it finds them, updates the new df object and merges its values with those of the original df.

                        ---What it needs---
    - A df with a 'name' (col_1) and 'gender' (col_2) column or equivalent
        * Gender column must contain 0 in the rows for the function to be effective.
    - A df2 for comparison (dfnu) with 'name' and 'gender' column
    """

    df3 = df.loc[df[col_2] == 0]   
    
    for e in range(df3.shape[0]):
        name = (df3[col_1].iloc[e]).split(' ')[0]   
        
        if name in list(df2['name']):
           df3[col_2].iloc[e] = list(df2.loc[df2['name'] == name, 'gender'])[0]

    df.loc[df[col_2] == 0] = df3

def credits_cleaner (df, col_1, col_list, cond_list):
    """
    ---What it does---
    Cleans the cast df into a workable format. It returns the size of the cast, the actors names (in list format) and their gender (also as a list)
    ---What it needs---
    A df object (df)
    A list of columns to check
    A list of conditions to check
    ---What it returns---
    The updated df
    """
    def cast_size (df, col_1):
        df['cast_size'] = df[col_1].apply(lambda x: len(x))
    def cast_info (df, col_1, col_2, condition):
        df[col_2] = df[col_1].apply(lambda x: [i[condition] for i in x] if isinstance(x, list) else [])
        return df[col_2]
    df[col_1] = df[col_1].apply(ast.literal_eval)
    
    cast_size (df, col_1)
    col_len = len(col_list)
    a = 0
    for col_2 in col_list:
        condition = cond_list[a]
        print (f'Working on {col_2} with {condition} as filter...')
        cast_info (df, col_1, col_2, condition)
        a += 1
        print (f'\n{col_2} done.\n')
    return df

def actor_separator (df, col_list):
    """
                        ---What it does---
    Creates a new df_new object using a list of 4 columns from another df object. Use these function when the cells of the original df are in       list format.
                        ---What it needs---
    A df object (df)
    A list of 4 columns from the df (col_list). These MUST correspond with those of the df.
                        ---What it returns---
    A new df object (df_new)
    """

    value_1_col = []
    value_2_col = [] 
    value_3_col = []
    value_4_col = []

    for e in range(df.shape[0]):
        for i in range(df.iloc[e, 2]):
            value_1 = df.loc[e, col_list[0]]
            value_1_col.append(value_1)

            value_2 = df.loc[e, col_list[1]][i]
            value_2_col.append(value_2)
            
            value_3 = df.loc[e, col_list[2]][i]
            value_3_col.append(value_3)
            
            value_4 = df.loc[e, col_list[3]][i]
            value_4_col.append(value_4)

    df_new = pd.DataFrame({col_list[0] : value_1_col, col_list[1] : value_2_col, col_list[2] : value_3_col, col_list[3] : value_4_col})
    return df_new

def crew_cleaner (df, role_name, function, condition_list):

    condition_1_extractor = lambda x: [i[condition_list[0]] for i in x if i['department'] == function]
    condition_2_extractor = lambda x: [i[condition_list[1]] for i in x if i['department'] == function]

    col_name_1 = f'{role_name}_{condition_list[0]}'
    col_name_2 = f'{role_name}_{condition_list[1]}'

    df[col_name_1] = df.loc[:, 'crew'].apply(condition_1_extractor)
    df[col_name_2] = df.loc[:, 'crew'].apply(condition_2_extractor)

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

### SPECIFIC TO MOVIE-METADATA NOTEBOOK
def genre_counter (df, df2, col1):
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
    df3 = df2.copy()
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
    
    df2 = df.copy()
    df3 = df2[col_list]

    df3[col_search] = df3[col_search].fillna('[]').apply(ast.literal_eval).apply(lambda x: [i[cond_1] for i in x] if isinstance(x, list) else [])
    return df3

### SPECIFIC TO KEYWORDS NOTEBOOK
def keys_separator (df, col_list):
    """
                        ---What it does---
    Creates a new df_new object using a list of 2 columns from another df object. Use these function when the cells of the original df are in       list format.
                        ---What it needs---
    A df object (df)
    A list of 2 columns from the df (col_list). These MUST correspond with those of the df.
                        ---What it returns---
    A new df object (df_new)
    """

    value_1_col = []
    value_2_col = [] 

    
    for e in range(df.shape[0]):
        for i in range(len(df.loc[e, col_list[1]])):
            value_1 = df.loc[e, col_list[0]]
            value_1_col.append(value_1)

            value_2 = df.loc[e, col_list[1]][i]
            value_2_col.append(value_2)
            
    df_new = pd.DataFrame({col_list[0] : value_1_col, col_list[1] : value_2_col})
    return df_new

### SPECIFIC TO FIXER-NAMES
def gender_for_name (df):
    """
                        ---What it does---
    Takes the 'name' column and the 'gender' column of your df and applies the gender and capper lambdas. This will return you a capitalized column of strings (name) and a Female/Male column.
                        ---What it needs---
    A df with at leas two columns that MUST be named 'name' and 'gender'
    """

    gender = lambda x: "Female" if x == 'G' or x == 2 else ("Male" if x == 'B' or x == 1 else x)
    capper = lambda e: e.capitalize()

    df['gender'] = df['gender'].apply(gender)
    df['name'] = df['name'].astype(str)
    df['name'] = df['name'].apply(capper)
    df['name'] = df['name'].drop_duplicates(keep = 'first')

### SPECIFIC TO CROSS-INDEXING NOTEBOOK
def genre_corresponder (df, df_genres):
    """
    ---What it does---
    This function creates a dataframe that relates a count of the number of male and female actors in any of the given film genres identified.
    It must be said that because any given film genre has more than one film genre, the count is done multiple times in order to condense the population.
    ---What it needs---
        - A df object with the following columns (df):
            * id
            * gender (values must be 'Male' and 'Female')
        - A df object with the following columns (df_genres):
            * id
            * genre
    ---What it returns---
    A df object with columns named 'genre', 'male_counts' and 'female_counts'
    """
    def gender_mixer (df, df_genres):
        df_genres_c = df_genres.copy()
        df_male = df[['id', 'gender']].loc[df['gender'] == 'Male']
        df_female = df[['id', 'gender']].loc[df['gender'] == 'Female']
        
        df_male = df_male.groupby(by='id', sort = False, group_keys= False)['gender'].value_counts()
        df_female = df_female.groupby(by='id', sort = False, group_keys= False)['gender'].value_counts()

        new_df = pd.merge(left = df_male, right = df_female, how = "outer", on = 'id')
        new_df = new_df.reset_index()
        new_df.columns = ['id', 'male_counts', 'female_counts']
        new_df = new_df.fillna(0)
        final_df = df_genres_c.merge(new_df, left_on='id', right_on='id')
        final_df = final_df.groupby('genre')['male_counts', 'female_counts'].sum()
        final_df = final_df.reset_index()
        return final_df
    
    def genre_mixer(first):
        
        first['genre'] = first['genre'].str.split(", ")

        genre_list = []
        male_list = []
        female_list = []
        
        for e in first.index:
            for i in first['genre'][e]:
                genre_list.append(i)
                male_list.append(first['male_counts'][e])
                female_list.append(first['female_counts'][e])
        
        second = pd.DataFrame(list(zip(genre_list, male_list,female_list)), columns=['genre', 'male_counts', 'female_counts'])
        second = second.groupby('genre').sum()
        
        second['male_counts'] = second['male_counts'].astype('int64')
        second['female_counts'] = second['female_counts'].astype('int64')
        second = second.reset_index()
        second = second.sort_values(by=['male_counts', 'female_counts'], ascending = False)

        return second
    
    first = gender_mixer(df, df_genres)
    second = genre_mixer(first)

    return second

def packer_preparer (df, df2):
    """
                        ---What it does---
    This function mixes the release date, runtime and gender ratios of a given movie.
    Letting us see how the evolution of gender representation has evolved over time.
    And also where do we find a more equal gender representation when talking about runtime.
    
    1st) The function agregates all gender values in a df object (packer function)
    2nd) Crosses the id values associated and merges it with the df containing the dates (preparer function)

    All dfs are copied to ensure data integrity
                        
                        ---What it needs---
    - A df object with columns 'id' and 'gender' (df). The columns MUST have those names.
    - A df object with an 'id' to be merged with (df2). The column MUST have that name.
                        
                        ---What it returns---
    A df object (df_definitive)
    """

    def packer (df):
        """
        Creates the df object with the gender values and returns them
        """
        df_copy = df.copy() 
        gender_counts = df_copy.groupby(by='id', sort = False, group_keys= False)['gender'].value_counts()

        df_gender = pd.DataFrame(data = gender_counts)
        df_gender.columns = ['gender_counts']
        df_gender.reset_index(level=['gender'], col_level=1, inplace = True)  

        return df_gender
    

    def preparer (df_preliminary, df2):
        """
        Merges the 2 dfs ands returns a third one
        """

        df2_copy = df2.copy()
        df2_copy = df2_copy.dropna()
        
        df_pre = df_preliminary.copy()

        mal_counts = df_pre.loc[df_pre['gender'] == 'Male']
        fem_counts = df_pre.loc[df_pre['gender'] == 'Female']
        
        mal_counts['male_counts'] = mal_counts['gender_counts']
        fem_counts['female_counts'] = fem_counts['gender_counts']
        mal_counts = mal_counts.dropna(axis = 0)
        fem_counts = fem_counts.dropna(axis = 0)
        

        df_final = df2_copy.merge(mal_counts['male_counts'], left_on='id', right_on='id')
        df_final = df_final.merge(fem_counts['female_counts'], left_on='id', right_on='id')
        df_final = df_final.fillna(0)

        return df_final
    
    df_preliminary = packer (df)
    df_definitive = preparer (df_preliminary, df2)
    
    return df_definitive

def plotter_by_decade (df, col_list, condition = 'decade'):
    """
                        ---What it does---
    Creates a new df for easier plotting with all the relevant date grouped by decade. A copy is made of the original for data safekeeping.
                        ---What it needs---
    - A df object to group (df)
    - A list of colums that will be kept (col_list)
    - A column name for grouping. 'decade' by default (condition)
                        ---What it returns---
    A df object (df_2)
    """
    df_2 = df.copy()
    dtype = df_2.release_date.dtype
    if dtype == 'O':
        year = df_2['release_date'].str.split(pat="-")
        year_list = []
        for e in year:
            years = e[0]
            year_list.append(years)
        df_2['decade'] = year_list

    df_2['decade'] = df_2['decade'].astype('int64')
    df_2['decade'] = (df_2['decade'] // 10) * 10

    df_2 = df_2[col_list]
    df_2 = df_2.groupby(condition).sum()
    df_2 = df_2.reset_index()
    return df_2


# LAMBDAS

gender = lambda x: "Female" if x == 1 else ("Male" if x == 2 else x)
rounder = lambda x: round(x)
todatetime = lambda e: datetime.utcfromtimestamp(e).strftime('%Y-%m-%d') # %H:%M:%S ommited