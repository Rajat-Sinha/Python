if __name__ == '__main__':
    s = input()
    alpha = 'False'
    alnum = 'False'
    dig = 'False'
    lowe = 'False'
    up = 'False'
    for x in range(0, len(s)):
        if s[x].isalnum():
            alnum = 'True'
        if s[x].isalpha():
            alpha = 'True'
        if s[x].isdigit():
            dig = 'True'
        if s[x].islower():
            lowe = 'True'
        if s[x].isupper():
            up = 'True'

    print(alnum)
    print(alpha)
    print(dig)
    print(lowe)
    print(up)