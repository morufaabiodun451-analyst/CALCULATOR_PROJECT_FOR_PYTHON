# numbers from 1 to 10

for i in range (1,11):
    print(i)

print('\n')

# even numbers from 1 to 20
for i in range (1,21):
    if i % 2==0:
        print(i)

print('\n')

# each character in python
word = 'python'
for w in word:
    print(w)

print('\n')

# numbers from 10 to 1
for num in range (10,0,-1):
    print(num)

print('\n')

# sum of numbers from 1 to 10
total = 0
for i in range (1,11):
    total += i
print('sum of numbers =', total)

print('\n')

# multiplication table of 5
for i in range(1,13):
    print('5 x', i, '=', 5 * i)

print('\n')

# divisible numbers by 3 from 1 to 50
count = 0
for i in range(1,51):
    if 1 % 3 == 0:
        count += 1
print('count =', count)

print('\n')

# largest numbers in a list
numbers =[3,7,2,9,5]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print('largest number =', largest)

print('\n')

# square pattern of stars of size 5
for i in range(5):
    for j in range(5):
        print('*',end='')
    print()

print('\n')

# reversed string
text = 'python'
reversed_text = '' 

for t in text :
    reversed_text = t + reversed_text
print(reversed_text)