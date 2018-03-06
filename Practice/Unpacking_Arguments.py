#Unpacking arbuments
def health_calculator(age,apple_ate,smoked_cig):
    answer = (100 - age) + (apple_ate * 3.5) - (smoked_cig * 2)
    print(answer)

data = [21,2,5]
health_calculator(data[0],data[1],data[2])
health_calculator(*data) #This is Unpacking of arguments