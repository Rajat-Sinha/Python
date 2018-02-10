n = int(input())
arr = map(int, input().strip().split())
#print(set(arr))
#print(list(arr))
x = sorted(list(set(arr)))[-2]
print(x)
