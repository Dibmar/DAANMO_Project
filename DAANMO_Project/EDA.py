# FUNCTIONS
import datetime
import numpy as np
from datetime import date
import matplotlib.pyplot as plt
import ast
import pandas as pd
from datetime import datetime
import time

def f_protected (x, i= 0):
    """
    Create, in your library/module, a protected function called 'f_protected' that creates a lambda function.
    The lambda function must receive a param 'x' and return a boolean True if 'x' is higher than 5.
    Also, 'f_protected' must create a list ('l1') with 'list comprehesion' that generates a list from 0 to 15. 
    Finally, 'f_protected' must return 'l1' filtered (using function 'filter') using the lambda function.
    After that, create a decorator called "prepost". The decorator must receive an *args and a **kwargs argument.
    If in 'kwargs' there is a key called "url", then it must do the next:
            1. Open with a pandas the url as 'csv'. The variable is called 'df'.
            2. Do what normal function does (the function wrapped with the decorator).
            3. Plot histograms of each column in 'df'.
    """
    filter_f = lambda x: True if len(x) > 5 else False
    l1=[{(yield i) for i in range(15)}]
    
    return filter_f(x = l1)

def general_info (df):
    """
                        ---What it does--
    This function checks the info, columns and shape of the df, printing them. Also it checks the presence of NaNs values on the df and prints them in case it founds them.

                        ---What it needs---
    A df object
    """

    # df columns info
    print('-dtype, length and name of columns-')
    print(df.info())
    print()
    print(df.columns)
    print()
    print(df.shape)
    print()

    # Presence of NaNs in df
    need_to_print =  False
    nulls = df.isnull().any()
    print('-Presence of NaNs in df-')
    print (nulls)
    for e in list(nulls):
        if e == True:
            need_to_print = True
    if need_to_print == True:
        print()
        print('-Number of NaNs in df-')
        print (df.isnull().sum() )

def time_indexer (df):
    """
                        What it does
    Groups your data by the time scale that you want (Year, Month, Day...) creating a new column in the process

                        What it needs
    A dataframe and your input
    """
    t_input = input("Select time scale (year, week, day). Please type this as given here>")
    if t_input == "year":
        df['year'] = df.index.year
    elif t_input == "month":
        df['month'] = df.index.month
    elif t_input == "day":
        df['day'] = df.index.day

def df_save (df):
    """
                        ---What it does---
    Saves your df of choice to a .csv file in the same directory of the parent file

                        ---What it needs---
    * Your input for the name (be careful with adding spaces)
    * Your ready-to-save df
    """
    name = input("Type the name of your df> ")
    name = name + ".csv"
    df.to_csv(name, sep = ',')

def null_count (df):
    """
                        ---What it does---
    Identifies and counts the number of null values in any given df. Does not return anything.

                        ---What it needs---
    A DataFrame
    """
    null_in_df = df.isnull().any()
    is_null = df.isnull().sum()
    print (f'Presence of null in clolumns:\n{null_in_df}\n\nNumber of null in columns:\n{is_null}')

def value_counter(df):
    """
                        ---What it does---
    Counts the values of all columns of a given df and prints them in succesion.
                        ---What it needs---
    A df object
    """
    for e in df.columns:
        print(f"\n{e}:\n{df[e].value_counts()}")
        print('----------------')
       
def counter(counter):
    """
    ---What it does---
    Counter system to show progress of function
    """
    counter += 1
    sys.stdout.write("\r {0} %".format(counter))
    sys.stdout.flush()

def test():
    print('EDA lib ready')
test()

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

def zscore_nuke (df, column1, column2, threshold = 3):
    """
                        ---What it does---
    This function will add a zscore column to the df of choice, then loc the values that are bellow the threshold (3) and store them in a new df object. Lastly, the zscore columns will be droped.

    It only does it with 2 columns at the moment.

                        ---What it needs---
    -A df object
    -A value for threshold. Set to 3 as default.
    """
    
    df['column1_zscore'] = np.abs(stats.zscore(df[column1]))

    df['column2_zscore'] = np.abs(stats.zscore(df[column2]))

    df2 = df[(df.column1_zscore <= threshold) & (df.column2_zscore <= threshold)]

    df = df.drop(['column1_zscore', 'column2_zscore'], axis=1)
    df2 = df2.drop(['column1_zscore', 'column2_zscore'], axis=1)

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
def mixer (gender_df, genre_df):
    """
                        ---What it does---
    Takes the dfs provided and right-merges them based on the 'id' column. Then it counts and creates a new df with the gender count of the gender_df ('Male' and 'Female' values currently accounted for) and assings it to whatever film genre(s) the 'id' column was assigned to.
                        ---What it needs---
    This function needs:
        - A df object with 'id' and 'gender' columns named as shown here
            + The 'gender' column should contain 'Male' and 'Female' strings.
        - A df object with 'id' and 'genre' columns named as shown here
            + This df can contain embeded lists
                        ---What it returns---
    A new df object with the following columns:
        - genre: a list of chain strings containing one or more film genre (obj, list)
        - male_counts: number of male participants (int)
        - female_counts: number of female participants (int)
    """

    # Merging of dfs
    df3 = pd.merge(gender_df, genre_df, on='id', how='right')

    # Lists creation and gender and genre search
    genre_2 = []
    gender_2 = []

    for e in range(len(df3.index)):
        gend = df3.loc[e,'gender']    
        gen = df3.loc[e,'genre']
        if type(gen) == list:                   # If gen is an object, it is broken into multiple elements
            for n in gen:
                genre_2.append(n)
                gender_2.append(gend)
                
        else:
            genre_2.append(gen)
            gender_2.append(gend)
    
    # df4 creation, reindexing and generation of lists in genres       
    df4 = pd.DataFrame({'genre': genre_2, 'gender': gender_2})
    df4['male_counts'] = (df4.gender == 'Male').astype(np.int_)
    df4['female_counts'] = (df4.gender == 'Female').astype(np.int_)
    df4 =df4.drop('gender', axis = 1)
    
    df4 = df4.groupby('genre')['male_counts', 'female_counts'].sum()
    
    df4 = df4.reset_index()
    df4['genre'] = df4['genre'].str.split(', ')

    return df4

def corresponder (gender_genre, genre_df):
    """
                        ---What it does--
    Takes two df objects and seeks the film genres contained in the first (gender_genre) in the second df (a copy of genre_df). If it finds a match, takes the gender values of the first df and plugs it into the second. This is done in for loops in order to keep an accurate gender count.
                        ---What it needs---
    Two df objects with the following columns:
        - gender_genre:
            + genre (list)
            + male/female_values (both must be int)
        - genre_df
            + Genre (string)
                        ---What it returns---
    A copy of genre_df with the sum of the gender values of all the correspondant film genres. This is displayed in three columns (Genre, male/ female_values)
    """

    # copy of genre_df for safekeeping
    genre_df_copy = genre_df.copy()
    genre_df_copy.insert(1, 'male_counts', 0)
    genre_df_copy.insert(2, 'female_counts', 0)

    for e in range(len(gender_genre.genre)):
        genre_list = gender_genre.genre[e]
        if len(genre_list) == 1:
            if genre_list[0] in list(genre_df.genre):
                male_values = gender_genre.male_counts.loc[e]                                           # Male counts in gender_genre
                female_values = gender_genre.female_counts.loc[e]                                       # Female counts in gender_genre
                genre_key = list(genre_df.genre.loc[genre_df.genre == genre_list[0]])[0]                # Genre in genre_df
                
                what_was_male = genre_df_copy.male_counts.loc[genre_df_copy.genre == genre_key]         # For easier reading    
                what_was_female = genre_df_copy.female_counts.loc[genre_df_copy.genre == genre_key] 

                genre_df_copy.male_counts.loc[genre_df_copy.genre == genre_key] = what_was_male + male_values
                genre_df_copy.female_counts.loc[genre_df_copy.genre == genre_key] = + female_values

        else:
            for a in range(len(genre_list)):
               if genre_list[a] in list(genre_df.genre):
                    genre_key = list(genre_df.genre.loc[genre_df.genre == genre_list[a]])[0]
                    male_values = gender_genre.male_counts.loc[e]                                       # Male counts in gender_genre
                    female_values = gender_genre.female_counts.loc[e]                                   # Female counts in gender_genre
                    genre_key = dict(genre_df.genre.loc[genre_df.genre == genre_list[a]]).values()      # Genre in genre_df

                    what_was_male = genre_df_copy.male_counts.loc[genre_df_copy.genre == genre_key] 
                    what_was_male = genre_df_copy.female_counts.loc[genre_df_copy.genre == genre_key]
                    
                    genre_df_copy.male_counts.loc[genre_df_copy.genre == genre_key] = what_was_male + male_values
                    genre_df_copy.female_counts.loc[genre_df_copy.genre == genre_key] = what_was_female + female_values
                    
    return genre_df_copy

def packer_preparer (df, df2):
    """
                        ---What it does---
    This function mixes the release date, runtime and gender ratios of a given movie. Letting us see how the evolution of gender representation has evolved over time. And also where do we find a more equal gender representation when talking about runtime.
    
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


### ----------------------------------

                                    # LAMBDAS

# Gender transforms data into genders (male/female)
gender = lambda x: "Female" if x == 1 else ("Male" if x == 2 else x)

rounder = lambda x: round(x)

todatetime = lambda e: datetime.utcfromtimestamp(e).strftime('%Y-%m-%d') # %H:%M:%S ommited

                                    # GRAPHICS

def plot_bar(df_column, save_image = 0):
    """
                        ---What it does---
    Plots a barplot with the variable given. And if desired, saves the plot in the same directory as parent file with "<current date>_barplot.jpg" as name.
                        ---What it needs---
    A df_column, panda series or dictionary with numerical values
                        ---What it returns---
    If desired (save_image != 0), a jpg image file in the same directory using "<current date>_barplot.jpg" as name.
    """
    if df_column.sum() > 0:
        df_column.plot(kind = 'bar')
        if save_image != 0:
            name = str(date.today()) + '_barplot.jpg'
            plt.savefig(name)
    else:
        print(f'No numeric data to plot')

def plot_line(df_column, save_image = 0):
    """
                        ---What it does---
    Plots a lineplot with the variable given. And if desired, saves the plot in the same directory as parent file with "<current date>_lineplot.jpg" as name.
                        ---What it needs---
    A df_column, panda series or dictionary with numerical values
                        ---What it returns---
    If desired (save_image != 0), a jpg image file in the same directory using "<current date>_lineplot.jpg" as name.
    """
    if df_column.sum() > 0:
        df_column.plot()
        if save_image != 0:
            name = str(date.today()) + '_lineplot.jpg'
            plt.savefig(name)
    else:
        print(f'No numeric data to plot')

def plot_pie(df_column, save_image = 0):
    """
                        ---What it does---
    Plots a pieplot with the variable given. And if desired, saves the plot in the same directory as parent file with "<current date>_pieplot.jpg" as name.
                        ---What it needs---
    A df_column, panda series or dictionary with numerical values
                        ---What it returns---
    If desired (save_image != 0), a jpg image file in the same directory using "<current date>_pieplot.jpg" as name.
    """
    if df_column.sum() > 0:
        data = df_column
        # Create lables
        labels = dict(df_column).keys()

        # Plot pie chart
        plt.pie(data, autopct='%1.1f%%', startangle=0, shadow= True, pctdistance = 0.5, labeldistance = 1.2)

        # Legend and titles
        plt.legend(labels, loc= 'best')
        plt.title(df_column.name, loc='center')

        plt.tight_layout()
        plt.show()
        
        if save_image != 0:
            name = str(date.today()) + '_pieplot.jpg'
            plt.savefig(name)
    else:
        print ("No numeric data to plot")

def plotter_special (df, col_1, col_2, col_3, save = 0):
    """
                        ---What it does---
    Plots a barth plot of a df, sorting firts by col_2 then by col_3. If desired, saves the plot

                        ---What it needs---
    - A df object with numerical values in columns 2 & 3
    - A column to be placed in y axis (col_1)
    - Value 1 to sort and plot (col_2), in column format
    - Value 2 to sort and plot (col_3), in column format
    - If you want to save plot, change save value to anything than 0.and

                        ---What it stores---
    A .png file if desired.
    """

    df = df.sort_values(ascending= False, by= [col_2, col_3])
    
    objects = df[col_1]
    labels = [col_2.title(), col_3.title()] 
    data = list(df[col_2])
    data2 = list(df[col_3])
    y_pos = range(len(objects))

    # Creating the plots
    plt.barh(y_pos, data, align='center', alpha=0.9, color= 'orange')
    plt.barh(y_pos, data2, align='center', alpha=0.75, color= 'blue')
    plt.yticks(y_pos, objects, fontsize=10)


    # Cretaing labels and titles
    plt.legend(labels, loc= 'best')

    if save != 0:
        print ('Saving as .png')
        name = input('Type the name of the plot: ')
        plt.savefig(name + '.png')

    plt.show()