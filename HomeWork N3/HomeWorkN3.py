# 1
# user_input = int(input("Enter a number: "))
#
# while user_input > 0:
#     print(user_input)
#     user_input -= 1


# 2
# total_sum = 0
#
# while True:
#     user_input = input("შეიყვანეთ რიცხვი ან 'sum' ჯამის გასათვლელად: ")
#
#     if user_input.lower() == "sum":
#         print(f"შეყვანილი დადებითი რიცხვების ჯამი არის: {total_sum}")
#         break
#
#     if user_input.isdigit():
#         number = int(user_input)
#         if number > 0:
#             total_sum += number
#         else:
#             print("გთხოვთ, შეიყვანეთ დადებითი რიცხვი.")
#     else:
#         print("გთხოვთ, შეიყვანეთ დადებითი რიცხვი ან 'sum' ჯამის გამოსათვლელად.")


# 3
import random

lives = 3
random_number = random.randint(1, 10)
print(random_number)

while True:
    user_input = int(input("Enter a number between 1 and 10: "))

    if user_input == random_number:
        print("Congratulations! You guessed the correct number. correct number was: ", random_number)
        break

    else:
        if user_input > random_number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")

        lives -= 1
        print(f"You have {lives} lives remaining.")

        if lives == 0:
            print(f"Game Over! You ran out of lives. number was: {random_number}")
            break