#!/bin/python3

import sys

def diagonalDifference(a):
    sum1 = 0
    sum2 = 0
    a_len = len(a)
    for x in range(len(a)):
        for y in range(len(a)):
            if x == y:
                sum1 = sum1 + int(a[x][y])
            if (x+y == a_len-1):
                sum2 = sum2 + int(a[x][y])
    result = abs(sum1 - sum2)
    return result

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
result=diagonalDifference(a)
print(result)
