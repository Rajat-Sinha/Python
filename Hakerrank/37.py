import re
x = int(input())

for i in range(x):
    x = str(input())
    ans = True
    try:
        reg = re.compile(x)
    except re.error:
        ans = False
    print(ans)
