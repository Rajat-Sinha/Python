#Dictionary Multiple Key Sort
from operator import itemgetter

users = [
    {'fname' : 'Rajat','lname' : 'Sinha'},
    {'fname' : 'Rajat','lname' : 'Singh'},
    {'fname' : 'Rahul','lname' : 'Raj'},
    {'fname' : 'Tina','lname' : 'Kiwi'}
]

for x in sorted(users, key=itemgetter('fname')):
    print(x)

print('------')

for x in sorted(users, key=itemgetter('fname','lname')):
    print(x)
