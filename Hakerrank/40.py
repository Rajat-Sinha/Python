n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
if query_name in student_marks:
    sum = 0.00
    for x in range(len(student_marks[query_name])):
        sum = sum + student_marks[query_name][x]
        #print(student_marks[query_name][x])
    ans = sum/len(student_marks[query_name])
    #format(ans, '.3f')
    #print(round(ans, 2))
    print("{0:.2f}".format(ans))





