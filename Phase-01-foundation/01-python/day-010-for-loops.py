#for loops = execute a block of a code fixed number of times.

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