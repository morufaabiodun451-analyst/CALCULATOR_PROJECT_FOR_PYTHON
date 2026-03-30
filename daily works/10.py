# student scores

#names_of_student = ['Morufa', 'Yusuf', 'Rahman', 'Abiodun']
#for name in names_of_student:
   # print(name)

for i in range(3):
    student = input('enter your name: \n')
    student_scores = input('enter your scores: \n')
    if student_scores <= '49':
        grade = 'F'
    elif student_scores <= '60':
        grade = 'C'
    elif student_scores <= '80':
        grade = 'B'
    else:
        grade = 'A'
print(student, 'got grade:', grade)