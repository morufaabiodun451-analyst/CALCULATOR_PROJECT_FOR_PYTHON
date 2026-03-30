# smart security system
# variables
has_keycard = True
knows_password = True
is_admin = False
# condition
if (has_keycard and knows_password) or is_admin:
    print('access granted')
else:
    print('access denied')


# online shopping checker
# variables
items_in_cart = True
payment_successful = False

# condition
if items_in_cart and payment_successful:
    print('checkout successful')
else:
    print('checkout failed')

    if not items_in_cart:
        print('reason: no items in cart')
    if not payment_successful:
        print('reason: payment not successful')


# traffic light stimulator
# variable
light_color = 'red'
light_color = 'yellow'
light_color = 'green'

# condition
if light_color == 'red':
    print('stop')
elif light_color == 'yellow':
    print('get ready')
elif light_color == 'green':
    print('go')
else:
    print('invalid light color')


# exam eligibility
# variable
attendance = 80 #percentage
fees_paid = True
# condition
if attendance > 75 and fees_paid:
    print('you are eligible to take the exam')
else:
    print('you are not eligible to take the exam')

    if attendance <=75:
       print('reason: attendance is below 75%')
    if not fees_paid:
        print('reason: fees not paid')


# weather decision maker
# variable
is_sunny = True
is_windy = False
is_raining = False

# condition
if is_raining:
    print('stay home or carry an umbrella')
elif is_sunny and not is_windy:
    print('go outside, the weather is nice')
elif is_sunny and is_windy:
    print('you can go out, but it is windy')
else:
    print('better stay home')