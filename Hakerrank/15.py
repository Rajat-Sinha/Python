def capitalize(string):
    x_y = string.split(' ')
    for x in range(0,len(x_y)):
        x_y[x] = x_y[x].capitalize()
    ans = ''
    for y in range(0, len(x_y)):
        ans = ans +x_y[y] + ' '
    print(ans)

if __name__ == '__main__':
    string = input()
    capitalize(string)
    #print(capitalize(string))