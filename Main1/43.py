#find the largest and smallest number

import heapq

grades = [23,543,43,12,33,64,765,76,78,98,90]
print(heapq.nlargest(1, grades))
print(heapq.nsmallest(1, grades))

stocks = [
    {'tickr':'GOOG','price':230},
    {'tickr':'AMZN','price':330},
    {'tickr':'MICRO','price':970},
    {'tickr':'FB','price':30}
]
print(heapq.nsmallest(2,stocks,key=lambda stock:stocks['price']))

