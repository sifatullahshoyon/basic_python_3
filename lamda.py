# lambda

# def doubled(x):
#     return x*2

doubled = lambda num : num * 2
squared = lambda num : num ** 2

result = doubled(44)
output = squared(9)
# print(output)

add = lambda x,y : x + y
sum = add(21, 54)
# print(sum)

numbers = [12,56,98,78,56,12,6,98]
# doubled_nums = map(doubled, numbers)
doubled_nums = map(lambda x : x*2, numbers)
print(numbers)
print(list(doubled_nums))

# Filter
actors = [
    {'name' : 'sabana', 'age' : 65},
    {'name' : 'Tasnim Farhan', 'age' : 31},
    {'name' : 'Sabila Noor', 'age' : 30},
    {'name' : 'Joya Ahsan', 'age' : 47},
]

juniors = filter(lambda actor : actor['age'] < 40, actors)
print(list(juniors))