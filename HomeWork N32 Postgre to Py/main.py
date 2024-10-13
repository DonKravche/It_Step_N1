import mainDatabase


class Book:
    def __init__(self, title, author, release_year, isbn):
        self.title = title
        self.author = author
        self.release_year = release_year
        self.isbn = isbn

    def __str__(self):
        return f"სათაური: {self.title}, ავტორი: {self.author}, გამოცემის წელი: {self.release_year}, ISBN: {self.isbn}"


def main():
    connection = mainDatabase.connect_to_db()
    if not connection:
        return

    while True:
        print("\nმოგესალმებით! რით შეგვიძლია დაგეხმაროთ?")
        print("1) ახალი წიგნის დამატება")
        print("2) ყველა წიგნის წაკითხვა")
        print("3) წიგნის ძიება ISBN-ით")
        print("4) წიგნის ატრიბუტების ცვლილება")
        print("5) წიგნის ამოშლა")
        print("0) გასვლა")

        choice = input("შეიყვანეთ შესაბამისი ციფრი -> ")

        if choice == '0':
            print("კავშირი გაუქმდა")
            break
        elif choice == '1':
            title = input("გთხოვთ შეიყვანოთ წიგნის სათაური: ")
            author = input("გთხოვთ შეიყვანოთ ავტორი: ")
            release_year = int(input("გთხოვთ შეიყვანოთ გამოშვების წელი: "))
            isbn = input("გთხოვთ შეიყვანოთ წიგნის ISBN კოდი: ")
            new_book = Book(title, author, release_year, isbn)
            mainDatabase.book_add(connection, new_book)
        elif choice == '2':
            mainDatabase.read_all_data(connection)
        elif choice == '3':
            mainDatabase.search_book_by_isbn(connection)
        elif choice == '4':
            mainDatabase.update_book_by_id(connection)
        elif choice == '5':
            mainDatabase.delete_book_by_id(connection)
        else:
            print("არასწორი პარამეტრები! ამოირჩიეთ სიიდან!")

    connection.close()


if __name__ == "__main__":
    main()
