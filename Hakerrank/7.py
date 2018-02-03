def mutate_string(string, position, character):
    str = list(string)
    x = len(str)
    for y in range(0, x):
        if y is position:
            str[y] = character
    new_str = ''
    for t in range(0,x):
        new_str += str[t]
    return new_str

s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)