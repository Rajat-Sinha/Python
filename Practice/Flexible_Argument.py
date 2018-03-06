#Flexible Number of Arguments

def add_numbers(*args):
    total= 0
    for a in args:
        total = total + a

    print(total)

add_numbers(2,4,5,6)
add_numbers(2,4)