class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f'Deposited Successfully! Amount in account: {self.balance}'
        else:
            return 'Invalid deposit amount. Please enter a positive number.'

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return f'Withdrawn Successfully! Amount in account: {self.balance}'
            else:
                return 'Insufficient funds.'
        else:
            return 'Invalid withdraw amount. Please enter a positive number.'

    def get_balance(self):
        return f'Balance in account: {self.balance}'


user = BankAccount('1', 'Jack', 100000)
print(user.deposit(500))
print(user.withdraw(300))
print(user.get_balance())


class Student(object):
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)
        return f'{self.name} has been registered for {self.subjects}'

    def display_information(self):
        return f'Student ID: {self.student_id}, Name: {self.name}, Subjects: {self.subjects}'

    def display_course(self):
        if self.subjects:
            return f'Student {self.name} enrolled in:  {self.subjects}'
        else:
            return f'{self.name} is not enrolled in any courses yet'


student = Student('1', 'Jack')
print(student.add_subject('Python'))
print(student.add_subject('Java'))
print(student.display_course())
print(student.display_information())

student2 = Student('2', 'Emily')
print(student2.add_subject('Data Structures & algorithms'))
print(student2.add_subject('Kotlin'))
print(student.display_course())
print(student2.display_information())