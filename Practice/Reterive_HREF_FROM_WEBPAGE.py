import requests
from bs4 import BeautifulSoup

def get_single_data(url):
    source_code = requests.get(url)
    source_code_text = source_code.text
    soup = BeautifulSoup(source_code_text)
    for link in soup.findAll('a'):
        href = 'http://achiredo.com/' + str(link.get('href'))
        print(href)

url = 'http://achiredo.com/'
source_code = requests.get(url)
source_code_text  = source_code.text # gives the source code in terminal
soup = BeautifulSoup(source_code_text) #gives the full Source Code and can be used to get the values from the code
for links in soup.findAll('a'):
    href = 'http://achiredo.com/' + str(links.get('href'))
    title = links.string
    print(href)
    get_single_data(href)

