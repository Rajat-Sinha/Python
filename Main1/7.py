#Return Value to The Function
'''


'''
def allowed_dating_age(my_age):
    girls_age = my_age//2 + 7
    return girls_age

my_limit = allowed_dating_age(19)
my_friend_limit = allowed_dating_age(23)
print('I can date the girl of age ',my_limit,' or older')
print('My Friend can date the girl of age ',my_friend_limit,' or older')
