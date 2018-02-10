#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    alice = 0
    bob = 0
    none = 0
    a = [a0, a1, a2]
    b = [b0, b1, b2]
    for x in range(3):
        if a[x] > b[x]:
            alice += 1
        if a[x] == b[x]:
            none += 1
        if a[x] < b[x]:
            bob += 1
    return str(bob) + '' + str(alice)
    # Complete this function

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))


