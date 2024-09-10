import json
import pickle
import dill
from faker import Faker


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


fake = Faker()

students = [
    Student(fake.first_name(), fake.last_name(), fake.year(), fake.random_int(min=0, max=100))
    for _ in range(3)
]


def processing_data(student_object):
    try:
        with open("students.json", 'w') as file_json:
            json.dump(student_object.to_dict(), file_json, indent=4)
        print("Data has been successfully written to JSON!")
        return
    except Exception as error:
        print(f"Failed to write to JSON. Error: {error}")

    try:
        with open("students.pickle", "wb") as file_pickle:
            pickle.dump(student_object, file_pickle)
        print("Data has been successfully written using pickle!")
        return
    except Exception as error:
        print(f"Failed to write to Pickle. Error: {error}")

    try:
        with open("students.dill", "wb") as file_dill:
            dill.dump(student_object, file_dill)
        print("Data has been successfully written using dill!")
        return
    except Exception as error:
        print(f"Failed to write in Dill. Error: {error}")

    print("Unable to serialize the object using any method.")


processing_data(students)