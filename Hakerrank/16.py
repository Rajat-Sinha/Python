#!/bin/python3

import sys

def factorial(n):
    ans = 1
    for x in range(1,n+1):
        ans = ans*x
    return ans

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
