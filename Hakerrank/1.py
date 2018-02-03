if __name__ == '__main__':
    N = int(input())

list = []

for c in range(N):
    v1 = 0
    v2 = 0
    command = ''
    string = input()
    st = string.split(' ')
    st_length = len(st)
    if st_length is 3:
        command = st[0]
        v1 = int(st[1])
        v2 = int(st[2])
        list.insert(v1, v2)
    elif st_length is 2:
        command = st[0]
        v1 = int(st[1])
        if 'remove' in  st:
            list.remove(v1)
        elif 'append' in st:
            list.append(v1)
    elif st_length is 1:
        command = st[0]
        if 'print' in st:
            print(list)
        elif 'sort' in st:
            list.sort()
        elif 'pop' in st:
            list.pop()
        elif 'reverse' in st:
            list.reverse()


print(list)