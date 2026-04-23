student_score = open('student.txt','w')

for x in range(5):
    name = input('enter your name:')
    score = int(input('enter your score:'))
    if score >= 90 :
        grade = 'A'
    elif score >= 70 :
        grade = 'B'
    elif score >= 50 :
        grade = 'C'
    else:
        grade = 'F'
    print(name,score,grade)
    student_score.write(name + ' ' + str(score) + ' ' + grade + '\n')
student_score.close()