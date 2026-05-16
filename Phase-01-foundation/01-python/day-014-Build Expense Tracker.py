def show_balance ():
    print(f'Your current balance is: ${balance:2f}')

def deposit ():
    amount = float(input('Enter your deposit amount: '))
    print(f'Your current deposit amount is: ${amount:.2f}')

    if amount <= 0:
        print('Please enter a valid  amount')
        return 0
    else:
        return  amount

def withdraw ():
    amount = float(input('Enter your withdraw amount: '))
    print(f'Your current withdraw amount is: ${amount:.2f}')


    if amount > balance:
        print('You have insuffient funds')
        return 0

    elif amount <= 0:
        print('Amount must be greater than 0')
        return 0
    else:
        return amount


balance = 0


is_running =True

while is_running :
    print("Welcome to the Expense Tracker")
    print('1. Show balance')
    print('2. Deposit')
    print('3. Withdraw')

    choice = input('Enter your choice (1-4): ')

    if choice == '1':
        show_balance()

    elif choice == '2':
        balance += deposit()

    elif choice == '3':
        balance -= withdraw()
        print(f'Your bank balance is: ${balance:2f}')

    elif choice == '4':
        is_running = False

    else:
        print("Please enter a valid choice")






