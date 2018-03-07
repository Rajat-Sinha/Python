#Word Frequency Counter
import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    response  = requests.get(url)
    source_code = response.text
    soup = BeautifulSoup(source_code)
    for post_text in soup.findAll('div'):
        content = post_text.text
        word = content.lower().split()
        for each_word in word:
            word_list.append(each_word)
    clean_up_list(word_list)

def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "~!@#$%^&*()`1234567890_+{}|:\"<>?-=[]\;',./'"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i],'')
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)


def create_dictionary(list):
    word_count = {}
    for word in list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for k,v in sorted(word_count.items(), key=operator.itemgetter(0)):
        print(k,v)
start('http://localhost/Achiredo/Achiredo%20Website/FAQ.html')
