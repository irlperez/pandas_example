import pandas as pd
from pathlib import Path
import os

# load data first
directory = './data_sets' 
df_list = []

for file in Path(directory).glob('**/*.csv'):
    df_temp = pd.read_csv(file)
    df_list.append(df_temp)

df = pd.concat(df_list)
print(df.head())

# drop column
df = df.drop(['phone'], axis='columns')
print(df.head())

# adding extra column (concat first and last)
df['last, first'] = df['last_name'] + ', ' + df['first_name']
print(df.head())

# partition data and save data
print(df.loc[df['age'] == 24])

for age in df['age'].unique():
    Path(f'./pd_partitioned_data/age={age}').mkdir(parents=True, exist_ok=True)
    age_df = df.loc[df['age'] == age]
    age_df.to_csv(f'./pd_partitioned_data/age={age}/data', header=True)

df.to_parquet('./pd_partitioned_data/df.parquet', partition_cols='age', engine='auto') # this is really cool!

# https://pandas.pydata.org/docs/user_guide/dsintro.html#dataframe
# https://pandas.pydata.org/docs/user_guide/index.html