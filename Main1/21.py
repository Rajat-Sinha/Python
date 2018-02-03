#Classes and Object
#self means use something from its own class

class Enemy:
    life = 3
    def attack(self):
        print('Ouch!')
        self.life -= 1
    def checkLife(self):
        if self.life <= 0:
            print('Uff! I am dead')
        else:
            print(str(self.life) + ' Life Left!')

#Object Created to access the function or the variable from the Enemy Class
enemy1 = Enemy()
enemy1.attack()
enemy1.checkLife()
