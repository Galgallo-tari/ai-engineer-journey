#   exception = An event that interrupt the flow of a program
#       (ZeroDivision, TypeError, ValueError)
#               1. try  2. except  3. finally

try:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    result = num1 / num2
    print(result)
except ZeroDivisionError as e:
    print(e)
    print('The division by zero error occurred')
except ValueError as e:
    print(e)
    print('The value entered is not a number')
except Exception as e:
    print(e)
    print('something went wrong:(')
else:
    print(result)
finally:
    print('This will always execute')


