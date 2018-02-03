#Multiple Inheritance

class First():
    def move(self):
        print('First Move')

class Second():
    def run(self):
        print('Second Run')
class Third(First, Second):
    #this class cannot be vacant it must have something
    pass #this keyword is used to keep class vacant

third = Third()
third.move()
third.run()