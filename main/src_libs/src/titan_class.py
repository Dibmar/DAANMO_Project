# EDA libs

import pandas as pd
import numpy as np
from pandas.api.types import is_numeric_dtype

# Visualization libs

import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date

# Helpful libs

import sys, os

class Titan ():
    """
    This class has been created to work with dataframes and allow for a quicker EDA process. For this it uses:
        
        - The pandas library
        - The numpy library
        - The pandas/api/is_numeric_dtype function
        - The matplotlib library
        - The datetime/date library
        - The sys and os libraries

    This is able to change data types, deal with NaN values and represent columns.
    It is also capable of returning a dataframe object (for further EDA processing/Machine Learning implentation) or
    store a csv file in given directory.
    """
    def __init__(self, path):
        
        # For dataframe construction.
        self.df = ''
        self.path = path     


    def create_df(self, wish= False, sep=',', delimiter= None, header= 'infer', 
                names= None, index_col= None, usecols= None, squeeze= False, 
                prefix= None, mangle_dupe_cols= True, dtype= None,
                engine= None, converters= None,
                true_values= None, false_values= None, skipinitialspace= False, 
                skiprows= None, skipfooter= 0, nrows= None, 
                na_values= None, keep_default_na= True, na_filter= True,
                verbose= False, skip_blank_lines= True, parse_dates= False,
                infer_datetime_format= False, keep_date_col= False, date_parser= None,
                dayfirst= False, cache_dates= True, iterator= False,
                chunksize= None, compression= 'infer', thousands= None,
                decimal= '.', lineterminator= None, quotechar='"',
                quoting= 0, doublequote= True, escapechar= None, 
                comment= None, encoding= None, dialect= None, 
                error_bad_lines= True, warn_bad_lines= True, 
                delim_whitespace= False, low_memory= True, 
                memory_map= False, float_precision= None, storage_options= None):
        """
                            ---What it does---
        This function creates a dataframe object using the pandas library and the read_csv function.

                            ---What it needs--
            - The command to return/not return the dataframe (wish). Should be a boolean.
            - A path to follow (provided earlier in class creation). Should be a double barred ('\\') formatted  string.
            - The rest of necessary values are set to default (as they appear in the pandas documentation)

                            ---What it returns---
        The dataframe generated (self.df).
        """
        # For df creation
        self.sep = sep                                  # By default set as ','
        self.delimiter = delimiter
        self.header = header
        self.names = names
        self.index_col = index_col
        self.usecols = usecols
        self.squeeze = squeeze
        self.prefix = prefix
        self.mangle_dupe_cols = mangle_dupe_cols
        self.dtype = dtype
        self.engine = engine
        self.converters= converters
        self.true_values = true_values
        self.false_values = false_values
        self.skipinitialspace = skipinitialspace
        self.skiprows = skiprows
        self.skipfooter = skipfooter
        self.nrows = nrows
        self.na_values = na_values
        self.keep_default_na = keep_default_na
        self.na_filter = na_filter
        self.verbose = verbose
        self.skip_blank_lines = skip_blank_lines
        self.parse_dates = parse_dates
        self.infer_datetime_format = infer_datetime_format
        self.keep_date_col = keep_date_col
        self.date_parser = date_parser
        self.dayfirst = dayfirst
        self.cache_dates = cache_dates
        self.iterator = iterator
        self.chunksize = chunksize
        self.compression = compression
        self.thousands = thousands
        self.decimal = decimal
        self.lineterminator = lineterminator
        self.quotechar = quotechar
        self.quoting = quoting
        self.doublequote = doublequote
        self.escapechar = escapechar
        self.comment = comment
        self.encoding = encoding
        self.dialect = dialect
        self.error_bad_lines = error_bad_lines
        self.warn_bad_lines = warn_bad_lines
        self.delim_whitespace = delim_whitespace
        self.low_memory = low_memory
        self.memory_map = memory_map
        self.float_precision = float_precision
        self.storage_options = storage_options

        # Creation of dataframe
        self.df = pd.read_csv(filepath_or_buffer= self.path, sep= self.sep,
                                delimiter= self.delimiter, header= self.header, names= self.names,
                                index_col= self.index_col, usecols= self.usecols, squeeze= self.squeeze,
                                prefix= self.prefix, mangle_dupe_cols= self.mangle_dupe_cols,
                                dtype= self.dtype, engine= self.engine, converters= self.converters,
                                true_values= self.true_values, false_values= self.false_values, 
                                skipinitialspace= self.skipinitialspace, skiprows= self.skiprows, 
                                skipfooter= self.skipfooter, nrows= self.nrows, na_values= self.na_values, 
                                keep_default_na= self.keep_default_na, na_filter= self.na_filter, verbose= self.verbose,
                                skip_blank_lines= self.skip_blank_lines, parse_dates= self.parse_dates,
                                infer_datetime_format= self.infer_datetime_format,
                                keep_date_col= self.keep_date_col, date_parser= self.date_parser, dayfirst= self.dayfirst,
                                cache_dates= self.cache_dates, iterator= self.iterator, chunksize= self.chunksize,
                                compression= self.compression, thousands= self.thousands, decimal= self.decimal,
                                lineterminator= self.lineterminator, quotechar = self.quotechar,quoting= self.quoting,
                                doublequote= self.doublequote, escapechar= self.escapechar, comment= self.comment,
                                encoding= self.encoding, dialect= self.dialect, error_bad_lines= self.error_bad_lines, 
                                warn_bad_lines= self.warn_bad_lines, delim_whitespace= self.delim_whitespace, 
                                low_memory= self.low_memory, memory_map= self.memory_map, float_precision= self.float_precision,
                                storage_options= self.storage_options) 

        if wish == True:
            return self.df


    def general_info(self):
        """
                            ---What it does--
        This function creates two dataframe objects to inform the user of all the relevant preliminary information about a dataframe.
        Such as:    1- Shape of the dataframe
                    2- Name and position of columns
                    3- Type of data contained
                    4- Number of NaN values


                            ---What it needs---
        A df object

                            ---What it returns---
        The data report (2 to 4) in dataframe format (report)
        """

        # df columns info
        columns_name = self.df.columns
        rows = self.df.shape[0]
        columns = self.df.shape[1]
        

        shape_df = pd.DataFrame({'Shape': ['Rows', 'Columns'], ' ': [rows, columns]})


        col_data = []
        null_numb = []
        null_per =[]
        for n in range(columns):
            col_data.append(self.df.iloc[:, n].dtype)
            null_numb.append(self.df.iloc[:, n].isnull().sum())
            null_per.append(round((self.df.iloc[:, n].isnull().sum() / rows) * 100, 2))
        

        report = pd.DataFrame({'Columns': columns_name, 'Data type': col_data, 'NaNs in column': null_numb, 
                                'Percentage of NaNs': null_per})

        title = '\t\tGeneral info on the df:'
        sub_title = 'Shape'
        sub_title_2 = 'Data type and NaNs'

        print(title)
        print(sub_title)
        print(shape_df)
        print('-' * len(sub_title_2), '\n')
        print(sub_title_2)
        print(report)
        

        return report


    def value_changer(self, column= None, position= None, change_num= True, copy= True, errors= 'raise', downcast= None):
        """
                                ---What it does---
        This function changes the data type of a given column in a dataframe. Locating it either by name or position.
                                
                                ---What it needs---
            - Either the name or the colum's position.
                * column for name
                * position for the colum's position
            - The choice to change the data to
            - The rest of necessary values are set to default (as they appear in the pandas documentation)
                                
                                ---What it returns---
        This function does not return anything.
        """

        self.column = column
        self.position = position

        self.change_num = change_num
        self.copy = copy
        self.errors = errors
        self.downcast = downcast



        def change_to_num_or_str(self, column= None, position= None, change_num= True):
            """
            TODO
                                ---What it does---
            This function changes the type of the data, from str to numeric or viceversa. By default it will try to change it to numeric.

                                ---What it needs---
                - Location of the data:
                    + Column's name (column). Set as None by default
                    + Position in the column index (column). Set as None by default
                    Choose one or another!
                -Wish to change from string to numeric or viceversa (change_num). Set as True (str -> num) by default
                                
                                ---What it returns--- 
            This function does not return anything           
            """

            self.column = column
            self.position = position

            if change_num == False:
                if column != None:
                    print("\nChanging type using the column's name...")

                    before = self.df[column].dtype
                    self.df[column] = self.df[column].astype(dtype= str, copy= self.copy, errors= self.errors)
                    after = self.df[column].dtype

                    print(f'Changed from {before} to {after}')

                elif position != None:
                    print("\nChanging type using the column's position...")

                    before = self.df.iloc[:, position].dtype
                    self.df.iloc[:, position] = self.df.iloc[:, position].astype(dtype= str, copy= self.copy, errors= self.errors)
                    after = self.df.iloc[:, position].dtype

                    print(f'Changed from {before} to {after}')
            
            else:
                if self.column != None:
                    print("\nChanging type using the column's name...")

                    before = self.df[self.column].dtype
                    self.df[self.column] = pd.to_numeric(self.df[self.column], errors= self.errors)
                    after = self.df[self.column].dtype

                    print(f'Changed from {before} to {after}')

                elif self.position != None:
                    print("\nChanging type using the column's position...")

                    before = self.df.iloc[:, self.position].dtype
                    self.df.iloc[:, self.position] = pd.to_numeric(self.df.iloc[:, self.position], errors= self.errors)
                    after = self.df.iloc[:, self.position].dtype

                    print(f'Changed from {before} to {after}')


        def auxiliary_function (self):
            """
            TODO
                                ---What it does---
            This function acts only if the regular function is unable to change data types.
            In such a case, it finds and drops any data that refuses to co-operate.
            
                                ---What it needs---
                - Column to be checked (self.column)
            
                                ---What it returns---
            This function does not return anything.
            """
            print('Unable to change types. Auxiliary function launched!')
            if self.column != None:
                to_nuke = dict(pd.to_numeric(self.df[self.column], errors='coerce'))
                             
                for e in to_nuke:
                    print (f'- {e}: {to_nuke}\n')
                    # print(f'Deleting {e}')
                    # self.column = self.column.drop(e, axis=1)


            else:
                to_nuke = dict(pd.to_numeric(self.df.iloc[:, self.position], errors='coerce'))
                
                for e in to_nuke:
                    print (f'- {e}: {to_nuke}\n')
                    # print(f'Deleting {e}')
                    # self.column = self.column.drop(e, axis=1)
                
            print('\n... Odd data dropped')
        try:
            change_to_num_or_str(self)
        
        except ValueError as ve:
            print(f'An error occured!{ve}...')
            
            auxiliary_function(self)
            print('Rebooting...')

            change_to_num_or_str(self)
        

    def nan_manager(self, column= None, position= None, drop_na= False, fill_na= False, axis=0, 
                    subset=None, value=None, method=None, limit=None, downcast=None, inplace=True, 
                    how='any'):
        """
                            ---What it does---
        This functions allows the user to either fill or drop NaN values in a dataframe, using the fillna() and dropna() functions of
        the pandas library.

                            ---What it needs---
            - Location of the data:
                * Name of the column (column)
                * Position of the column (position)
                * Almost all the attributes of the fill_na and dropna functions
                    -> TODO implement the thresh= in the function
                    
                            ---What it returns---
        This function does not return anything
        """
        
        self.column = column
        self.position = position
        self.axis = axis
        self.inplace = inplace


        if drop_na == True:
            self.how = how

            print('Dropping data...')

            if column != None:
                print(f"Dropping NaN values by column name\n")
            
                self.df[column].dropna(axis= self.axis, how= self.how, inplace= self.inplace)

            if position != None:
                print(f"Dropping NaN values by position\n")
                
                self.df.iloc[:, position].dropna(axis= self.axis, how= self.how, inplace= self.inplace)

            else:
                self.df.dropna(axis= self.axis, how= self.how, inplace= self.inplace)


        elif fill_na == True:
            self.value = value
            self.value = value
            self.limit = limit
            self.downcast = downcast
            self.method = method

            print('Filling data...')

            if column != None:
                if type(self.value) == int or type(self.value) == float:

                    self.df[column].fillna(value= self.value, method= self.method, 
                                        axis= self.axis, inplace= self.inplace, limit= self.limit,
                                        downcast= self.downcast)
                
                elif type(self.value) == str:
                    values = ['mean', 'std', 'mode']

                    if self.value in values:
                       
                        if self.value == values[0]:
                            self.df[column].fillna(value= self.df[column].mean(), method= self.method, 
                                        axis= self.axis, inplace= self.inplace, limit= self.limit,
                                        downcast= self.downcast)

                        if self.value == values[1]:
                            self.df[column].fillna(value= self.df[column].std(), method= self.method, 
                                        axis= self.axis, inplace= self.inplace, limit= self.limit,
                                        downcast= self.downcast)

                        if self.value == values[2]:
                            self.df[column].fillna(value= self.df[column].mode(), method= self.method, 
                                        axis= self.axis, inplace= self.inplace, limit= self.limit,
                                        downcast= self.downcast)
                    
                    else:
                        self.df[column].fillna(value= self.value, method= self.method, 
                                            axis= self.axis, inplace= self.inplace, limit= self.limit,
                                            downcast= self.downcast)
            
            elif position != None:
                if type(self.value) == int or type(self.value) == float:
                    self.df.iloc[:, position].fillna(value= self.value, method= self.method, 
                                        axis= self.axis, inplace= self.inplace, limit= self.limit,
                                        downcast= self.downcast)
                
                elif type(self.value) == str:
                    methods = ['mean', 'std', 'mode']

                    if self.value in methods:
                        if self.value == methods[0]:
                            self.df.iloc[:, position].fillna(value= self.df.iloc[:, position].mean(), method= self.method, 
                                        axis= self.axis, inplace= self.inplace, limit= self.limit,
                                        downcast= self.downcast)

                        if self.value == methods[1]:
                            self.df.iloc[:, position].fillna(value= self.df.iloc[:, position].std(), method= self.method, 
                                        axis= self.axis, inplace= self.inplace, limit= self.limit,
                                        downcast= self.downcast)

                        if self.value == methods[2]:
                            self.df.iloc[:, position].fillna(value= self.df.iloc[:, position].mode(), method= self.method, 
                                        axis= self.axis, inplace= self.inplace, limit= self.limit,
                                        downcast= self.downcast)
                    
                    else:
                        self.df.iloc[:, position].fillna(value= self.value, method= self.method, 
                                            axis= self.axis, inplace= self.inplace, limit= self.limit,
                                            downcast= self.downcast)
            

    def return_df(self, wish= False, name= None):
        """
                            ---What it does---
        This function rerturs a processed dataframe.

                            ---What it needs---
            - A dataframe (self.dataframe)
            - wish = True saves de dataframe in .csv format in the CURRENT directory
            - sep is equal to self.sep (',' by default)

                            ---What it returns---
        A dataframe (self.df)
        """
                
        # print(self.df)

        if wish == True:
            name = name + '_' + str(date.today()) + '.csv'
            self.df.to_csv(name, sep= self.sep)
        
        return self.df


    def quick_plotter(self, column= None, save_image= False, kind= 'bar'):

        self.column = self.df[column]
        self.save_image =  save_image

        def plot_bar(self):
            """
                                ---What it does---
            Plots a barplot with the variable given. And if desired, saves the plot in the same directory as parent file with "<current date>_barplot.jpg" as name.
                                ---What it needs---
            A df_column, panda series or dictionary with numerical values
                                ---What it returns---
            If desired (save_image != 0), a jpg image file in the same directory using "<current date>_barplot.jpg" as name.
            """

            if is_numeric_dtype(self.column):
                
                if self.column.sum() > 0:
                
                    # Plotting data
                    self.column.plot(kind = 'bar')

                    # Create lables
                    labels = dict(self.column).keys()

                    # Legend and titles
                    plt.legend(labels, loc= 'best')
                    plt.title(self.column.name, loc='center')

                    plt.tight_layout()
                    plt.show()

                    if self.save_image == True:
                        name = str(date.today()) + '_barplot.jpg'
                        plt.savefig(name)
                
                else:
                    print(f'No numeric data to plot')
            
            else:

                # Counting values
                data = self.column.value_counts()
                
                # Plotting data
                data.plot(kind = 'bar')

                # Create lables
                labels = dict(self.column).keys()

                # Legend and titles
                plt.legend(labels, loc= 'best')
                plt.title(self.column.name, loc='center')

                plt.tight_layout()
                plt.show()

                if self.save_image == True:
                    name = str(date.today()) + '_barplot.jpg'
                    plt.savefig(name)


        def plot_line(self):
            """
                                ---What it does---
            Plots a lineplot with the variable given. And if desired, saves the plot in the same directory as parent file with "<current date>_lineplot.jpg" as name.
                                
                                ---What it needs---
            A df_column, panda series or dictionary with numerical values
                                
                                ---What it returns---
            If desired (save_image != 0), a jpg image file in the same directory using "<current date>_lineplot.jpg" as name.
            """

            if is_numeric_dtype(self.column):
                
                if self.column.sum() > 0:
                    
                    # Plotting data
                    self.column.plot()

                    # Create lables
                    labels = dict(self.column).keys()

                    # Legend and titles
                    plt.legend(labels, loc= 'best')
                    plt.title(self.column.name, loc='center')

                    plt.tight_layout()
                    plt.show()

                    if self.save_image == True:
                        name = str(date.today()) + '_lineplot.jpg'
                        plt.savefig(name)
                
                else:
                    print(f'No numeric data to plot')
            
            else:
                # Counting values
                data = self.column.value_counts()
                
                # Create lables
                labels = dict(self.column).keys()

                # Legend and titles
                plt.legend(labels, loc= 'best')
                plt.title(self.column.name, loc='center')

                plt.tight_layout()
                plt.show()

                if self.save_image == True:
                    name = str(date.today()) + '_lineplot.jpg'
                    plt.savefig(name)


        def plot_pie(self):
            """
                                ---What it does---
            Plots a pieplot with the variable given. And if desired, saves the plot in the same directory as parent file with "<current date>_pieplot.jpg" as name.
                                
                                ---What it needs---
            A df_column, panda series or dictionary with numerical values
                                
                                ---What it returns---
            If desired (save_image != 0), a jpg image file in the same directory using "<current date>_pieplot.jpg" as name.
            """

            if is_numeric_dtype(self.column):
                
                if self.column.sum() > 0:
                    # Create lables
                    labels = dict(self.column).keys()

                    # Plotting data
                    plt.pie(self.column, autopct='%1.1f%%', startangle=0, shadow= True, pctdistance = 0.5, labeldistance = 1.2)

                    # Legend and titles
                    plt.legend(labels, loc= 'best')
                    plt.title(self.column.name, loc='center')

                    plt.tight_layout()
                    plt.show()
                    
                    if self.save_image == True:
                        name = str(date.today()) + '_pieplot.jpg'
                        plt.savefig(name)
                else:
                    print ("No numeric data to plot")
            
            else:
                
                # Counting values
                data = self.column.value_counts()
                
                # Create lables
                labels = dict(self.column).keys()

                # Plotting data
                plt.pie(data, autopct='%1.1f%%', startangle=0, shadow= True, pctdistance = 0.5, labeldistance = 1.2)

                # Legend and titles
                plt.legend(labels, loc= 'best')
                plt.title(self.column.name, loc='center')

                plt.tight_layout()
                plt.show()
                
                if self.save_image == True:
                    name = str(date.today()) + '_pieplot.jpg'
                    plt.savefig(name)


        if kind == 'bar' or kind == 'Bar' or kind == 'BAR' :
            plot_bar(self)
        
        elif kind == 'line' or kind == 'Line' or kind == 'LINE' :
            plot_line(self)

        elif kind == 'pie' or kind == 'Pie' or kind == 'PIE' :
            plot_pie(self)


    def correlation_plot(self, matrix_return= False, save_image= False, vmin=None, vmax=None, 
                        cmap=None, center=None, robust=False, 
                        annot=None, fmt='.2g', annot_kws=None, 
                        linewidths=0, linecolor='white', cbar=True, 
                        cbar_kws=None, cbar_ax=None, square=False, 
                        xticklabels='auto', yticklabels='auto', mask=None, 
                        ax=None):
        """
                            ---What it does---
        This function creates a seaborn heatmap graphic based on the correlation matrix for a given dataframe.
        It is capable of saving the image and returning de matrix if desired.

                            ---What it needs---
            - The desire to return the matrix (matrix_return). Set to False by default.
            - The desire to save the image (save_image) in jpg format. Set to False as default.
            - The seaborn.heatmap standard parameters. All set in their default configuration.

                            ---What it returns---
        This function returns the correlation matrix as a dataframe object if desired. And is capable of saving the heatmap as a .jpg
        """
        
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        data = self.df.select_dtypes(include= numerics)
        
        self.corr_matrix = data.corr()

        sns.heatmap(data= self.corr_matrix, vmin= vmin, vmax= vmin, 
                    cmap= cmap, center= center, robust= robust, 
                    annot= annot, fmt= fmt, annot_kws= annot_kws, 
                    linewidths= linewidths, linecolor= linecolor, cbar= cbar, 
                    cbar_kws= cbar_kws, cbar_ax= cbar_ax, square= square, 
                    xticklabels= xticklabels, yticklabels= yticklabels, mask= mask, 
                    ax= ax)
        
        if save_image == True:
            
            name = str(date.today()) + '_heatmap.jpg'
            plt.savefig(name)


        if matrix_return == True:
            return pd.DataFrame(self.corr_matrix)


    def add_to_my_path_dir (self):
        """
                            ---What it does---
        This function adds the libraries current path to your pc path directory.

                            ---What it needs---
            - The sys and os libraries
        
                            ---What it returns---
        This function does not return anything
        """
        CURR_DIR = os.path.dirname(os.path.abspath(__file__))
        print(CURR_DIR)
        sys.path.append(CURR_DIR)
        for path in sys.path:
            print(path)    


    def new_df (self, columns = None, position_1 = None, position_2 = None, axis= 1):
        """
        ---What it does---
        This function slices the dataframe. Either by column name or position.
        ---What it needs---
            - A list of columns to keep in string format (column). Set as None by default
            - Two positions for index:
                + postion_1 is the FIRST position in the interval
                + postion_2 is the SECOND
                Either one or the other may be set as None
            - An axis to filter by (axis). Set as 1 by default

        ---What it returns---
        This function does not return anything
        """
        
        print('Sclicing dataframe...')
        if columns != None:
            self.df = self.df[columns]
        
        elif position_1 != None or position_2 != None:
            if axis == 1:
                if position_1 == None:
                    self.df = self.df.iloc[:, : position_2]

                elif position_2 == None:
                    self.df = self.df.iloc[:, position_1: ]
                
                else:
                    self.df = self.df.iloc[:, position_1: position_2]
            
            else:
                if position_1 == None:
                    self.df = self.df.iloc[:, position_2: ]

                elif position_2 == None:
                    self.df = self.df.iloc[position_1:, : ]
                
                else:
                    self.df == self.df.iloc[position_1: position_2, : ]


    def store_csv(self, name= None, destination= 'Output/'):
        """
                            ---What it does---
        This function stores a .csv file in a given directory.
                            
                            ---What it needs---
            - The name of your dataframe to store into csv (name). It should be in string format
            - The storage directory (destination). It should be in string format.
                * It should ALREADY exist
                * It should be contained within your path directory

                            ---What it returns---
        This funtion does not return anything
        """

        self.name = f'{name}.csv'
        if destination.endswith('/'):
            self.stored_in = f'{destination}{self.name}'
        
        else:
            self.stored_in = f'{destination}/{self.name}'

        print(f'The file will be stored as "{name}"  in {destination}...')
        self.df.to_csv(self.stored_in)