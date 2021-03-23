# Needed for stablishing connection with database and queries
import json
import pymysql
import psycopg2
from sqlalchemy import create_engine
import sys

# For data export as csv and/or dataframe
import pandas as pd

class General_SQL (object):
    def __init__(self, path):
        self.path = path


    # For reading config files
    def read_config(self):
        """
                            ---What it does---
        Loads a json file and turns it into a dictionary.
                            
                            ---What it needs---
            - The path to the file (path) in string format
        
                            ---What it returns---
        A dictionary (settings) with the contents of the json loaded
        """
        try:
            with open(self.path, 'r+') as outfile:
                self.settings = json.load(outfile)
                              
                return self.settings
            
        except Exception as error:
            raise ValueError(error)


    # For connecting your Database
    def CREATE_a_MySQL_db(self):
        """
                            ---What it does---
        This function creates a MySQL database for use in a Python enviroment.
        Using a json file to connect to a MySQL server stored in AWS. 
                            
                            ---What it needs---
            - MySQL library for Python
            - A path to the settings (path) in string format
                + The settings file should be a json file
                            
                            ---What it returns---
        This function returns a MySQL database ready for connection
        """

        try:             
            self.settings = self.settings['MySQL']

            IP_DNS = self.settings["IP_DNS"]
            USER = self.settings["USER"]
            PASSWORD = self.settings["PASSWORD"]
            DATABASE = self.settings["DB_NAME"]
            PORT = self.settings["PORT"]

            self.connection = pymysql.connect(host= IP_DNS, user= USER, 
                                    password= PASSWORD, database= DATABASE, 
                                    port= PORT)
            
            self.cursor = self.connection.cursor()
                     
            print(f"Connected to MySQL server {DATABASE}")
                                            
            return self.connection, self.cursor
       
        except Exception as error:
            raise ValueError(error)        
    
    
    def CREATE_a_postgre_db (self):
        """
                            ---What it does---
        This function creates a postgre SQL database connection with Python.

                            ---What it needs---
            - This function needs access to a json with the connection settings (self.path)

                            ---What it returns---
        This function returns the cursor object.
        """
                
        try:
            self.settings = self.settings['Postgre_SQL']

            localhost = self.settings['HOST']
            user = self.settings['USER']
            password = self.settings['PASSWORD']
            dbname = self.settings['DB_NAME']
            self.schema = self.settings['SCHEMA']

            try:
                self.connection = psycopg2.connect(f"host={localhost} dbname= {dbname} user= {user} password= {password}")   
                self.cursor =  self.connection.cursor()

                print(f'Succesfull connection to {dbname}, in schema {self.schema}')

            except psycopg2.DatabaseError:
                if self.connection:
                    self.connection.rollback()
                
                print ('Error %s' % psycopg2.DatabaseError)  
                sys.exit(1)
                        
        except Exception as error:
            raise ValueError(error)


    # General queries
    def ORDER_custom_query(self, query, wish= False):
        """
                            ---What it does---
        This function executes a custom query. Then prints it.

                            ---What it needs---
            - A query in string format and in the proper sintax
            - A boolean value (wish) if you wish to return the query in dataframe format.

                            ---What it returns---
        This function does not return anything
        """
        
        print(f'{query}\n')
        table =  pd.read_sql(query, con= self.connection)
        print(table)

        if wish == True:
            print('Returning your query')

            return table


    def ORDER_select_all_from (self, table):
        """
                            ---What it does---
        This function prints all available data in dataframe format.
        
                            ---What it needs---
            - The name of the (table)
            
                            ---What it returns---
        This function does not return anything
        """

        query = f'SELECT * FROM {table}'
        
        print(f'{query}\n')
        table =  pd.read_sql(query, con= self.connection)

        print(table)


    def ORDER_create_a_df_from_sql(self, query= None, return_file= True, store= False, name= 'my_file', destination='Output/'):
        """
                            ---What it does---
        Creates a dataframe from a given sql table and returns it and/or saves it locally.
        This table must be generated through a MySQL query.

                            ---What it needs---
            - A valid SQL query (query). It should be in string format.
            - A boolean value
            - A boolean value (store) if you wish to save the dataframe in csv format locally. Set to False by default.
            - The name of the file to save (name) it should be in string format. Set to 'my_file' by default.
            - The directory to be saved in (destination). It should be in string format end with '/'. Set as 'Output/' by default.
        
                            ---What it returns---
        This function returns a dataframe object
        """
        print(f'{query}\n')
        self.df = pd.read_sql(query, con= self.connection)

        if return_file == True and store == False:
    
            return self.df
        
        elif return_file == True and store == True:
            self.name = f'{name}.csv'

            if destination.endswith('/'):
                self.stored_in = f'{destination}{self.name}'
            
            else:
                self.stored_in = f'{destination}/{self.name}'

            print(f'The file will be stored as "{name}"  in {destination}...')
            self.df.to_csv(self.stored_in)

            return self.df


    def ORDER_join_tables (self, table, table_2, on, selection= '*', how= 'inner'):
        """
                            ---What it does---
        Joins the selected tables in your database on the column of your choice, selection and method.

                            ---What it needs---
            - Names of your tables (table, table_2) in  string format.
            - The column to join on (on) in string format.
            - Your selection (selection), by default set to '*'.
            - The method of join (how), by default set to 'inner'.
        """
        if how == 'left' or how == 'LEFT':
            query = f"""SELECT {selection} 
                FROM {table} 
                LEFT JOIN {table_2} ON {on};"""
        
        elif how == 'right' or how == 'RIGHT':
            query = f"""SELECT {selection} 
                FROM {table} 
                RIGHT JOIN {table_2} ON {on};"""

        elif how == 'inner' or how == 'INNER':
            query = f"""SELECT {selection} 
                FROM {table} 
                INNER JOIN {table_2} ON {on};"""

        elif how == 'full' or how == 'FULL':
            query = f"""SELECT {selection} FROM {table}
                    LEFT JOIN {table_2} ON {on}
                    UNION
                    SELECT {selection} FROM {table_2}
                    LEFT JOIN {table} ON {on}"""

        print(f'{query}\n')
        self.cursor.execute(query)
        

    # For closing your db
    def ORDER_close(self):
        """
                                ---What it does---
        Closes conection with your database
        """

        print(f"Closing connection connection with SQL server...")
        self.cursor.close()
        self.connection.close()




class MySQL_manager(General_SQL):
    """
    This class has been created to establish a connection with a MySQL server database. For this it uses:
        
        - The json library
        - The pymysql library
        - The slalchemy/create_engine library
        - The pandas library

    This class can make queries in MySQL and return the results as a dataframe for further exploration.
    """
    def __init__(self, path):
        self.path = path




    # Quick oders for your database
    def ORDER_show_tables (self):
        """
                            ---What it does---
        Shows the tables in your database
        """
        query = "SHOW TABLES"
        
        print(f'{query}\n')
        result = self.cursor.execute(query)
        tables = self.cursor.fetchall()
        table_list = [table for table in tables]

        self.table_dict = {}

        for item in range(result):
            self.table_dict[item] = table_list[item][0]
            print(f'{item}: {self.table_dict[item]}')

        return self.table_dict


    def ORDER_describe_table (self, table):
        """
                            ---What it does---
        Describes a table in your database
        """
        query = f"DESCRIBE {table}"

        print(f'{query}\n')
        self.cursor.execute(query)
        data = [detail for detail in self.cursor.fetchall()]

        name = []
        d_type = []
        default_v = []
        nullable = []
        prim_k = []
        collation =[]

        for d in data:
            name.append(d[0])
            d_type.append(d[1])
            nullable.append(d[2])
            prim_k.append(d[3])
            default_v.append(d[4])
            collation.append(d[5])

        self.table_data = pd.DataFrame({'name': name, 'data_type': d_type, 'nullable': nullable,
                                        'primary_key': prim_k, 'default_value': default_v, 'collation': collation})
        print(self.table_data)
    

    def ORDER_drop_if_already_exists (self, table):
        """
                            ---What it does---
        Drops the table in your database if it already exists
                            ---What it needs---
            - Name of your table (table). 
        """
        query = f"""
                 DROP TABLE IF EXISTS {table}"
                 """

        print(f'{query}\n')
        self.cursor.execute()


    def ORDER_insert_into_table(self, table, columns, values):
        """
                            ---What it does---
        This function adds data to a given table using MySQL INSERT INTO statement, printing the query.
        
        ---What it needs---
            - The name of the (table)
            - The columns of the table (columns). It should be in string format.
                * In this format -> "(col_1, col_2)"
            - The values to insert. It should be in string format.
                * In this way -> "(val_1, val_2), (val_3, val_4);"
            BOTH table and values MUST coincide in order!

        ---What it returns---
        This function does not return anything
        """
        
        query = f"INSERT INTO {table} {columns} VALUES {values};"
        print(f'{query}\n')

        self.cursor.execute(query)


    def ORDER_load_data_infile(self, dataframe, table, delimiter= ',', new_line= '\\r\\n'):
        """
                            ---What it does---
        This function executes the LOAD DATA INFILE query. Allowing the user to review it as a safeguard before execution.
        
                            ---What it needs---
            - A dataframe to load into (dataframe)
            - A table to load the data in
            Needless to say, both need to coincide in both number and name of columns

                            ---What it returns---
        This function does not return anything
        """
        
        query = (f"""
            LOAD DATA LOCAL INFILE 
            INTO TABLE {table} 
            COLUMNS TERMINATED BY {delimiter} 
            LINES TERMINATED BY {new_line}
            IGNORE 1 LINES
            {tuple(dataframe.columns)}
            ;""")
        
        print(f'{query}\n')

        choice = input('Do you wish to execute? y/n> ')

        if choice == 'y' or choice == 'Y':
            print('Executing query')
            self.cursor.execute(query)
        
        else:
            print('Quitting')



class PostgreSQL_manager(General_SQL):
    """
    This class has been created to establish a connection with a Postgre SQL database. For this it uses:
        
        - The json library
        - The psycopg2 library
        - The slalchemy/create_engine library
        - The pandas library
        - The MySQL_manager (parent class)

    This class can make queries in Postgre SQL and return the results as a dataframe for further exploration.
    """

    def __init__(self, path):
        self.path = path


    def ORDER_show_tables (self):
        """
                            ---What it does---
        This function shows the tables present in a postgre SQL database, then creates a dictionary with all table names.

                            ---What it needs---
            - The self.schema attiribute. It must be present in the config file!

                            ---What it returns---
        This fucntion returns a dictionary
        """

        query = f"""
                SELECT *
                FROM pg_catalog.pg_tables
                WHERE schemaname = '{self.schema}'
                """
        print(f'{query}\n')
        table =  pd.read_sql(query, con= self.connection)
        print(table)

        return dict(table['tablename'])


    def ORDER_join_tables(self, how= None, select= '*', table_1= None, table_2= None, col_1= None, col_2= None, wish= False):
        """
                            ---What it does---
        This function joins two given SQL tables. Using the usual (INNER, RIGHT, LEFT... etc.) SQL commands.
        And if you wish it, it returns a dataframe object.

                            ---What it needs---
            - A join method (how). Must be string and properly spelled SQL values.
            - A selection of data to print/return (select). Set as '*' by default.
            - Your first table (table_1). Must be a table present in your schema.
            - Your second table (table_2). Must be a table present in your schema.
            - A column to join by present in table_1 (col_1). Must be string and exist in your table.
            - A column to join by present in table_2 (col_2). Must be string and exist in your table.
            - If you wish to return the data (wish). Set to False by default. Must be a boolean.
            
                            ---What it returns---
        This fucntion returns the queried data if desired.
        """

        if how == 'left' or how == 'LEFT':
            method = "LEFT JOIN"
        
        elif how == 'right' or how == 'RIGHT':
            method = "RIGHT JOIN"

        elif how == 'full' or how == 'FULL':
            method = 'FULL OUTER JOIN'

        elif how == 'inner' or how == 'INNER':
            method = 'INNER JOIN'

        query = f"""
                SELECT {select}
                FROM "{self.schema}".{table_1} {method} "{self.schema}".{table_2} ON ({table_1}.{col_1} = {table_2}.{col_2});
                """
        
        print(f'{query}\n')
        result = pd.read_sql(query, con= self.connection)
        print(result)

        return result


    def ORDER_describe_table(self, table= None):
        """
                            ---What it does---
        This function describes the data types present in your table.

                            ---What it needs---
            - The table to describe (table). Must be present in the schema. Must be string.
            
                            ---What it returns---
        This fucntion returns nothing
        """        
        
        query = f"""
                SELECT table_name, column_name, data_type   
                FROM information_schema.columns 
                WHERE table_name = '{table}';
                """

        print(f'{query}\n')
        result = pd.read_sql(query, con= self.connection)
        print(result)

