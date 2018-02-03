# How to Build a Web Crawler

#beautifulsoup4 is the module that let you to go to the website and sort through data

import requests #This is the way to connect to the internet
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://achiredo.com/Blog/'
        source_code = requests.get(url)
        #plain_text = source_code.headers
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text) # This is all the source code from the website

        for link in soup.findAll('div',{'class':'col-xs-9'}):
            for links in link.findAll('h3'):
                for link_link in links.findAll('a'):
                    href= 'http://achiredo.com/Blog/' + str(link_link.get('href'))
                    title = link_link.string
                    #print(href)
                    #print(title)
                    get_single_data(href)

        #print(soup)
        page += 1
def get_single_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('a'):
        hrefs = 'http://achiredo.com/Blog/' + str(item_name.get('href'))
        #string = item_name.string
        print(hrefs)

trade_spider(4)
