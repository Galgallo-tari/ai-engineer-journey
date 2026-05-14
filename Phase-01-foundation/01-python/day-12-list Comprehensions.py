#List Comprehension
domains = ['www.google.com',
           'localhost',
           'www.DATAWITHGALGE.COM']

#cleaned = [
            # Data Transformation
            # For Loop
            # Data Filtering
#]

cleaned = [
    d.lower().replace('www', '')
    for d in domains
    if '.' in d
]

print(cleaned)

#Example


nums = [3, 7, 8, 9, 6]

#.....instead of this....

new_nums = []
for n in nums:
    add = n + 2
    new_nums.append(add)
print(new_nums)

#....use...
new_nums =[n+2 for n in nums]

print(new_nums)


#Example 2

tv_shows = ['friends', 'PARK AND RECREATION', 'the Office', '30 rock', 'modern FAMILY']

tv_shows_cap = []
for show in tv_shows:
    if len(show) < 10:
        show_cap = show.title()
        tv_shows_cap.append(show_cap)
print(tv_shows_cap)


tv_shows_cap = [show.title() for show in tv_shows if len(show) >= 10]

print(tv_shows_cap)






# LAMBDA

# Lambda has 3 parts
# 1. lambda  2. input(param) 3. Expression

multiply = lambda x: x*2
print(multiply(3))

calc = lambda x, y: x*y+2-x
print(calc(2, 7))

check = lambda i: i in 'python'
print(check('p'))
print(check('m'))
print(check('o'))


#Lambda with map

prices = ['$25.30', '$67.50', '$70.00']

#first solve for one list
#....
# p = '$25.30'
#print(p.replace('$', '')
#the use Lambda + map to use for all list

print(list(map(lambda p: float(p.replace('$', '')), prices)))




#Lambda with filter

prices = [120, 30, 300, 80]

print(list(filter(lambda p: p >= 100, prices)))


students = [['Tariq', 90],
            ['Galge', 87],
            ['Marcus', 56],
            ['Kumar', 74]]

print(list(filter(lambda row: row[1] > 70, students)))


 #Challenge .. keep only students with names starting with 'M'

students = [['Maria', 90],
            ['Kumar', 86],
            ['Max', 60]]

print(list(filter(lambda row: row[0].startswith('M'), students)))






