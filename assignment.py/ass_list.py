# create a list of 5 fruits and print the list
fruits = ['Banana', 'pineapple', 'Watermelon', 'Apple', 'Orange']
print(fruits)

# add a new fruit to the end of the list using append()
fruits.append('cucumber')
print(fruits)

# insert a fruit at position 2 in your list
fruits.insert(2,'cherry')
print(fruits)

# remove the last item from the list using pop()
fruits.pop(-1)
print(fruits)

# remove the last item from the list using remove()
fruits.remove('Orange')
print(fruits)

# create a list of numbers and sort in ascending
numbers = [12,21,10,3,2005,3,3,10]
numbers.sort()
print(numbers)

# reverse the order of a list using reverse()
numbers.reverse()
print(numbers)

# count how many times a number appears in list using count()
count = numbers.count(3)
print(count)

# find the index of a specific element in a list using index
index = numbers.index(2005)
print(index)

# create two lists and combine them into one list
combine = fruits + numbers
print(combine)