#Comments And Break
'''
For Multiline line comment use three single quote
for sing line cmment use #
'''

magicNumber = 26

for n in range(100):
    if n is magicNumber:
        print(n,' is the Magic Number')#+ sign is only for adding not printing string with number.For this we have to use comma(,)
        break # used for break and exiting out of the loop
    else:
        print(n)

for n in range(1,100):
    if n%4 is 0:
        print(n)
