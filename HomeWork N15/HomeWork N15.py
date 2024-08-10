# 1

def read_file():
    file = open('homework.txt', 'r')
    file_read = file.read()
    words = file_read.split()

    for palindrome_word in words:
        if len(palindrome_word) > 1 and palindrome_word == palindrome_word[::-1]:
            print(palindrome_word)
        else:
            pass

    file.close()


print(read_file())

# 2

def writeTenLine():
    with open("homework.txt", "r") as file:
        lines = file.readlines()
        line_size = 10

        for line in range(0, len(lines), line_size):
            size = lines[line:line + line_size]
            output_filename = f"tenLinedHomework_{line // line_size + 1}.txt"
            with open(output_filename, "w") as splitTenLine:
                splitTenLine.writelines(size)
    file.close()


writeTenLine()


# 3

def read_files():
    fileList = [
        'tenLinedHomework_1.txt',
        'tenLinedHomework_2.txt',
        'tenLinedHomework_3.txt',
    ]

    with open('output.txt', 'w') as output_file:
        for fileName in fileList:
            with open(fileName, 'r') as f:
                for line in f:
                    if line.strip():
                        output_file.write(line)


read_files()

output_file = open('output.txt', 'r')
output_file.close()

# 4

import csv
import os

starting_data = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "Moby Dick", "author": "Herman Melville", "year": 1851},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"title": "War and Peace", "author": "Leo Tolstoy", "year": 1869},
    {"title": "Ulysses", "author": "James Joyce", "year": 1922},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
]


def create_initial_file():
    with open('books.csv', 'w', newline='') as books_file:
        writer = csv.writer(books_file)
        writer.writerow(['title', 'author', 'year'])
        for book in starting_data:
            writer.writerow([book['title'], book['author'], book['year']])
    print("Initial books.csv created successfully!")


def user_add_book(title, author, year):
    new_book = {"title": title, "author": author, "year": year}
    starting_data.append(new_book)
    print(f"Added: {title} by {author} ({year})")


def read_book_info(title):
    for book in starting_data:
        if book['title'].lower() == title.lower():
            return f"Reading: {book['title']} by {book['author']} ({book['year']})"
    return "Sorry, the book you entered does not exist."


def update_csv():
    with open('books.csv', 'w', newline='') as books_file:
        writer = csv.writer(books_file)
        writer.writerow(['title', 'author', 'year'])
        for book in starting_data:
            writer.writerow([book['title'], book['author'], book['year']])
    print("Books.csv updated successfully!")


user_input = input(
    "Hello, how can I help you? Do you want to write or read information? Write (write or read) in the field: ").lower()

if user_input == 'write':
    try:
        title = input("What is your title? ")
        author = input("What is the author's name? ")
        year = int(input("What is the year? "))
        user_add_book(title, author, year)
        update_csv()
    except ValueError:
        print("Please enter a valid year!")
elif user_input == 'read':
    if not os.path.exists('books.csv'):
        create_initial_file()
    user_input2 = input("Please enter book title to read information: ")
    print(read_book_info(user_input2))
else:
    print("Invalid input. Please enter 'write' or 'read'.")
