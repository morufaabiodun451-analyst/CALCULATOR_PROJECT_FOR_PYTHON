# conditional statement

score = int(input)
if score >= 90:
    print('You are an A student ✅✅✅')
elif score >= 70:
    print('You are a B student ✅')
else:
    print('You are a C student.. You may need to do better 😊')

# logical operators (AND, OR, NOT)
a, b, c = True, False, True

if a and b:
    print('Both a and b are false')

if a or b:
    print('one must be true')

if not b:
    print('b is false')

# real life example

# AND
has_username = True
has_password = True

if has_username and has_password:
    print('login successful! Welcome!!!')
else:
    print('missing username or password')