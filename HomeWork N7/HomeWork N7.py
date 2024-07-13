# 1

int_list = [10, 20, 30, 40]


def number():
    new_number = int(input("Enter a number: "))
    int_list.append(new_number)
    return int_list


print(number())


# 2

def longest_word():
    word_list = sentences.split()
    longest = max(word_list, key=len)
    return longest


sentences = input("Enter a sentence: ")
print(longest_word())

# 3

numbers = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]


def sum_of_numbers():
    return sum(numbers)


print(sum_of_numbers())


# 4

def main(*args):
    new_list = []
    for i in args:
        if i not in new_list:
            new_list.append(i)
    new_list.sort()
    return new_list


print(main(1, 2, 3, 4, 5, 6, 6, 4, 32, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2))


# 5

def sum_of_digits(number):
    def recursive_sum(num):
        if num == 0:
            return 0
        else:
            last_digit = num % 10
            rest_of_the_number = num // 10
            return last_digit + recursive_sum(rest_of_the_number)

    return recursive_sum(number)


# Main program
number = int(input("Enter a number: "))
result = sum_of_digits(number)
print(f"Sum of digits: {result}")


# 6


def recursion_function(word):
    def inner_function(w):
        return w[::-1]

    return inner_function(word)


word = input("Enter a word: ")
print(recursion_function(word))


# 7

def recursion(n):
    def recursion2(n):
        if n == 1:
            return n
        else:
            return n * recursion2(n - 1)

    return recursion2(int(n))


print(recursion(int(input("Enter a number: "))))
