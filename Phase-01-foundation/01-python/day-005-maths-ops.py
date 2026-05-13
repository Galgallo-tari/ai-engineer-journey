# ARITHMETIC OPERATION


#integer
my_int_1 = 20
my_int_2 = 10

#addition
total_int = my_int_1 + my_int_2
print(total_int)

#subtraction
remaining_int = my_int_1 - my_int_2
print(remaining_int)

#division
div_int = my_int_1 / my_int_2
print(div_int)

#multiplication
multiply_int = my_int_1 * my_int_2
print(multiply_int)

#exponentation  - for square
expo_int = my_int_2 ** 2
print(expo_int)

#floor division  - removes decimal
floor_int = my_int_1 // 3
print(floor_int)        #6

calc = 7 // 2
print(calc)         #3

#modulo     this gives what remained after division
mod_int = my_int_1 % 3
print(mod_int)          #2


"""
book = 5
book = book + 3
print(book)



book = 5
book += 3
print(book)
"""

# round( )

my_float_1 = 4.546
my_float_2 = 4.234
my_float_3 = 4.352

rounded_float_1 = round(my_float_1)
rounded_float_2 = round(my_float_2, 3)  #....this will give in 3 decimal places
rounded_float_3 = round(my_float_2, 1)  #....this will give in 1 decimal places

print(rounded_float_1)          #5
print(rounded_float_2)          #4.234
print(rounded_float_3)          #4.2


#abs( )....this gives absolute value of a number

num = -500

abs_num = abs(num)

print(abs_num)          #500

#pow ( )

result_1 = pow(3, 2)        #equivalent to 3 ** 2
result_2 = pow(3, 2, 2)     #equivalent to (3**2) % 2

equiv_of_result_1 = 3 ** 2
equiv_of_result_2 = (3**2) % 2


print(result_1)                 #9
print(result_2)                 #1

print(equiv_of_result_1)        #9
print(equiv_of_result_2)        #1


numbers_1 = min(3, 2, 6, 76, 34, 23, 34, 54, 5)
numbers_2 = max(3, 2, 6, 76, 34, 23, 34, 54, 5)

print(numbers_1)
print(numbers_2)

