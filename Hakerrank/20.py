input()
s1=set(map(int, ((input().split()))))
input()
s2=set(map(int, ((input().split()))))
print(s1)
print(s2)
ss = sorted(s1 ^ s2)
print(ss)
for i in ss:
    print(i)