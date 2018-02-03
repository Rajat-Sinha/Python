#map

income = [10,20,30]

def dollar_money(dollars):
    return dollars * 72.6

#map function takes two parameter 1st one is the what is the function you want to run and 2nd one is list
new_income = list(map(dollar_money, income))
print(new_income)
