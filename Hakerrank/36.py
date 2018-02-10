x = int(input())
for i in range(x):
    a,b = input().split()
    try:
        print(int(a)/int(b))
    except ZeroDivisionError as e:
        print('Error Code: '+ str(e))
    except ValueError as e:
        print('Error Code:'+str(e))