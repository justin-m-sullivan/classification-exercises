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

def prep_iris(df):
    '''
    prep_iris takes in the iris data set and prepares it for analysis by:
    dropping columns: measurement_id, species_id
    renaming columns: species_name == species
    encoding columns: species
    '''
    dropcols = ['species_id', 'measurement_id']
    df.drop(columns=dropcols, inplace=True)
    df.rename(columns={'species_name': 'species'}, inplace=True)
    dummies = pd.get_dummies(df[['species']], drop_first=True)
    return pd.concat([df, dummies], axis=1)
    


prep_iris(df)