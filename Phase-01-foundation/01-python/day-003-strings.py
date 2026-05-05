#string
name = 'Galgallo'
institution = "Havard"

#both of line 2 and 3 are a string type, a string can be typed using either a single or doubled quote.
#for multiline use (""" or ''')
institutions = '''
Havard
MKU
UON
JKUAT
OXFORD
'''
print(institutions)

# to check a length of a string:
print(len(institutions))
print(len(institution))

#use in operator to check if a character exists in a string
#it will return a boolean, either True or False

school = 'Sacred Heart Primary'
print('Sacred' in school) #True
print('sacred in school') #False because python is case sensitive, Sacred is not same as sacred

#each character in a string has a position called index and to check the index of a character:
sport = 'football'
print(sport[2])
print(sport[0])
print(sport[-3])

#Strings are immutable data types in Python.
# This means that you can reassign a different string to a variable:

greeting = 'hi'
greeting = 'hello'

print(greeting)  #hello

#String Concatenation - this is adding different string using +
#only used to combine string and a string

my_str_1 = 'Morning'
my_str_2 = 'Everyone'

my_both_str = my_str_1 + ' ' + my_str_2
print(my_both_str)

# String interpolation is process of inserting variables and expressions into a string.
#f-string is used to handle interpolation with a compact and readable syntax.

teacher = 'Mr. John'
position = 'Head Teacher'
school = 'Glory Primary'

print(f'{teacher} is {position} of {school}')

#String slicing lets you extract a portion of a string or work with only a specific part of it
# [START:STOP:STEP]

brand = 'Mitsubishi'
print(brand[2:10:2])       #tuih
print(brand[0::1])    #Mitsubishi





