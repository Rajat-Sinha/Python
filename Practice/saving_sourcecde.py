import requests
import urllib
from urllib import request
from bs4 import BeautifulSoup

url = 'http://achiredo.com/Blog/'
source_code = requests.get(url)
source_code_header = source_code.headers
#print(source_code_header)
source_code_text  = source_code.text # gives the source code in terminal
soup = BeautifulSoup(source_code_text) #gives the full Source Code
print(soup)


#code = request.urlopen(url).read() #gives source code in a bad way
#print(code)

#ancode = request.urlretrieve(url,'x.txt') # saves the source code in new file
