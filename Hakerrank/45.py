#!/bin/python3

import sys

def staircase(n):
    str = '#'
    for x in range(1,n+1):
        print(('#' * x).rjust(n, ' '))

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)
