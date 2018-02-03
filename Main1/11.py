#Flexcible number of arguments

def add_number(*args):
    total = 0
    for a in args:
        total+=a
    print(total)

add_number(3,4)
add_number(3)
add_number(3,4,5,3,6,7)
