#Unpack List or tuples

name,branch,interest = ['Rajat','MME','Core'] #number of variables must be euqaul to the values
print(name)
print(branch)
print(interest)

def drop_first_last(grades):
    first,*middle,last = grades
    avg = sum(middle) / len(middle)
    print(avg)
drop_first_last([1,2,3])
