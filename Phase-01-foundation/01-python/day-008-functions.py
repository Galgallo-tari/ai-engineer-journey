#10th May 2026... WEEK 2.

#function... this are block of reusable codes

#001

def personal_details(name, age, location, contact):
    print(f'Hello sir {name}')
    print(f'is this details accurate?...\n You are {age} years old, '
          f'live in {location} and this is your contact {contact}')
personal_details('Tariq', 49, 'Ohio', 98789098)

personal_details('John', 71, 'Moscow', 93792829)

personal_details('Joseph', 23, 'Chicago', 67689098)

personal_details('Elizabeth', 24, 'Cuba', 78374388)


#002

def personal_details(name, age, location, contact):
    return (f'Hello sir {name}\n'
            f'Is this details accurate?...\n'
            f'You are {age} years old, '
            f'live in {location} and this is your contact {contact}')

print(personal_details('Tariq', 49, 'Ohio', 98789098))
print(personal_details('John', 71, 'Moscow', 93792829))
print(personal_details('Elizabeth', 24, 'Cuba', 78374388))


#003

def bills_to_pay(transport, house, electricity):
  return (f'Transport: ${transport}\n'
          f'Rent: ${house}\n'
          f'Electricity: ${electricity}')

def send_bills(transport, house, electricity):
  return transport + house + electricity

def total_bill(total):
  print(f'Total Bills: ${total}')

# step 1 — show the breakdown
bills = bills_to_pay(300, 200, 200)
print(bills)

# step 2 — calculate the total
calc = send_bills(300, 200, 200)

# step 3 — print the total
total_bill(calc)


#004

def names(age):
    return f'Galge is {age} years'
his_name = names(20)
print(his_name)


def get_price(pizzas):
  return pizzas * 10

def add_tax(price):
  return price * 1.2

def send_bill(total):
  print(f'Bill: ${total}')

price = get_price(3)
total = add_tax(price)
send_bill(total)


#005

def personal_expense(name, expense_type, amount):
    return f'Hi {name}! Your {expense_type} is ${amount}'

my_name = 'Tariq'

bill1 = personal_expense (my_name, 'transport bill', 300)
bill2 = personal_expense(my_name, 'electricity bill', 200)
bill3 = personal_expense(my_name, 'house bill', 300)

def total_expenses(name, a, b, c):
    return a+b+c

total = total_expenses('Tariq', 200, 300, 300)

print(bill1)
print(bill2)
print(bill3)
print(f'Total bill:{total}')


