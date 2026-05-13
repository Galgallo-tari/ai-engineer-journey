#7 DAYS DONE... 9th May 2026. 383 Days to go.


#001variables

#string
name = 'Galgallo'
school = 'Havard'
age = '19'

print(type(name))

#integers
Age = 19
profit = 19000

print(type(profit))

#boolean
is_schooling = True
has_sport_bike = False

print(type(is_schooling))

#float
salary = 89000.790
quantity = 67.65

print(type(salary))

#list ... mutable, ordered, duplicate.... [ ]

car_brands = ['BMW', 'Mercedes Benz', 'Toyota']

print(type(car_brands))

#tuples ... immutable, ordered, duplicate.... ( )

phone_brands = ('Iphone', 'Samsung', 'Google Pixel')

print(type(phone_brands))

#set ... mutable, unordered, No duplicate

shoe_brands = {'Nike', 'Adidas', 'New Balance'}

print(type(shoe_brands))


#maths operation

num1 = 3
num2 = 5

print(num1 + num2)
print(num1 - num2)
print(num1 / num2)
print(num1 // num2)
print(num1 * num2)
print(num1 ** num2)
print(num1 % num2)

#coditionals

num1 = int(input('Enter the first Number:'))
num2 = int(input('Enter the second Number:'))
symbol = input('Enter the Symbol(+ - x /): ').lower()

if symbol == '+':
    print(num1 + num2)
elif symbol == '-':
    print(num1 - num2)
elif symbol == 'x':
    print(num1 * num2)
elif symbol == '/':
    print(num1/num2)
else:
    print('please choose appropriate symbol')

