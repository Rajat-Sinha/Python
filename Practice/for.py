name = ['Rajat','Rahul','Lishan','Ravi','Kawi','Liwi']

for f in name:
    print(f,end=' ')
    print(len(f))


for f in name[2:]: #ends at not 2
    print(f,end='')
    print(len(f))

for f in name[2:]: #starts from 2
    print(f,end='')
    print(len(f))