#Build an Employee Profile Generator

first_name = 'Galgallo'
last_name = 'Godana'
full_name = first_name + ' ' + last_name
address = '034 Main Street'
address += ', Blue Apartment 4B'
employee_age = 19
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)
experience_years = 1
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)
position = 'AI Engineer'
salary = 100000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)
employee_code = 'ENG-2026-GG-008'
department = employee_code[0:3]
print('Department:', department)
year_code = employee_code[4:8]
print('Year:', year_code)
initials = employee_code[9:11]
print('Initials:', initials)
last_three = employee_code[-3:]
print('Code:', last_three)



