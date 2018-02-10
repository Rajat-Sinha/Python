def average(array):
    ar = set()
    i = 0
    while i < len(array):
        ar.add(array[i])
        i+=1
    xy = list(ar)
    i = 0
    sum = 0
    while i < len(xy):
        sum += xy[i]
        i+=1
    return sum

n = int(input())
arr = list(map(int, input().split()))
average(arr)
