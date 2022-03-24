import pandas as pd
from search import isWordPresent

df = pd.read_csv('clean_data.csv')

print(df.index)

for ind in df.index:
    if df['title'][ind] == 'title':
        df.drop(ind, inplace=True)

print(df)
df.to_csv('clean_data.csv', index=False)