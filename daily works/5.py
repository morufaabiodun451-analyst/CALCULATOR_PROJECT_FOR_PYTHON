# more on string and numeric values

#hospital dataset

patient_name1 = 'Rasaq Opemipo'
age1 = 14
patient_name2 = 'Moses Toluwani'
age2 = 17
patient_name3 = 'Bokoh Margaret'
age3 = 17

# commom disease among teenager fever,chicken pox,acne etc
# patient name
patient_name = input('enter your name: \n')
# symptoms list
print('\nselect from the below symptoms:\n')

symptoms1 = 'high blood temperature,sweating,headache,loss of appetite'
symptoms2 = 'pimples,oily skin,dark spots'
symptoms3 = 'fever,tiredness,itchy blisters'

print('1.', symptoms1)
print('2.', symptoms2)
print('3.', symptoms3)

# user choice
symptoms = input('enter option (1, 2 or 3): ')

# diagnosis
if symptoms == '1':
     print('fever')

elif symptoms == '2':
     print('acne')

elif symptoms == '3':  
     print('chicken pox')
       
else:print('consider doing a thorough check_up.')
