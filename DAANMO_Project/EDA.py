# FUNCTIONS
import datetime
import numpy as np
from datetime import date
import matplotlib.pyplot as plt
import ast
import pandas as pd

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
        - A list of columns to construct the new df with (col_list).ç
        - The column to be searched (col_search)
        - A condition for separation (cond_1)
    ---What it returns---
    A df object (df3)

    """
    
    df2 = df.copy()
    df3 = df2[col_list]

    df3[col_list[1]] = df3[col_list[1]].fillna('[]').apply(literal_eval).apply(lambda x: [i[cond_1] for i in x] if isinstance(x, list) else [])
    return df3


### ----------------------------------

                                    # LAMBDAS

# Gender transforms data into genders (male/female)
gender = lambda x: "Female" if x == 1 else ("Male" if x == 2 else x)

rounder = lambda x: round(x)

                                    # GRÁFICOS

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