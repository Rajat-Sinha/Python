#Unpack List or Tuples

'''
date,name,price = ['Dec 21 2017','Bread Souce',21.4] # number of varibales must  be equal to number of items
print(date)
print(name)
print(price)

'''


def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)


drop_first_last([1,2,3])