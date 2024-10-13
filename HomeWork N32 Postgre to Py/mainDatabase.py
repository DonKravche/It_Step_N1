import psycopg2
from main import Book

host = 'localhost'
port = 5432
database = 'postgres'
user = 'postgres'
password = 'shHZB4bL'


def connect_to_db():
    try:
        connection = psycopg2.connect(host=host, port=port, database=database, user=user, password=password)
        print("მონაცემთა ბაზასთან კავშირი დამყარებულია")
        return connection
    except psycopg2.Error as e:
        print(f"მონაცემთა ბაზასთან დაკავშირება ვერ მოხერხდა: {e}")
        return None


def book_add(connection, book):
    cursor = connection.cursor()

    try:
        query = "insert into book (book_title, book_author, release_year, isbn) values (%s, %s, %s, %s)"
        cursor.execute(query, (book.title, book.author, book.release_year, book.isbn))
        connection.commit()
        print("წიგნი წარმატებით დაემატა!")
    except psycopg2.DatabaseError as database_error:
        print(f"მონაცემთა ბაზის შეცდომა: {database_error}")
        connection.rollback()


def read_all_data(connection):
    cursor = connection.cursor()

    try:
        cursor.execute("select * from book")
        data = cursor.fetchall()
        for book_data in data:
            book = Book(book_data[1], book_data[2], book_data[3], book_data[4])
            print(f"ID: {book_data[0]}, {book}")
    except psycopg2.Error as error:
        print(f"მონაცემთა ბაზის შეცდომა: {error}")


def search_book_by_isbn(connection):
    try:
        with connection.cursor() as cursor:
            isbn = input("შეიყვანეთ წიგნის ISBN კოდი: ")

            query = "select book_title, book_author, release_year, isbn from book where isbn = %s"
            cursor.execute(query, (isbn,))

            book_data = cursor.fetchone()

            if book_data:
                book = Book(*book_data)
                print("წიგნი ნაპოვნია:")
                print(book)
            else:
                print(f"წიგნი ISBN კოდით {isbn} ვერ მოიძებნა.")

    except psycopg2.Error as e:
        print(f"მონაცემთა ბაზის შეცდომა: {e}")


def update_book_by_id(connection):
    try:
        with connection.cursor() as cursor:
            user_input_id = input("შეიყვანეთ წიგნის ID, რომლის განახლებაც გსურთ: ")

            check_query = "select * from book where bookid = %s"
            cursor.execute(check_query, (user_input_id,))
            book_data = cursor.fetchone()

            if book_data:
                book = Book(book_data[1], book_data[2], book_data[3], book_data[4])
                print(f"ნაპოვნია წიგნი ID-ით {user_input_id}")
                print(f"არსებული დეტალები: {book}")

                new_title = input("შეიყვანეთ ახალი სათაური (ან დააჭირეთ Enter-ს უცვლელად დასატოვებლად): ") or book.title
                new_author = input(
                    "შეიყვანეთ ახალი ავტორი (ან დააჭირეთ Enter-ს უცვლელად დასატოვებლად): ") or book.author
                new_release_year = input(
                    "შეიყვანეთ ახალი გამოცემის წელი (ან დააჭირეთ Enter-ს უცვლელად დასატოვებლად): ") or book.release_year
                new_isbn = input("შეიყვანეთ ახალი ISBN (ან დააჭირეთ Enter-ს უცვლელად დასატოვებლად): ") or book.isbn

                query = "update book set book_title = %s, book_author = %s, release_year = %s, isbn = %s where bookid = %s"
                cursor.execute(query, (new_title, new_author, new_release_year, new_isbn, user_input_id))
                connection.commit()
                print("წიგნის დეტალები წარმატებით განახლდა!")
            else:
                print(f"წიგნი ID-ით {user_input_id} ვერ მოიძებნა.")

    except psycopg2.Error as e:
        print(f"მონაცემთა ბაზის შეცდომა: {e}")
        connection.rollback()


def delete_book_by_id(connection):
    try:
        with connection.cursor() as cursor:
            user_input_id = int(input("შეიყვანეთ წიგნის ID, რომლის წაშლაც გსურთ: "))

            check_query = "select * from book where bookid = %s"
            cursor.execute(check_query, (user_input_id,))
            book_data = cursor.fetchone()

            if book_data:
                book = Book(book_data[1], book_data[2], book_data[3], book_data[4])
                print(f"ნაპოვნია წიგნი ID-ით {user_input_id}")
                print(f"არსებული დეტალები: {book}")

                confirm = input("დარწმუნებული ხართ, რომ გსურთ ამ წიგნის წაშლა? (დიახ/არა): ")
                if confirm.lower() == 'დიახ':
                    query = "delete from book where bookid = %s"
                    cursor.execute(query, (user_input_id,))
                    connection.commit()
                    print("წიგნი წარმატებით წაიშალა მონაცემთა ბაზიდან!")
                else:
                    print("წიგნის წაშლა გაუქმდა.")
            else:
                print(f"წიგნი ID-ით {user_input_id} ვერ მოიძებნა.")
    except psycopg2.Error as e:
        print(f"მონაცემთა ბაზის შეცდომა: {e}")
        connection.rollback()
