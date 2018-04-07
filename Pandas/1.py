import pandas

#from List
df = pandas.DataFrame([[1, 2,3], [30, 40,50]]  ,columns=['age','value','number'],index=['first','second'])
print(df)


#from dict
df1 = pandas.DataFrame([{"Name":"Rajat"},{"Name":"Varun"}])
print(df1)

#mean of column
print(df.mean())

#mean of entire dataframe
print(df.mean().mean())

df3 = pandas.read_csv('supermarkets.csv')
print(df3)