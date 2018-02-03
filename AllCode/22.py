#init is a special type of function which can be called automatically when object is created

class Name:

    def __init__(self):
        print('init function gets Called')
    def new_name(self):
        print('Another Function gets called')

name = Name()
name.new_name()

class Enemy:
     def __init__(self,x):
         self.energy = x
     def get_energy(self):
         print(self.energy)

enemy1 = Enemy(5)
enemy1.get_energy()


