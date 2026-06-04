name = 'Sifat\'s' # escape
name2 = "Sifat Ullah Shoyon"
# multiline string
name3 = """
Sifat 
Ullah 
Shoyon
"""

print(name)
# string is a sequence of characters
for char in name2:
    print(char)

print(name2[2])
print(name2[1:7])
print(name2[-4])
print(name2[::-1])
# mutable means changeable
# immutable means you can not change it

# name2[2] = '54'
# print(name2)

if 'khan' in name2:
    print('exists')
else:
    print('No Exists')

text_upper = name2.upper()
print('text upper:', text_upper)

sch_name = "Bamoil Ideal Hig'h School & College"

sch_name = "Bamoil Sorkari Prothomik Bidhaloy"
print(sch_name)