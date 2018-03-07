#map

income = [10,20,30]
def dollar_money(dollars):
    return dollars * 72.1

'''
map takes two parameter
1st is what function you want to run
2nd is lis
map(function_name,list_name)
We cannot directly print the map object 
for printing it we have to convert it into list or set
'''

#new_income = map(dollar_money, income) #cannot run as it prints the map object
#new_income = list(map(dollar_money, income))
new_income = set(map(dollar_money, income))
print(new_income)
