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
    if st_length is 2:
        command = st[0]
        v1 = int(st[1])
        if 'remove' in  st:
            list.remove(v1)
        elif 'discard' in st:
            list.discard(v1)
    elif st_length is 1:
        command = st[0]
        if 'pop' in st:
            list.pop()


print(sum(list))