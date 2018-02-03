#Word Frequency Counter

import requests #This is used to connect url to the internet
from bs4 import BeautifulSoup # this is for extracting information from the webpages
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for post_text in soup.findAll('div',{'class','panel-body'}):
        content = post_text.text
        word = content.lower().split() # lower() is used to convert into lowercase
        for each_word in word:
            word_list.append(each_word)
    clean_up_list(word_list)

def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "~!@#$%^&*()_+{}|:\"<>?`-=[]\;',./1234567890"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)

def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key = operator.itemgetter(0)):
        print(key, value)



start('http://localhost/Achiredo/Achiredo%20Website/FAQ.html')