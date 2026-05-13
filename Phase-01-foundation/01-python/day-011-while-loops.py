# While Loops

#while condition
    #do something
'''

# updating a variable

x = 0
x = x + 1

# While Loops is repeating a piece of code until the condition becomes False
n = 1
while n <= 3:
    print(n)
    n += 1


while True:
    n = input('Do you want to play the game again?: ').lower()
    if n == 'no':
        print('Okay, Byee')
        break
    else:
        print(n)
'''


#Application in a Calculator

while True:
    num1 = int(input('Enter the first Number: '))
    num2 = int(input('Enter the second Number: '))
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

    choice = input('Want to continue?(yes/no): ').lower()
    if choice == 'yes':
        continue
    else:
        print('Stay Safe')
        break