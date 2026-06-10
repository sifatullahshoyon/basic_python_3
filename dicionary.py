person = {
    'name' : 'Sifat',
    'address' : 'Dhaka',
    'age' : 23,
    'Proffesion' : 'Student'
}
print(person)
print(person['Proffesion'])
print(person.keys())
print(person.values())
person['Language'] = 'Python'
person['name'] = 'Sifat Ullah Shoyon'
del person['age']
print(person)

# special dictionary looping
for item in person:
    print('Item: ', item)

for key, value in person.items():
    print(key, value)