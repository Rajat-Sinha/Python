#Inheritance is basically getting something from someone else
#() after classname as for name of the class you want to inherit

class Parents():
    def print_last_name(self):
        print('Sinha')

class Child(Parents):
    def print_first_name(self):
        print('Rajat')
    '''def print_last_name(self):
        print('Singh')'''

parents = Parents()
parents.print_last_name()
#parents.print_first_name() shows an error as Parents class doesnot inherit the property of child class

child = Child()
child.print_first_name()
child.print_last_name() #does not shows an error as Child class  inherit the property of Parents class

