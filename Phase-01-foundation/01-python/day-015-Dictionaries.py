#dictionaries = a collection of {key : value} pairs
#               ordered and changeable. No duplicates

capitals = {'Kenya' : 'Nairobi',
            'Tanzania' : 'Arusha',
            'Ethiopia' : 'Addis Ababa',
            'Germany' : 'Berlin',
            'China' : 'Beiing'}

print(capitals)

if capitals['Kenya'] == 'Nairobi':
    print('Jambo Kenya')

else:
    print('capital doesnt exist')

if capitals.get('Tanzania'):
    print('Capital Exists')

else:
    print('Capital doesnt exist')

capitals.update({'USA' : 'DC Washington'})
print(capitals)

capitals.update({'Kenya' : 'Isiolo'})
print(capitals)

capitals.pop('Tanzania')
print(capitals)

capitals.popitem()
print(capitals)

# capitals.clear()
# print(capitals)

keys = capitals.keys()
print(keys)

values = capitals.values()
print(values)


print('***keys***')
for key in capitals.keys():
    print(key)


print('***values***')
for value in capitals.values():
    print(value)


print('***items ***')

items  = capitals.items()
for key, value  in capitals.items ():
    print(f'{key}: {value}')
