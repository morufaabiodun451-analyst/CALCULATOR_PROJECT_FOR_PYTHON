# create and write lines

student = open('student_note.txt','w')
student.write('My name is Morufa.\n')
student.write('I am a computer science student.\n')

future = ['I want to become a data analyst.\n']
student.writelines(future)
student.close()

# append

student = open('my_note.txt','a')
student.write('I enjoy programming in python.\n')
student.close()

# read 
student = open('my_note.txt','r')
content = student.read()
print(content)
student.close()

# count of lines
student = open('my_note.txt','r')
lines = student.readlines()
print(len(lines))
student.close()

# fix bug
# student.writable(['hello\n','world\n'])
# student.writelines(['hello\n','world\n'])

# explanation
# writable() checks if file can be written to (returns True/False)
# writelines() write multiple line to file

# store names with numbering
student = open('employees.txt','w')
for i in range(1,11):
    name = input('enter employee {i} name: ')
    student.write('{i}.{name}\n')
student.close()

# print
student = open('employees.txt','r')
lines = student.readlines()
print(lines[2])
print(lines[4])
student.close()

# store and display
quotes = [
    'never give up\n',
    'stay consistent\n',
    'knowledge is power\n',
    'success takes time\n',
    'believe in yourself.\n'
]
student = open('quotes.txt','w')
student.writelines(quotes)
student.close()
student = open('quotes.txt','r')
for line in student:
    print(line.strip())
student.close()

# save then stop
student = open('user_txt','w')
while True:
    text = input('enter text (type stop to end): ')
    if text == 'stop':
        break
    student.write(text + '\n')
student.close()

# copy content
source = open('my_note.txt','r')
destination = open('copy_note.txt', 'w')
content = source.read()
destination.write(content)
source.close()
destination.close()