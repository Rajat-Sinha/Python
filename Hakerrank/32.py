import cmath
n = str(input())
theta = cmath.phase(complex(n))
r = abs(complex(n))
#format(a, '.2f')
print(round(r, 3))
print(round(theta, 3))

