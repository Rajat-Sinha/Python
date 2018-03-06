#Inheritance is basiclly getting something from someone else
#() after the class name as which class you wants to inherit

class Parents:
    def print_last_name(self):
        print('Sinha')

class Child(Parents):
    def print_first_name(self):
        print('Rajat')

p = Parents()
p.print_last_name()
#parents.print_first_name() shows an error as Parents class doesnot inherit the property of child class


c= Child()
c.print_first_name()
c.print_last_name() #does not shows an error as Child class  inherit the property of Parents class
