# 1
def zip_function():
    lst1 = [1, 2, 3]
    lst2 = ['a', 'b', 'c']

    return zip(lst1, lst2)


print(list(zip_function()))

# 2

even_numbers = lambda lst: [x for x in lst if x % 2 == 0]

params = [1, 2, 3, 4, 5, 6, 7]

result = even_numbers(params)
print(result)

# 3

random_number_list = [-3, -2, -1, 0, 1, 2, 3]

positive_number = filter(lambda num: num > 0, random_number_list)

print(list(positive_number))

# 4

user_input = input("Enter text: ").split()
non_palindromes = []

palindrome = lambda word: word if word == word[::-1] else non_palindromes.append(word)

result = list(map(palindrome, user_input))
print("Non-palindromes:", non_palindromes)

# 5