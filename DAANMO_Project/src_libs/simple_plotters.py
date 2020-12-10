# SIMPLE PLOTTER

# Libraries
import numpy as np
import pandas as pd
from datetime import date
import sys, os

# Plotting libraries
import matplotlib.pyplot as plt


helpful_reminder = ("""
                        ---POURPOSE---
This library is aimed towards plotting graphics using matplotlib.

                        ---IT USES---
    - pandas as pd
    - numpy as np
    - matplotlib as plt
    - sys, os -> for adding the path to path directory
""")

# FUNCTIONS

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

def population_pyramid_plotter (df, col_1, col_2, col_3, population):
    """
    ---What it does---
    Creates a population pyramid graph.
    ---What it needs---
        - A df object to plot (df)
        - A column to place on Y axis (preferably dates) (col_1)
        - A column representing the MALE population (col_2)
        - A column representing the FEMALE population (col_3)
        - A string to represent the population (population)
    ---What it shows---
    A pyramid graph
    """
    
    # Generating data
    objects = df[col_1]                                 # Labels on Y axis
    y_pos = np.arange(len(objects))
    data = df[col_2]                                    # MALE population
    data2 = df[col_3]                                   # FEMALE population
    labels= ['male', 'female']


    if data.max() > data2.max():                        # Scaler
        width = data.max() + (data.max()/8) 
    else:
        width = data2.max() + (data.max()/8)

    # Generating plots
    fig, axes = plt.subplots(ncols=2, sharey=True)
    axes[0].set_xlim(0, width)
    axes[1].set_xlim(0, width)
    axes[0].barh(y_pos, data, align='center', alpha=0.9, color= 'darkred')
    axes[1].barh(y_pos, data2, align='center', alpha=0.75, color= 'darkgreen')
    axes[0].invert_xaxis()                              # Inversion of axis to create pyramid
    axes[1].xaxis.grid()
    axes[0].xaxis.grid()
    
    # Generating labels
    plt.yticks(y_pos, objects, fontsize=10)
    fig.suptitle(f'Difference in the male/female {population} population', fontsize=15) # 'population' goes here
    fig.legend(labels, loc= 'lower center', bbox_to_anchor=(0.75,0.1))

    plt.show()