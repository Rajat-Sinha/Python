def count_substring(string, sub_string):
    x = len(string)
    t = len(sub_string)
    counter = 0
    for i in range(0, x):
        if sub_string[0] is string[i]:
            if string[i:(i + t)] == sub_string:
                counter = counter + 1
    return counter


string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)

