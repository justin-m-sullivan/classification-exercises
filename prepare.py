import pandas as pd
import numpy as np
import os
import acquire
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# visualize
import seaborn as sns
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(11, 9))
plt.rc('font', size=13)

# turn off pink warning boxes
import warnings
warnings.filterwarnings("ignore")

# acquire
from env import host, user, password
from pydataset import data

########## Prepare Iris ##########

df = acquire.get_iris_data()

def clean_iris(df):
    '''
    clean_iris takes in the iris data set and prepares it for analysis by:
    dropping columns: measurement_id, species_id
    renaming columns: species_name == species
    encoding columns: species
    '''
    dropcols = ['species_id', 'measurement_id', 'Unnamed: 0', 'species_id.1']
    df.drop(columns=dropcols, inplace=True)
    df.rename(columns={'species_name': 'species'}, inplace=True)
    dummies = pd.get_dummies(df[['species']])
    return pd.concat([df, dummies], axis=1)

def prep_iris(df):
    '''
    prep_iris takes in the iris data set and prepares it for analysis by:
    dropping columns: measurement_id, species_id
    renaming columns: species_name == species
    encoding columns: species
    
    performs a train, validate, and test split 
    return three pandas dataframes for train, validate, split
    '''
    df = clean_iris(df)
    train_validate, test = train_test_split(df, test_size=0.2, random_state=1776, stratify=df.species)
    train, validate = train_test_split(train_validate, train_size=0.7, random_state=1776, stratify=train_validate.species)
    return train, validate, test

def split(df, stratify_by=None):
    """
    Crude train, validate, test split
    To stratify, send in a column name
    """
    
    if stratify_by == None:
        train, test = train_test_split(df, test_size=.3, random_state=123)
        train, validate = train_test_split(df, test_size=.3, random_state=123)
    else:
        train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[stratify_by])
        train, validate = train_test_split(df, test_size=.3, random_state=123, stratify=train[stratify_by])
    
    return train, validate, test

