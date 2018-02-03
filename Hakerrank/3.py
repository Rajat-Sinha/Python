#!/bin/python3

import sys


n = int(input().strip())
for x in range(0,n):
    x = str(input())
    x_sp = list(x)
    even = ''
    odd = ''
    y = len(x)
    for t in range(0,y):
        if t%2 is 0:
            even +=  x_sp[t]
        else:
            odd += x_sp[t]
    print(even)
    print(odd)