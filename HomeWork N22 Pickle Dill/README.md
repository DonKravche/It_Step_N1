# Student Data Processing Project

This project demonstrates the creation and serialization of student objects using various methods (JSON, pickle, and dill) with a fallback mechanism.

## Project Description

The goal of this project is to create a `Student` class with attributes for name, surname, birth year, and grade. The program creates three different objects of this class and implements a function that attempts to serialize these objects using different methods.

## Features

- Creation of `Student` objects with random data using Faker
- Serialization attempts in the following order:
  1. JSON
  2. pickle
  3. dill
- Fallback mechanism: if one method fails, it tries the next
- Error handling and reporting

## Code Structure

### Student Class

```python
class Student:
    def __init__(self, name, surname, birth_year, grade):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.grade = grade

    def to_dict(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "birth_year": self.birth_year,
            "grade": self.grade
        }
```

### Creating Student Objects

```python
fake = Faker()

students = [
    Student(fake.first_name(), fake.last_name(), fake.year(), fake.random_int(min=0, max=100))
    for _ in range(3)
]
```

### Processing Function

```python
def processing_data(students_list):
    # JSON serialization attempt
    try:
        with open("students.json", 'w') as file_json:
            json.dump([student.to_dict() for student in students_list], file_json, indent=4)
        print("Data has been successfully written to JSON!")
        return
    except Exception as error:
        print(f"Failed to write to JSON. Error: {error}")

    # pickle serialization attempt
    try:
        with open("students.pickle", "wb") as file_pickle:
            pickle.dump(students_list, file_pickle)
        print("Data has been successfully written using pickle!")
        return
    except Exception as error:
        print(f"Failed to write to Pickle. Error: {error}")

    # dill serialization attempt
    try:
        with open("students.dill", "wb") as file_dill:
            dill.dump(students_list, file_dill)
        print("Data has been successfully written using dill!")
        return
    except Exception as error:
        print(f"Failed to write in Dill. Error: {error}")

    print("Unable to serialize the objects using any method.")
```

## Usage

To run the program:

1. Ensure you have the required libraries installed (`faker`, `dill`)
2. Run the script:
   ```
   python student_data_processing.py
   ```
3. The program will attempt to serialize the student objects and output the results.

## Error Handling

If all serialization methods fail, the program will output:
```
Unable to serialize the objects using any method.
```

## Dependencies

- Python 3.x
- Faker
- dill

## Note

This project is a demonstration of serialization techniques and error handling in Python. In a real-world scenario, you might want to implement more robust error handling and logging mechanisms.