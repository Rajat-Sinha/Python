input()
s1=set(map(int, ((input().split()))))
input()
s2=set(map(int, ((input().split()))))

s3 = set(s1.intersection(s2))
s4 = list(s3)
print(len(s4))