n, m = input().split()

sc_ar = input().split()

A = set(input().split())
B = set(input().split())
for i in sc_ar:
    m = i in A
    n = i in B

print(m+n)
