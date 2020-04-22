# Diomedes' EDA Library
"""For Data Visualization and Annalysis pourposes"""

# External library imports.
# %matoplotlib inline #only works in jupyter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn; seaborn.set()


# Large functions
def mean_min_max_standard (variable):
    """
    Prints the Average (mean), Min & Max (min, max) and Standard Deviation (standard) of a given vairable.
    This function does not return anything. I'ts only for show.
    No strs allowed!
        -variable = variable to be calculated
    """
    mean_v = variable.mean()
    min_v = variable.min()
    max_v = variable.max()
    standard_v = variable.std()

    print (f"\n------Function Mean, Min, Max, Standard------")
    print (f"Mean of variable: {mean_v}cm")
    print (f"Min in variable: {min_v}cm")
    print (f"Max in variable: {max_v}cm")
    print (f"Standard Deviation in variable: {standard_v}")

def percentiles (variable):
    """
    Prints information about the distribution of the data, showing the 25 and 75 (var_25 & 75 respectively) percentile as well as the median (var_median)
    This function does not return anything. NO strs allowed!
        -variable = variable to be calculated
    """
    var_25 = np.percentile(variable, 25)
    var_median = np.median(variable)
    var_75 = np.percentile(variable, 75)

    print (f"\n------Function Percentiles------")
    print (f"25th percentile: {var_25}")
    print (f"Variable's median: {var_median}")
    print (f"75th percentile: {var_75}")

def plotter (variable):
    """
    Plots the distribution of the data across the board. This function does not return anythig.
    NO strs allowed!
        -variable = variable to be plotted
    """

    print ("\n------Plotter Function------")
    plt.hist (variable)
    plt.title ("Distribution of Variable")
    plt.xlabel ("X axis")
    plt.ylabel ("Y axis")
    plt.show()

def popular (df, item_searched, quantity):
    """
    Takes the dataframe provided and returns the most repeated item and its quantity,
    and returns them for further use. NEEDS to be fed the fields manually in the 
    item and quantity variables OUTSIDE the function.
        -df = dataframe to be used
        -item_searched = column name of item to be searched
        -quantity = column name of item to be searched
    """
    item = df[item_searched].value_counts().idxmax()
    quantity = df.loc[df.item_name == item, quantity].sum()

    return item, quantity

def capitalizer (var):
    """
                        What it does
    Capitalizes the first letter of a string located in a dataframe's column.

                        What it needs
    A dataframe's column to be slotted into the variable
    """
    capitalize = lambda e: str(e).title()
    for c in range(len(var)):
        var[c] = capitalize(var[c])

def f_protected (x):
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
    i = 0
    l1=[{(yield i) for i in range(15)}]
    
    return filter_f(x = l1)

def general_info (df):
    """
                        What it does
    Takes the dataframe and scans it for NaN values, measures its shape and checks the column names. All of theese are returned at the end.

                        What it needs
    Your dataframe
    """
    print("""1) Presence and numbers of NaN values \n2) Shape of df \n3) Column names \n4) All of the above""")
    choice = int(input("Which data would you like to have? (only numbers are valid inputs!)>"))
    
    nan = df.isnull().any()
    nan_count = df.isnull().sum()
    shape = df.shape
    col_names =  df.columns

    if choice == 1:
        return nan, nan_count
    elif choice == 2:
        return shape
    elif choice == 3:
        return col_names
    elif choice == 4:
        return nan, nan_count, shape, col_names


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

def gender_search (df):
    """
                        ---What it does---
    gender_search goes trough your df 'gender' column and checks the values. If if finds 1, 2 or 0 does the following:
        * If the value is equal to 1: changes the value to 'Female'
        * If the value is equal to 2: changes the value to 'Male'
        * If the value is equal to 0: takes your 'name' column and makes a new variable with the first name, then checks it with it's own DB and changes the value to whatever gender is assinged to it.
        * None of the above: does nothing, congrats.

    Prints a "Done" when its done.

                        ---What it needs---
    gender_search requires the following:
        * Your df of choice to change (df)
                - Your columns SHOULD be named 'name' and 'gender' for it to work
        * A df of names and their current gender value: 
                - This df SHOULD be named 'dfnu' (DataFrame Names Unique)
                - This df SHOULD have it's values filtered through the drop_duplicates method of pandas (keep= whatever you want except false)
                        
                        ---Notes---
    Feel free to add more genders to the mix, but be reminded that you'll need a df that supports it.
    """
    for e in df.index:
        usuario = df.loc[e]
        gender = usuario['gender']
        
        if gender == 0:
            name = usuario['name'].split(' ')[0]
            listSerie = dfnu['gender'].loc[dfnu.name == name].unique()
            if len(listSerie) == 1:
                df.loc[e, 'gender'] = listSerie[0]
            else:
                df.loc[e, 'gender'] = None
            print(df.loc[e, 'gender'])
        elif gender == 1:
            df.loc[e, 'gender'] = 'Male'
        else:
            df.loc[e, 'gender'] = "Female"

    print ("Done")

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


# LAMBDAS

# Convert takes a timestamp object and converts it to a date object. Useful for dataframes columns
convert = lambda e: datetime.utcfromtimestamp(e).strftime('%Y-%m-%d') # %H:%M:%S ommited

# Gender transforms data into genders (male/female)
gender = lambda x: "Female" if x == 1 else ("Male" if x == 2 else x)