# 1

import random


#
#
# def random_range():
#     lst = []
#
#     for _ in range(100):
#         lst.append(random.randint(1, 100))
#
#     print(lst)
#
#     lst.sort()
#     print(lst)
#
#     print(sorted(lst, reverse=True))
#
#
# random_range()


# 2

# def sorting_algorithms():
#     lst = []
#
#     for _ in range(100):
#         lst.append(random.randint(1, 100))
#
#     print(f"Random 100 number list: {lst}")
#
#     # Bubble Sort
#     for i in range(len(lst)):
#         for j in range(i + 1, len(lst)):
#             if lst[i] > lst[j]:
#                 lst[i], lst[j] = lst[j], lst[i]
#
#     print(f"Used Bubble Sort for increment: {lst}")
#
#     # Insertion Sort
#     for k in range(1, len(lst)):
#         key_item = lst[k]
#         l = k - 1
#
#         while l >= 0 and lst[l] < key_item:
#             lst[l + 1] = lst[l]
#             l -= 1
#
#         lst[l + 1] = key_item
#
#     print(f"Implementing Sorting Algorithms: {lst}")
#
#
# sorting_algorithms()

# 3

# increase = 0.02
#
#
# def citizens_algorithms():
#     citizens = 1000
#     year = 0
#     operations = 0
#
#     while citizens < 10000:
#         year += 1
#         citizens = citizens * (1 + increase)
#         operations += 1
#
#     print(f"Year Needed: {year}")
#     return year
#
#
# citizens_algorithms()
#
# try:
#     def citizens_year(year):
#         citizens = 1000
#
#         population = citizens * (1 + increase) * year
#
#         print(f"population after {year} years: {population}")
#         return population
#
#
#     citizens_year(float(input("Enter a year: ")))
#
# except (ValueError, TypeError):
#     print("Value Error: Please enter a number")
#
#
# # 4
# def two_list():
#     first_list = [2, 40, 21, 32, 54, 234, 123, 1]
#     second_list = [32, 20, 45, 123, 34, 2134, 41, 0]
#     new_list = []
#
#     for i in range(min(len(first_list), len(second_list))):
#         if first_list[i] > second_list[i]:
#             new_list.append(first_list[i])
#         else:
#             new_list.append(second_list[i])
#
#     print(new_list)
#
#
# two_list()
#
# # 5
#
# try:
#     def triangle(first_number, second_number, third_number):
#         if first_number + second_number > third_number:
#             return "it is possible to build a triangle"
#         else:
#             return "it isn't possible to build a triangle"
#
#
#     first_number = int(input("Enter first number: "))
#     second_number = int(input("Enter second number: "))
#     third_number = int(input("Enter third number: "))
#
#     print(triangle(first_number, second_number, third_number))
#
# except ValueError:
#     print("Value Error: Please enter a number")
#
#
# # 6
# def students():
#     student_list = {
#         "Mellisa Parker": [91, 60, 89, 84, 26],
#         "Paige Simon": [39, 90, 38, 74, 49],
#         "Kevin Atkins": [27, 7, 89, 96, 62],
#         "Barry Ramo": [94, 93, 62, 30, 66],
#         "Karen Hudson": [51, 15, 94, 20, 8],
#         "Jennifer Diaz": [56, 31, 81, 52, 50],
#         "Robin Smith": [90, 3, 92, 86, 14],
#         "Kevin Clark": [69, 65, 47, 58, 44],
#         "Lisa Shields DDS": [92, 1, 53, 40, 89],
#         "John Kennedy": [21, 41, 12, 15, 90]
#     }
#
#     students_info = []
#     for key, value in student_list.items():
#         avg = sum(value) / len(value)
#         students_info.append([f'{key}, "avg" {avg}'])
#
#     print(students_info)
#
#
# students()


# 7

def num_list():
    numbers = [9255, 1358, 1045285, 59828218, 881525, 388, 8586, 9988, 599828, 812358, 855, 85585, 85885, 888]

    five = '5'
    eight = '8'

    eight_five_list = []
    for number in numbers:
        number_str = str(number)
        if five in number_str and eight in number_str:
            eight_five_list.append(number)
        else:
            pass

    print(eight_five_list)

    eight_list = []
    for number in numbers:
        num_str = str(number)
        if num_str.count('8') > num_str.count('5'):
            eight_list.append(number)

    print(eight_list)


num_list()
