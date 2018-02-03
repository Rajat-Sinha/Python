def swap_case(s):
    x_sp = list(s)
    print(x_sp)
    xy = ''
    y = len(s)
    for t in range(0, y):
        if x_sp[t].isupper():
            x_sp[t] = x_sp[t].lower()
        else:
            x_sp[t] =  x_sp[t].upper()
    for t in range(0, y):
        xy += x_sp[t]
    return xy

s = input()
result = swap_case(s)
print(result)
