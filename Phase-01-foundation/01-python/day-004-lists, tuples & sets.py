#06th May, 2026

# LIST.....Mutable, Allow Duplicate and Ordered

empty = []
print(empty)

numbers = [1,2,3,4,5]
print(numbers)

letters = ['a','b','c','d','e']
print(letters)

mixed = ['a', 1, True, None]
print(mixed)

my_language = 'Python'
print(my_language)      #Python

language = list(my_language)
print(language)         #['P', 'y', 't', 'h', 'o', 'n']

my_list = [[1,2,3,4],
           ['a','b','c','d'],
           [True, 'today']]
print(my_list)
print(type(my_list))


courses = ['Data Science', 'Data Analytics', 'AI/ML']

print(courses)
print(courses[2])       #AI/ML
print(courses[0])       #Data Science
print(courses[-1])      #AI/ML
print(courses[0:2])     #['Data Science', 'Data Analytics'] first index is included, last index not.
print(courses[0:3])     #['Data Science', 'Data Analytics', 'AI/ML']

courses.append('AI Engineering')
print(courses)               # ['Data Science', 'Data Analytics', 'AI/ML', 'AI Engineering']

courses.insert(0, 'Prompt Engineering')     #['Prompt Engineering', 'Data Science', 'Data Analytics', 'AI/ML', 'AI Engineering']
print(courses)

course_2 = ['Cybersec.' 'IT']

#courses.append(course_2)
#print(courses)      #['Prompt Engineering', 'Data Science', 'Data Analytics', 'AI/ML', 'AI Engineering', ['Cybersec.IT']]

courses.extend(course_2)
print(courses)       #['Prompt Engineering', 'Data Science', 'Data Analytics', 'AI/ML', 'AI Engineering', 'Cybersec', 'IT']

courses.remove('Data Analytics')
print(courses)

courses.pop()
print(courses)          #['Prompt Engineering', 'Data Science', 'AI/ML', 'AI Engineering']

courses.pop()
print(courses)          #['Prompt Engineering', 'Data Science', 'AI/ML']

courses.pop()
print(courses)          #['Prompt Engineering', 'Data Science']

courses.pop()
print(courses)          #['Prompt Engineering']


nums = [1, 10, 19, 7, 3, 2]
nums.sort()

names = ['Galgallo', 'Abel', 'AI', 'Tariq']
names.sort()

print(nums)             #[1, 2, 3, 7, 10, 19]
print(names)            #['AI', 'Abel', 'Galgallo', 'Tariq']


numbers = [1, 10, 19, 7, 3, 2]
numbers.sort(reverse=True)

name = ['Galgallo', 'Abel', 'AI', 'Tariq']
name.sort(reverse=True)

print(numbers)      #[19, 10, 7, 3, 2, 1]
print(name)         #['Tariq', 'Galgallo', 'Abel', 'AI']


apartments = ['Ebenezer', 'Sun Rise', 'Havana', 'Dolphin']

for apartment in apartments:
    print(apartment)

for index, apartment in enumerate(apartments, start=1):         #this will list apartment from 1
    print(index, apartment)

apartments_str = ' | '.join(apartments)     #Ebenezer | Sun Rise | Havana | Dolphin
print(apartments_str)

new_list = apartments_str.split(' | ')
print(new_list)                     #['Ebenezer', 'Sun Rise', 'Havana', 'Dolphin']



#Tuple .... Immutable, Allow Duplicate and Ordered
#this exact as list expect being mutable, tuple is immutable
my_tuple = ('car', 'school')
print(type(my_tuple))

#Set ..... Mutable, No Duplicate and Unordered

cs_courses = {'Math', 'Design', 'AI', 'IT'}
art_courses = {'Craft', 'Math', 'History', 'Design'}

print(cs_courses.intersection(art_courses))     #{'Math', 'Design'}
print(cs_courses.difference(art_courses))       #{'IT', 'AI'}
print(art_courses.difference(cs_courses))       #{'History', 'Craft'}
print(cs_courses.union(art_courses))            #{'IT', 'History', 'Math', 'Design', 'AI', 'Craft'}


