# DATA HUNTER

# Libraries
import webbrowser
from pathlib import Path
import pandas as pd
import sys, os

helpful_reminder = ("""
                        ---POURPOSE---
This library is aimed towards the extraction of csvs from different sources. Also it includes the webbbrowser function for visualization of urls in new browser tabs.

                        ---IT USES---
    - pandas as pd
    - webbrowser
    - Path from pathlib
    - sys, os
""")


def add_to_my_path_dir ():
    """
    TODO
                        ---What it does---
    This function adds the libraries current path to your pc path directory.

                        ---What it needs---
    - 
    
                        ---What it returns---
    This function does not return anything
    """
    CURR_DIR = os.path.dirname(os.path.abspath(__file__))
    print(CURR_DIR)
    sys.path.append(CURR_DIR)
    for path in sys.path:
        print(path)


def open_a_tab (url, browser):
    """
                        ---What it does---
    Reads an url and opens a new tab in your browser of choice. This function preassumes that your browser of choice is installed in C:
    
    This function currently supports:
        - OPERA
        - CHROME
        - MOZILLA FIREFOX

                        ---What it needs---
        - The webbrowser library
        - A url to search. MUST be in string format.
    """
    browser_dict = {'chrome': ['Chrome', 'chrome', 'Google Chrome', 'Google', 'google'], 'opera': ['Opera', 'opera'], 'mozilla': ['Firefox', 'firefox', 'Mozilla firefox', 'Mozilla', 'mozilla']}

    if type(url) != 'str':
        print("You didn't do it the correct way! I'll try to convert it for you")
        url = str(url)
    
    if browser in browser_dict['chrome']:
        browser = 'Google/Chrome/Application/chrome.exe %s'
    
    elif browser in browser_dict['opera']:
        browser = '/AppData/Local/Programs/Opera %s'
    
    elif browser in browser_dict['mozilla']:
        browser = 'Program Files/Mozilla Firefox/ %s'
    

    webbrowser.get(browser)
    webbrowser.open(url)


def df_url_opener (url, sep= ','):
    """
                        ---What it does---
    This function opens a dataframe in python and returns it for further use.

                        ---What it needs---
        - The url of the destination file (url). It SHOULD be a string.
        - The separator (sep). By default equals ','.
                        
                        ---What it returns--- 
    The file to be openend (dataframe)
    """

    dataframe = pd.read_csv(url, sep = sep)

    return dataframe


def csv_opener_from_path (path, sep= ','):
    """
                        ---What it does--
    This function opens a file in python from a given directory of your computer.

                        ---What it needs---
        - The path to the file (path) with the filename and extension. Must be a string
            E g. D:\\csvs\\titanic.csv
        - The csv separator. Must be string. By default set as sep= ','

    ---What it returns---
    The opened file (file)
    """
    path_to_file = Path(__file__).parent / path

    with path_to_file.open() as f:
        csv = pd.read_csv(f, sep= sep)
    
    return csv


print('Library ready!')