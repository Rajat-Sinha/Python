#Classes and Instance variables

class Girl:
    gender = 'Female' #Class Variables
    def __init__(self, name):
        self.name = name #Instance Varibles

r = Girl('Nili')
s = Girl('Rashi')

print(r.gender) # for accessing the class variables
print(r.name) # for accessing the instance variables
print(s.gender) # for accessing the class variables
print(s.name) # for accessing the instance variables


