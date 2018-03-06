#Sets is a list of item where itr cannot have duplicates WHEREAS a list can have duplicates


groceries = {'a','r','A','t','u','P','a'}
print(groceries)

var = 'r'

if var in groceries:
    print(var,' already exists')
else:
    print(var, ' need to be added')

data = [4,1,2,4,5,6,4,3,2,4,5,6]
print(list(set(data)))



