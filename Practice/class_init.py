#Classes and Objects
#self means use something from its own class
#init is a special type of function which can be called when object is created

class Name:
    def __init__(self):
        print('init Function Called')
    def sec(self):
        print('It\'s  Time')

name  = Name()
name.sec()

class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)


enemy1 = Enemy(5)
enemy1.get_energy()