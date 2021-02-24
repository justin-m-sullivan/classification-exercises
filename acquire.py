import pandas as pd
import numpy as np
import os

from env import host, password, user

def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the CodeUp db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

########### Aquire Titanic Data ###########

def get_titanic_data():
    '''
    This function reads in titanic data from Codeup database and writes data to
    a csv file if cached == False or if cached == True reads in titanic df from
    a csv file, returns df.
    '''
    filename = 'titanic.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # Read fresh data from db into a DataFrame.
        df = pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))
        
        # Write DataFrame to a csv file.
        df.to_csv(filename)
          
    return df

 

def get_iris_data():
    '''
    This function reads in iris data from Codeup database and writes data to
    a csv file if cached == False or if cached == True reads in iris df from
    a csv file, returns df
    '''

    filename = 'iris.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        
        # Read fresh data from db into a DataFrame. Joins species id on dataframe. 
        df = pd.read_sql('''
    SELECT * FROM measurements as m
    JOIN species ON m.`species_id`
    ''', get_connection('iris_db'))
        
        # Write DataFrame to a csv file.
        df.to_csv(filename)
          
    return df