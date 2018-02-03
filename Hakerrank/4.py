#!/bin/python3

import sys


n = int(input().strip())
for x in range(0,n):
    x = str(input())
    x_sp = list(x)
    even = ''
    odd = ''
    xy = ''
    y = len(x)
    for t in range(0,y):
        if x_sp[t].isupper() is 'True':
            x_sp[t].upper()
        else:
            x_sp[t].lower()
    for t in range(0, y):
        xy += x_sp[t]
