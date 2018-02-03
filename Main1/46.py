#Sorting Custom Object

from operator import attrgetter

class User:

    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    def __repr__(self):
        return self.name + ':' + str(self.user_id)

users = [
    User('Rajat',45),
    User('Raj',42),
    User('Rati',43),
]

for x in users:
    print(x)

print('-----')

for x in sorted(users, key=attrgetter('name')):
    print(x)