import pandas

df1 = pandas.read_csv('supermarkets.csv')
df2 = pandas.read_json('supermarkets.json')
df3 = pandas.read_excel('supermarkets.xlsx',sheetname=0)
df4 = pandas.read_csv('supermarkets-commas.txt')
df5 = pandas.read_csv('supermarkets-semi-colons.txt',sep=':')

#print(df1.shape)
#print(df1)
#print(df1.set_index(['ID']))

print(df5)
#print(df3)