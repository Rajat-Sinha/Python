#!/bin/python3

import sys
import string

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
x = 0
new_arr = []
while x < n:
    t = n - x - 1
    x_y = str(arr[t]) + ' '
    print(x_y,end='')
    #new_arr[x] = arr[t]
    #pri(new_arr[x])
    x += 1

