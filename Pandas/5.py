import pandas
df = pandas.read_csv('supermarkets.csv')
df = df.drop('City',1)
df = df.drop('Address',1)
#Adding New Columns
df['Access'] = [0,1,2,3,4,5]
df['Continent'] = df.shape[0]*['Asia']

#Changing row into columns
df = df.T
#Adding New Columns to transpose
df[6] = df.shape[0]*['Cool']
df = df.T
print(df)
