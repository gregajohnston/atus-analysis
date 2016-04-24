import pandas as pd
from pandas import DataFrame, Series
# import numpy as np
# import matplotlib as plt


def importer():
    return pd.read_csv('atus_analysis/atussum_2014.dat', nrows=20, header=0)


"""
df.head()
list(df.columns.values)
df['t010101'].head(10)
print(df.describe())
print(df.corr())

"""
