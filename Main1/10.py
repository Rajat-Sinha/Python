# Keyword Argument

def dumb_sentence(name = 'Rajat',action = 'ate',item = 'tuna'):
    print(name,action,item)

dumb_sentence()
dumb_sentence('Raj','farts','gently')
dumb_sentence(item = 'awesome')
dumb_sentence(item = 'awesome',action = 'feels')
