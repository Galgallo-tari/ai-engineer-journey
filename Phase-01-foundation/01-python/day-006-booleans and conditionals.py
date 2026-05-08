# boolean and conditionals
# boolean returns True/False
#conditionals let you control flow of program based on whether certain conditions are True or False
# comparison compares two or more values

print(3<4)              #   less than                   #True
print(5>7)              #   greater than                #False
print(3== 3.0)          #   equal to                    #True
print(4 != 4)           #   not equal to                #True
print(7 <= 5)           #   less than or equal to       #False
print(9<=11)            #   greater than or equal to    #True


#conditionals

age = 12

if age >= 18:
    print('You are an Adult')
else:
    print('You are underage Nigga!')


#......
age = 100

if age >= 65:
    print('You are Old')
elif age >= 30:
    print('You are in your prime')
elif age >= 18:
    print('You are Young Adult')
elif age > 12:
    print('You are Teenager')
elif age > 3:
    print('You are young child')
elif age >=1:
    print('How did you typed this?')

'''
# nested conditional statements

Citizen = input("Are you a Citizen?(Yes/No): ").lower()

if Citizen == 'yes':
    age = int(input('Enter Your Age:'))
    if age >18:
        print('You are Eligible to Vote')

    else:
        print('You are below Voting Age, borrow some!')

elif Citizen == 'NO':
    print('You are not Eligible to vote in this Country, no matter your Age.')

else:
    print('Enter correct input please!')
'''



#Here are a few falsy values:

name = None
dating = False
integer = 0
float_ = 0.0
empty_strings = ''

print(bool(name))           #False
print(bool(dating))         #False
print(bool(float_))          #False
print(bool(empty_strings))  #False
print(bool(integer))        #False


#Here are a few Truthy values:

name = 'Galgallo'
dating = True
integer = 3
float_ = 5.0
strings = ' '

print(bool(name))            #True
print(bool(dating))          #True
print(bool(float_))          #True
print(bool(strings))         #True
print(bool(integer))         #True


#Boolean operators.....and/or/not


#and

age = 20
is_citizen = True
registered_voter = True

if age > 18 and is_citizen and registered_voter:
    print('See You Aug, 2027!')

else:
    print('Next time. You are not yet eligible.')



#or

age = 19
is_student = True

if age >= 19 or is_student:
    print('Stands a chance to win Students Laptop')

else:
    print('DENIED!! Either go back to school or wait for some years to be 19😂')


#not

a = True
print(not a)   #False

b = False
print(not b)    #True

