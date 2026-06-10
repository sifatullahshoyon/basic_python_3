# List --> []
# tuple --> ()
# set --> {}
# set: Unique items colletion
numbers = [12, 56, 98, 78, 56, 12, 6, 98]
print(numbers)
numbers_set = set(numbers)
print(numbers_set)
numbers_set.add(55) # no order maintain
numbers_set.remove(98)
print(numbers_set)

for item in numbers_set:
    print(item)

if 54 in numbers_set:
    print('54 Exists')
else:
    print('54 is Not Exists')

A = {1, 3, 5, 7}
B = {1, 2, 3, 4, 5}
print(A & B)
print(A | B) # A U B