import pandas
df1 = pandas.read_json('supermarkets.json')
df1 = df1.set_index('ID')
df2 = df1.loc[1,'Country':'Name']
df3 = df1.loc[:,'Name']
df4 = list(df1.loc[:,'Name'])
df5 = df1.iloc[1:3,1:3]
df6 = df1.iloc[3,:]
df7 = df1.iloc[3,1:4]
df8 = df1.ix[3,'Name']
print(df8)
print(df6)
print(df7)
print(df3)
print(df4)
