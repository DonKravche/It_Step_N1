# 1

try:
    user_string_input = str(input("Enter a string: "))

    split_string = user_string_input.split()

    words_count = {}
    count = 0

    for word in split_string:
        if word in words_count:
            words_count[word] += 1
            count += 1
        else:
            words_count[word] = 1
            count = 1

    print(words_count)

except ValueError:
    print("Please enter only numbers.")


# 2

try:
    user_first_number_input = int(input("Enter a number: "))

    user_mathematical_operator_input = str(input("Enter a mathematical operator "
                                                 "(increment, decrement, multiply or divide): "))

    user_second_number_input = int(input("Enter a number: "))

    mathematical_operators = {
        'increment': lambda x, y: x + y,
        'decrement': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y,
    }

    if user_mathematical_operator_input in mathematical_operators:
        output = mathematical_operators[user_mathematical_operator_input](user_first_number_input,
                                                                          user_second_number_input)
        print(f"The result is: {output}")
    else:
        print("Invalid operator, choose from (increment, decrement, multiply or divide)")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


# 3

key_number_range = range(1, 11)
value = 0
number_dict = {}

for key in key_number_range:
    number_dict[key] = key
    number_dict.update({key: key ** 2})

print(number_dict)

# 4

company = {
    "HR": [
        {"name": "John", "surname": "Doe", "age": 35, "salary": 50000},
        {"name": "Jane", "surname": "Smith", "age": 28, "salary": 45000}
    ],
    "IT": [
        {"name": "Mike", "surname": "Johnson", "age": 40, "salary": 75000},
        {"name": "Sarah", "surname": "Williams", "age": 32, "salary": 70000},
        {"name": "Tom", "surname": "Brown", "age": 27, "salary": 60000}
    ],
    "Finance": [
        {"name": "Emily", "surname": "Davis", "age": 45, "salary": 80000},
        {"name": "David", "surname": "Wilson", "age": 38, "salary": 72000}
    ]
}

for department in company:
    total_salary = 0
    average_salary = 0
    for employee in company[department]:
        total_salary += employee["salary"]
        average_salary = total_salary / len(company[department])

    print(f"{department} average salary: {average_salary}")


# 5

def dict_function(dictionary):
    new_dictionary = {}
    for key, value in dictionary.items():
        new_dictionary[value] = key
    return new_dictionary


dictionary = {
    "apple": "A round fruit with red or green skin and crisp flesh",
    "book": "A written or printed work consisting of pages glued or sewn together",
    "computer": "An electronic device for storing and processing data",
    "dog": "A domesticated carnivorous mammal",
    "elephant": "A very large plant-eating mammal with a trunk and tusks",
    "flower": "The seed-bearing part of a plant",
    "guitar": "A musical instrument with strings",
    "house": "A building for human habitation",
    "internet": "A global computer network providing information and communication",
    "jacket": "An outer garment extending either to the waist or the hips"
}

result = dict_function(dictionary)
print(result)