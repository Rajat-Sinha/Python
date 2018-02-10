#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    s = max(ar)
    y = 0
    for x in range(n):
        if ar[x] == s:
            y+=1
    return y

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
