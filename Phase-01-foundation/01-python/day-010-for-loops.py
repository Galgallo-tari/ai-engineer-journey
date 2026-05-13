#for loops = execute a block of a code fixed number of times.

#for var in iterable
    #do something

for x in range(1,10,2):
    #(START, END, STEPS)
    print (x)   #13579



for x in reversed(range(1,10,2)):
    print(x)    #97531



for x in range (1,21):
    if x == 13:
        break
    else:
        print(x)       #1 2 3 4 5 6 7 8 9 10 11 12




for i in range(5):
    print(i)

bills = [300, 200, 300]
total = 0



for my_bill in bills:
    print(f'Processing bill: {my_bill}')
    total = total+my_bill
print(f'Total: {total}')


bills = [300, 200, 300]




def expense_summary(name, bills):
    total = 0  # start total at 0

    for my_bill in bills:  # loop through what?
        print(f'Hi {name}! Bill: ${my_bill}')  # use name and my_bill
        total = total + my_bill # add each bill to total

    return total  # return what?


result = expense_summary('Tariq', bills)
print(f'Total: ${result}')

result = expense_summary('John', bills)
print(f'Total: ${result}')

result = expense_summary('Peter', bills)
print(f'Total: ${result}')


"""
items = [0]
for item in items:
    print(item)
    items.append(item)
    if item == +11:
        break
"""



items = [1,2,3,4,5,'Hi']

for item in items:
    print(f'Round: {item}')

#OUTPUT WILL BE

'''
Round: 1
Round: 2
Round: 3
Round: 4
Round: 5
Round: Hi
'''

for i in range(1,11):
    math = 7 * i
    print(f'7 x {i} = {math}')

#OUTPUT WILL BE

'''
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70

  '''

for i in range(1,7):
    symbol = '*' * i
    print(symbol)

#OUTPUT WILL BE

'''
*
**
***
****
*****
******
'''
