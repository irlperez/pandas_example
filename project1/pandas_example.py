import pandas as pd
from pathlib import Path
import os

# load data first
directory = './data_sets'
dfs = []
for file in Path(directory).glob('**/*.csv'):
    dfs.append(pd.read_csv(file))

df = pd.concat(dfs)
print(df.columns)
df.drop()
print(df.columns)

# drop column
# adding extra column (concat first and last)
# patition data
# save data

# https://pandas.pydata.org/docs/user_guide/dsintro.html#dataframe
# https://pandas.pydata.org/docs/user_guide/index.html