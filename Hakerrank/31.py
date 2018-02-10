n = set(map(int, input().split()))
x = int(input())
set_list = []
for i in range(x):
    x = set(map(int, input().split()))
    set_list.append(x)

result = True

for i in set_list:
    if not n.issuperset(i):
        result = False

print(result)