if __name__ == '__main__':
    N = int(input())

list = set(map(int,input().split()))
print(list)

x_y = int(input())

for c in range(x_y):
    v1 = 0
    v2 = 0
    command = ''
    string = input()
    st = string.split()
    st_length = len(st)

    command = st[0]
    v1 = int(st[1])
    if 'intersection_update' in  st:
        new_1 = set(map(int,input().split()))
        list.intersection_update(new_1)
    elif 'symmetric_difference_update' in st:
        new_2 = set(map(int, input().split()))
        list.symmetric_difference_update(new_2)
    elif 'difference_update' in st:
        new_3 = set(map(int, input().split()))
        list.difference_update(new_3)
    elif 'update' in st:
        new_4 = set(map(int, input().split()))
        list.update(new_4)

print(list)