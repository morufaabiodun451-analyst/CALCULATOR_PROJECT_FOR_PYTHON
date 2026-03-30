# calculator program

# ask the user to enter two numbers
a_num = float(input('enter first number: \n'))
b_num = float(input('enter second number: \n'))

# ask the user to choose operation
print('choose an operation:')
print('+ for addition')
print('- for substraction')
print('* for multiplication')
print('/ for division')

operation = input('enter operation (+,-,*,/): ')

# perform the calculation based on the operation
if operation == '+':
    result = a_num + b_num
    print('result:', result)

elif operation == '-':
    result = a_num - b_num
    print('result:', result)

elif operation == '*':
    result = a_num * b_num
    print('result:', result)

elif operation == '/':
    # check for division by zero
    if b_num == 0:
        print('error:division by zero is not allowed.')
    else: 
       result = a_num / b_num
       print('result:', result)

else:print('invalid')


# Percentage app

# ask the user for number
num = float(input('enter number: '))

# ask the user for percentage
percentage = float(input('enter percentage: '))

# calculate the percentage of the number
result = (percentage / 100) * num

# display result
print(percentage,'% of', num, 'is', result)
print(f'{percentage}, % of ,{num}, is {result}')

