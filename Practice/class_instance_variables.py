#Class and Instance Variable
class Girl:
    gender = 'Female' #Class Variable
    def __init__(self,name):
        self.name = name #instance variable

r = Girl('Sexy')

print(r.gender)
print(r.name)