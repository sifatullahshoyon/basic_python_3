def multiple():
    return 54,21

# print(multiple())

things = 'Pen', 'tripod', 'water bottle', 'charger', 'phone', 'web cam', 'sunglass'

# print(type(things))

# print(things[0])
# print(things[-2])
# print(things[3:6])

if 'phone' in things:
    print('exists')

for item in things:
    print(item)

# things[0] = 'wagon'
# print(things) # 'tuple' object does not support item assignment

print(len(things))

mega = ([2,3,4], [9,6,8])
# print('Mega',type(mega))
print(mega[0])
mega[0][1] = 546
print(mega)