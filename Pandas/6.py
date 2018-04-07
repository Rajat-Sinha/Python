#GeoCoding Addrsss with pandas
import pandas
from geopy.geocoders import Nominatim

nom = Nominatim()

df = pandas.read_csv('supermarkets.csv')
df =df.drop('Employees',1)
df['Address'] = df['Address']+','+df['City']+','+df['State']+','+df['Country']
df['Coordinates'] = df['Address'].apply(nom.geocode)
df['latitude'] = df['Coordinates'].apply(lambda x:x.latitude if x != None else None)
print(df)