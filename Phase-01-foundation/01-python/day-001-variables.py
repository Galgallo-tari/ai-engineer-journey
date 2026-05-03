#This is May 03th 2026

#string
#       in python they are texts enclosed in quotes, Example:
name = 'Galgallo'
school = 'Havard University'
passion = 'Ai'
location = 'Africa'

print(f'{name} studies at {school} and he has passion in {passion}')

#integers
#       an integer should not be in quotes, only strings are stored in quotes.
age = 19
quantity = 10
years_of_experience = 6

print(f'he is {age} year old')
print(f'he has {years_of_experience} years of experience in procastination')
print(quantity)
#float
#       these are decimal numbers
price = 900.00
gpa = 3.9
distance = 5.5

print(f'he got a gpa of {gpa}')

#boolean
#       this have false or true

he_study_abroad = True
he_is_lying = True
he_likes_to_study_abroad = True


#Typecasting - is process of converting a variable from one data type to another.

#integer to string
students = 50
teachers = 15

students = str(students)
teachers = str(teachers)

#to check the type of a variable
print(type(students))
print(type(teachers))


#float to integer
profit = 5000.14
amount = 1500.04

profit = int(profit)
amount = int(amount)

#to check the type of a variable
print(type(profit))
print(type(amount))


#integer to float
salary = 500
expenses = 150

salary = float(salary)
expenses = float(expenses)

#to check the type of a variable
print(type(salary))
print(type(expenses))