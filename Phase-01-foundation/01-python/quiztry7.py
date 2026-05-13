#check for missing name

names = ['John', 'Fatma', 'Galgallo', 'Carpenter Marcus']

for name in names:
    if name is None:
        print('Name missing')
        break
else:
    print('All names are available')



#Check if all files are CSV

file_list = ['report.csv', 'data.xlsx', 'report.csv', 'data.csv']

for file in file_list:
    if not file.endswith('.csv'):
        print(f'{file} is not CSV')
        break
else:
    print('All files are CSV')


#USE BOTH FOR AND WHILE LOOP...
#check whether any file name appears more than once..
#print 'Duplicate found' if duplicate exist.
# otherwise print 'All file are unique'

#FOR LOOP

file_list = ['data.xlsx', 'summary.docx', 'report.csv', 'data.csv']
seen = []

for file in file_list:
    if file in seen:
        print('Duplicate found')
        break
    seen.append(file)
else:
    print('file are unique')


#WHILE LOOP

file_list = ['report.csv', 'data.xlsx', 'summary.docx', 'report.csv', 'data.csv']
seen = []
i = 0

while i < len(file_list):
    if file_list[i] in seen:
        print('Duplicate found')
        break
    seen.append(file_list[i])
    i += 1
else:
    print('All files are unique')