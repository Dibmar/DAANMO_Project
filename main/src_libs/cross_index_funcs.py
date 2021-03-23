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
todatetime = lambda e: datetime.utcfromtimestamp(e).strftime('%Y-%m-%d') # %H:%M:%S ommited