import json
from difflib import get_close_matches


file = open('data.json')
data = json.load(file)

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input('Did You mean %s instead ! Enter Y if yes,N if no: '% get_close_matches(w,data.keys())[0])
        yn = yn.lower()
        if yn == 'y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == 'n':
            return 'The Word Doesn\'t exists.Please Double Check it'
        else:
            return 'We didn\'t understand your entry'
    else:
        return 'The Word Doesn\'t exists.Please Double Check it'

word = str(input('Enter Word: '))
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
