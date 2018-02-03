#variable scope

a = 745

def corn():
    b = 65
    print(a)
    print(b)

def fudge():
    print(a)
    #print(b) shows an error

corn()
fudge()