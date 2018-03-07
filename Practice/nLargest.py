#For finding the largest and smallest number
import heapq
grades = [2,3,45,12,23,13,56,76,54,87,64,32]
print(heapq.nlargest(2,grades))# print the first two largest number
print(heapq.nsmallest(2,grades))

