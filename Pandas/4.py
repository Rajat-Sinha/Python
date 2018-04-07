import pandas
df = pandas.read_csv('supermarkets.csv')
df = df.set_index('ID')
print(df)
df1 = df.loc[1,'Address':'State']
#print(df1)
df2 = df.iloc[1,2:3]
#print(df2)
df3 = df.ix[2,'Name']
#print(df3)

df4 = df.drop('City',1)
df5 = df4.drop('Address',1)
df6 = df5.drop(3,0)
#print(df6)

df7 = df4.drop(df4.index[0:3],0)
df8 = df7.drop(df7.columns[0:3],1)
print(df8)

