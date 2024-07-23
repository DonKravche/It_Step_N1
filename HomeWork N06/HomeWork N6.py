# 1
def anagram(str1, str2):
    if len(str1) != len(str2):
        return f'{str1} and {str2} are not anagrams'
    if sorted(str1) == sorted(str2):
        return f'{str1} and {str2} are anagrams'
    else:
        return f'{str1} and {str2} are not anagrams'


print(anagram('sword', 'words'))
print(anagram('listen', 'silent'))


# 2

def count_symbol(string, symbol):
    count = 0
    for char in string:
        if char == symbol:
            count += 1
    return count


input_string = input('Enter a string: ')
input_symbol = input('Enter a symbol to count: ')

result = count_symbol(input_string, input_symbol)
print(f"The symbol '{input_symbol}' appears {result} times in the string.")


# 3
import math


def fibonacci(number):
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2

    return round((phi ** number - psi ** number) / sqrt_5)


n = int(input("Enter the position of the Fibonacci number you want to calculate: "))
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")
