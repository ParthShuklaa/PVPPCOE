import pandas as pd
import numpy as np
df = pd.read_csv('netflix_titles_nov_2019.csv')

print(df['release_year'])
#Extracting Col from DataFrame
col  = np.array(df['release_year'])
#Process/Compute NumpyArray
#print(list(df))
col[col<2018] = np.average(col)
#updating DATFRAME

df['release_year'] = col
print(df['release_year'])

