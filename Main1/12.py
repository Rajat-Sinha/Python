#Unpacking arguments

def health_calculator(age,apples_ate,cigs_smoked):
    answer = (100 - age) + (apples_ate * 3.5) - (cigs_smoked * 2)
    print(answer)

data = [19, 10, 6]
health_calculator(data[0],data[1],data[2])
health_calculator(*data) #This is the Unpacking of arguments