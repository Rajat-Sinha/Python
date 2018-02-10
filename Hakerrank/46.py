#!/bin/python3

import sys

def miniMaxSum(arr):
    s = sum(arr)
    print(str(s - max(arr)) + ' ' + str(s - min(arr)))

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
