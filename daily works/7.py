# conditional statement
# to become a data scientist
# variables
AI = True
ML = True
Statistic_and_mathematics = True
knows_python = True
sql = False
coding = False

# conditions
if AI and ML and Statistic_and_mathematics and knows_python and not sql:
    print('You can become a data scientist')
else:
    print('You need to learn the basic skill')    
    if not knows_python or not ML:
        print('you need to know more')
    elif not Statistic_and_mathematics:
        print('you are still joking') 
        

