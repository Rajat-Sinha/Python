from collections import Counter

x = int(input())
shoe_size = Counter(map(int, input().split()))
sum = 0
for i in range(int(input())):
    num,p = map(int, input().split())
    if shoe_size[num]:
        sum = sum + p
        shoe_size[num] = shoe_size[num] - 1
print(sum)