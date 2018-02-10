l,k = input().split()
x = int(l)
y = int(k)
num = []
for k in range(y):
    num.append((input().split()))
print(num)
for i in range(x):
    sum = 0
    for j in range(y):
       sum = sum + float(num[j][i])
    print(sum/y)

'''
n, x = map(int, input().split())

sheet = []
for _ in range(x):
    sheet.append(map(float, input().split()))

for i in zip(*sheet):
    print(sum(i)/len(i))
'''