#Build a Bill Splitter

running_total = 0

friends_num = 2

coffee = 34.89
pizza = 52.34
cake = 29.39
take_away = 64.27

running_total += coffee + pizza + cake + take_away
print('Total bill so far:$', running_total)

tip = running_total * 0.25
print('Tip amount:$', tip)

running_total += tip
print('Total with tip:$', running_total)

final_bill = running_total / friends_num
print('Bill per person:$', final_bill)

each_pays = round(final_bill, 2)
print(f'Each person pays: ${each_pays}')