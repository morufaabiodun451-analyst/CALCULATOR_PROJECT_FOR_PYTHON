# funtions that print greeting
def greeting():
    print('hello world')
greeting()

# function of my name
def name():
    print('Yusuf Morufa Abiodun')
name()

# print 1 to 10
def num():
    for i in range(1,11):
        print(i)
num()

# functions for even numbers 1 to 20
def even():
    for i in range(1,21):
        if i % 2 == 0:
            print(i)
even()

# multiplication table of 5
def mul_5():
    for i in range(1,13):
        print('5 x',i,'=',5*i)
mul_5()

# sum of numbers 1 to 50
def sum():
    total = 0
    for i in range(1,51):
        total += i
        print('sum is:', total)
sum()

# check even or odd numbers
def check():
    for i in range(1,50):
        if i % 2 == 0:
            print(i,'is even')   
        else:
            print(i,'is odd')

# star pattern
def  star_pattern():
    for i in range(1,6):
        print('*'*i)

# current year
import datetime
def current_year():
    year = datetime.datetime.now().year
    print('current year is:',year)
current_year()

# square of numbers
def square_numbers():
    for i in range(1,11):
        print(i,"square is",i*i)
square_numbers()