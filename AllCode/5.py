#Continue

numbersTaken = [2,5,6,4,6,7,23]
print('Here are the numbers that are still availabe')

for n in range(1,25):
    if n in numbersTaken:
        continue
    print(n)