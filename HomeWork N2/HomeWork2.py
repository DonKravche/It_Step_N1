# 1

# user_input = int(input("Enter a number: "))
#
# if user_input % 2 == 0:
#     print(user_input, "is an even number.")
# else:
#     print(user_input, "is an odd number.")


# 2

# user_input = str(input("Enter Text: "))
# a, b, c = 'small', 'tall', 'middle'
#
# if a in user_input or b in user_input or c in user_input:
#     print(user_input)
# else:
#     print(f"In this text this words {a}, {b} and {c} can not be founded")


# 3
user_first_number_input = int(input("Please enter your first number: "))
user_operator_input = input("Please enter your operator (plus, minus, multiplication, division, balance): ")
user_second_number_input = int(input("Please enter your second number: "))

if user_operator_input == "plus":
    answer = user_first_number_input + user_second_number_input
    print(answer)
elif user_operator_input == "minus":
    answer = user_first_number_input - user_second_number_input
    print(answer)
elif user_operator_input == "multiplication":
    answer = user_first_number_input * user_second_number_input
    print(answer)
elif user_operator_input == "division":
    if user_second_number_input == 0:
        print("separator can't be 0")
    else:
        answer = user_first_number_input / user_second_number_input
        print(answer)
elif user_operator_input == "balance":
    answer = user_first_number_input % user_second_number_input
    print(answer)
else:
    print("Invalid input")