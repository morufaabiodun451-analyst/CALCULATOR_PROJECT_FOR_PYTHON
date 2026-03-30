# conditional statement
# money and foodstuff

# money available
amount_own = 10000
foodstuff_to_buy = 'rice, pepper, fish, veggies, spices'
# prices
price_of_rice = 2000
price_of_pepper = 1500
price_of_fish = 5000
price_of_veggies = 1000
price_of_spices = 600

# calculate total
total = price_of_rice + price_of_pepper + price_of_fish + price_of_veggies + price_of_spices
print('1.rice',price_of_rice)
print('2.pepper',price_of_pepper)
print('3.fish',price_of_fish)
print('4.veggies',price_of_veggies)
print('5.spices',price_of_spices)

foodstuff = input('enter things to buy: \n')

if amount_own >= total:
    print('Buy all.', foodstuff_to_buy)
else:
    print('Withdraw more money, go back home or reduce the things to buy')   