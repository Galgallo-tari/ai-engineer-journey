#scope determines the point at which you can access a variable

"""
Python follows the LEGB rule, which stands for the following:
"""

#    Local scope (L): Variables defined in functions or classes.
#example

def my_func():
    my_var = 10
    print(my_var)

my_func()       #10

#print(my_var)       #NameError: name 'my_var' is not defined


"""
    Global scope (G): Variables defined at the top level of the module or file.

    Built-in scope (B): Reserved names in Python for predefined functions, modules, keywords, and objects.

Python uses the LEGB rule to resolve the scope of the variables in your program.
"""


#Enclosing scope means that a function that's nested inside another function
#           can access the variables of the function it's nested within.

def outer_func():
    msg = 'Hello there!'

    def inner_func():
        print(msg)

    inner_func()

outer_func() # Hello there!

'''
#outer functions cannot access variables defined within any nested functions:
def outer_func():
    msg = 'Hello there!'
    print(res)

    def inner_func():
        res = 'How are you?'
        print(msg)

    inner_func()
    print(res)

outer_func() # NameError: name 'res' is not defined
'''


#One solution is to initialize res as an empty string in the enclosing scope,
#       which is within outer_func. Then within inner_func,
#       make res a non-local variable with the nonlocal keyword:

def outer_func():
    msg = 'Hello there!'
    res = ''

    def inner_func():
        nonlocal res
        res = 'How are you?'
        print(msg)

    inner_func()
    print(res)

outer_func()




#Global scope refers to variables that are declared outside any functions
# or classes which can be accessed from anywhere in the program.


my_var = 100

def show_var():
    print(my_var)

show_var() # 100
print(my_var) # 100


#And if you want to make a locally scoped variable defined
# inside a function globally accessible,
# you can use the global keyword:


my_var_1 = 7

def show_vars():
    global my_var_2
    my_var_2 = 10
    print(my_var_1)
    print(my_var_2)

show_vars() # 7 10

# my_var_2 is now a global variable and can be accessed anywhere in the program
print(my_var_2) # 10


#You can also use the global keyword to modify a global variable:

my_var = 10  # A global variable

def change_var():
    global my_var  # Allows modification of a global variable
    my_var = 20
    print(my_var)

change_var()

print(my_var)  # my_var is now modified globally to 20


#built-in scope refers to all of Python's built-in
# functions, modules, and keywords,
# and are available anywhere in your program:

print(str(45)) # '45'
print(type(3.14)) # <class 'float'>
print(isinstance(3, str)) # False



