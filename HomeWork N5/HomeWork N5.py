# 1

mylist = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9, 12, 34, 49]

result = mylist[3] + mylist[9] + mylist[14]

print(result)

# 2

random_list = [1, 3, 5, 7, 9, 11, 13, 15, 4, 7, 11, 13, 15, 4, 7, 11, 13, 15, 4, 7]
new_list = []

for i in random_list:
    if i % 2 != 0:
        new_list.append(i)

new_list.sort()

print(f'min: {new_list[0]}, max: {new_list[-1]}')

# 3

my_list = [43, '22', 12, 66, 210, ["hi"]]

# a
print(f'index of 210 is: {my_list.index(210)}')

# b
my_list.append('hello')
print(my_list)

# c
my_list.pop(2)
print(my_list)

# d
my_list2 = my_list.copy()
my_list2.clear()
print(my_list2, my_list)

# 4

a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

b = [
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
]

result = []

for i in range(len(a)):
    row = []
    for j in range(len(a[i])):
        row.append(a[i][j] + b[i][j])
    result.append(row)

for row in result:
    print(row)

# 5

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = list(zip(*matrix))

print("საწყისი მატრიცა:")
for row in matrix:
    print(row)

print("\nტრანსპონირებული მატრიცა:")
for row in transposed:
    print(row)

# 6

import random

matrix = []

for _ in range(4):
    row = []
    for _ in range(4):
        row.append(random.randint(1, 100))
    matrix.append(row)

for row in matrix:
    print(row)
