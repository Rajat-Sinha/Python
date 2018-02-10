n = int(input())
student_marks = {}
name = []
num = []
for i in range(n):
    name.append(str(input()))
    num.append(float(input()))
    student_marks[name[i]] = num[i]

sorted(zip(student_marks.values(),student_marks.keys()))
print(sorted(zip(student_marks.values(),student_marks.keys())))
print(student_marks.values())

'''
N = int(input())
students = []
for i in range(N):
    grade = [input(), float(input())]
    students.append(grade)    
students = sorted(students, key=lambda x: x[1])
second_highest = students[0][1]
for name, grade in students:
    if grade > second_highest:
        second_highest = grade
        break
print('\n'.join([name for name, grade in sorted(students) if grade == second_highest]))

'''

