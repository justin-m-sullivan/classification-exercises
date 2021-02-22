import pandas as pd
import numpy as np

from env import host, password, user

def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the CodeUp db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_titanic_data():
    '''
    This function reads in the titanic data from the CodeUp db
    and returns a pandas DF with all columns
    '''
    sql_query = 'SELECT * FROM passengers'
    return pd.read_sql(sql_query, get_connection('titanic_db'))

    