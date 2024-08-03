# 1

with open("first_task.txt", "w") as file:
    string = "ILY"

    for latter in range(1,1001):
        file.write(f'{latter} - {string}\n')

with open("first_task.txt", "r") as file:
    lines = file.readlines()
    print(f'Filled: {len(lines)} lines')

file.close()

# 2

with open("second_task.txt", "w") as second_file:
    for number in range(1, 101):
        if number == 2:
            second_file.write("second\n")
        elif number == 8:
            second_file.write("eighth\n")
        elif number == 10:
            second_file.write("tenth\n")
        elif number == 13:
            second_file.write("thirteenth\n")
        elif number == 17:
            second_file.write("seventeenth\n")
        else:
            second_file.write(str(number) + "\n")

second_file.close()


# 3

with open("first_folder_of_third_task.txt", "r", encoding="utf-8") as first_file:
    first_folder_of_third_task = first_file.read().strip()

first_file.close()

with open("second_folder_of_third_task.txt", "r", encoding="utf-8") as second_file:
    second_folder_of_third_task = second_file.read().strip()

second_file.close()

with open("third_folder_of_third_task.txt", "w", encoding="utf-8") as third_file:
    third_file.write(f"{first_folder_of_third_task}\n\n{second_folder_of_third_task}")

third_file.close()