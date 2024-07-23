# 1
import random

import random


def binary_function():
    list_of_random_numbers = []

    for number in range(0, 100):
        list_of_random_numbers.append(random.randint(0, 100))

    print("Original random list:", list_of_random_numbers)

    def line_search(lst, search_number: int):
        if search_number in lst:
            return lst.index(search_number)
        else:
            return -1

    print("Linear search result for 10 in unsorted list:", line_search(list_of_random_numbers, 10))

    def bubble_sort(list_of_numbers):
        for i in range(len(list_of_numbers)):
            for j in range(0, len(list_of_numbers) - i - 1):
                if list_of_numbers[j] > list_of_numbers[j + 1]:
                    list_of_numbers[j], list_of_numbers[j + 1] = list_of_numbers[j + 1], list_of_numbers[j]
        return list_of_numbers

    sorted_list = bubble_sort(list_of_random_numbers.copy())
    print("Sorted list using bubble sort:", sorted_list)

    def binary_search(list_of_random_numbers, search_number: int):
        left, right = 0, len(list_of_random_numbers) - 1
        while left <= right:
            mid = (left + right) // 2
            if list_of_random_numbers[mid] == search_number:
                return mid
            elif list_of_random_numbers[mid] < search_number:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    print("Binary search result for 10 in sorted list:", binary_search(sorted_list, 10))


binary_function()

# 2

numbers_that_are_multiples_of_three = lambda x: x % 3 == 0


def find_multiples_of_three(lst: list, lambda_func):
    new_list = []
    for i in range(len(lst)):
        if lambda_func(lst[i]):
            new_list.append(i)
    return new_list


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = find_multiples_of_three(lst, numbers_that_are_multiples_of_three)
print(f'List of numbers which is multiples of 3: {result}')
