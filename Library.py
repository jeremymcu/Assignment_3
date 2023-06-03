# Name: Jeremy (蕭智強)
# ID: 10890402

import sqlite3
from IPython.display import clear_output
import os
# from flask import Flask, request, jsonify
# from flask_cors import CORS


class Book:
    def __init__(self, title, author, publisher, publication_date, ISBN):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date
        self.ISBN = ISBN


class Author:
    def __init__(self, ID, name, birth_date, origin):
        self.ID = ID
        self.name = name
        self.birth_date = birth_date
        self.origin = origin


class Publisher:
    def __init__(self, ID, name, address, country):
        self.ID = ID
        self.name = name
        self.address = address
        self.country = country


class Borrower:
    def __init__(self, ID, name, email, contact_number):
        self.ID = ID
        self.name = name
        self.email = email
        self.contact_number = contact_number


class Library:
    conn = sqlite3.connect("Library.DB")
    print("'Library' Database created successfully!")
    cursor = conn.cursor()
    conn.commit()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Books(
            ISBN TEXT PRIMARY KEY NOT NULL,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publisher TEXT NOT NULL,
            publication_date TEXT NOT NULL
        )
        """
    )
    conn.commit()
    print("'Books' table is created successfully")

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Authors(
            ID INTEGER PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            birth_date TEXT NOT NULL,
            origin TEXT NOT NULL
        )
        """
    )
    conn.commit()
    print("'Author' table is created successfully")

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Publishers(
            ID INTEGER PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            country TEXT NOT NULL
        )
        """
    )
    conn.commit()
    print("'Publisher' table is created successfully")

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Borrowers(
            ID INTEGER PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            contact_number TEXT NOT NULL
        )
        """
    )
    conn.commit()
    print("'Borrower' table is created successfully")

    ##########################################################
    ######################### BOOKS ##########################
    ##########################################################
    # Insert a book
    def insert_book(self, book):
        self.cursor.execute(
            """
            INSERT INTO Books
            VALUES(:ISBN, :title, :author, :publisher, :publication_date)
            """,
            (
                    {
                        "ISBN": book.ISBN,
                        "title": book.title,
                        "author": book.author,
                        "publisher": book.publisher,
                        "publication_date": book.publication_date
                    }
            )
        )
        self.conn.commit()
        print("Book {} has been added successfully!".format(book.ISBN))

    # Update a book
    def update_book(self, isbn, book):
        if book.ISBN != "":
            self.cursor.execute(
                """
                UPDATE Books
                SET ISBN = :ISBN
                WHERE ISBN = :old
                """, (
                    {
                        "ISBN": book.ISBN,
                        "old": isbn
                    }
                )
            )
            self.conn.commit()
            isbn = book.ISBN
        if book.title != "":
            self.cursor.execute(
                """
                UPDATE Books
                SET title = :title
                WHERE ISBN = :old
                """, (
                    {
                        "title": book.title,
                        "old": isbn
                    }
                )
            )
            self.conn.commit()
        if book.author != "":
            self.cursor.execute(
                """
                UPDATE Books
                SET author = :author
                WHERE ISBN = :old
                """, (
                    {
                        "author": book.author,
                        "old": isbn
                    }
                )
            )
            self.conn.commit()
        if book.publisher != "":
            self.cursor.execute(
                """
                UPDATE Books
                SET publisher = :publisher
                WHERE ISBN = :old
                """, (
                    {
                        "publisher": book.publisher,
                        "old": isbn
                    }
                )
            )
            self.conn.commit()
        if book.publication_date != "":
            self.cursor.execute(
                """
                UPDATE Books
                SET publication_date = :publication_date
                WHERE ISBN = :old
                """, (
                    {
                        "publication_date": book.publication_date,
                        "old": isbn
                    }
                )
            )
            self.conn.commit()
        print("Book {} has been updated successfully!".format(isbn))

    # Delete a book
    def delete_book(self, ISBN):
        self.cursor.execute(
            """
            DELETE FROM Books
            WHERE ISBN = :ISBN
            """, (
                    {
                        "ISBN": ISBN
                    }
                )
        )
        self.conn.commit()
        print("Book {} has been deleted successfully!".format(ISBN))

    # Get all books
    def get_books(self):
        books = []
        for book in self.cursor.execute("SELECT * FROM Books"):
            books.append(book)
        return books

    ##########################################################
    ######################### AUTHOR #########################
    ##########################################################
    # Insert an author
    def insert_author(self, author):
        self.cursor.execute(
            """
            INSERT INTO Authors 
            VALUES(:ID, :name, :birth_date, :origin)
            """,
            (
                {
                    "ID": author.ID,
                    "name": author.name,
                    "birth_date": author.birth_date,
                    "origin": author.origin
                }
            )
        )
        self.conn.commit()
        print("Author {} has been added successfully!".format(author.ID))

    # Update an author
    def update_author(self, ID, author):
        if author.ID != "":
            self.cursor.execute(
                """
                UPDATE Authors
                SET ID = :ID
                WHERE ID = :old
                """, (
                    {
                        "ID": author.ID,
                        "old": ID
                    }
                )
            )
            self.conn.commit()
            ID = author.ID
        if author.name != "":
            self.cursor.execute(
                """
                UPDATE Authors
                SET name = :name
                WHERE ID = :old
                """, (
                    {
                        "name": author.name,
                        "old": ID
                    }
                )
            )
            self.conn.commit()
        if author.birth_date != "":
            self.cursor.execute(
                """
                UPDATE Authors
                SET birth_date = :birth_date
                WHERE ID = :old
                """, (
                    {
                        "birth_date": author.birth_date,
                        "old": ID
                    }
                )
            )
            self.conn.commit()
        if author.origin != "":
            self.cursor.execute(
                """
                UPDATE Authors
                SET origin = :origin
                WHERE ID = :old
                """, (
                    {
                        "origin": author.origin,
                        "old": ID
                    }
                )
            )
            self.conn.commit()
        print("Author {} has been updated successfully!".format(ID))

    # Delete an author
    def delete_author(self, ID):
        self.cursor.execute(
            """
            DELETE FROM Authors
            WHERE ID = :ID
            """, (
                    {
                        "ID": ID
                    }
                )
        )
        self.conn.commit()
        print("Author {} has been deleted successfully!".format(ID))

    # Get all authors
    def get_authors(self):
        authors = []
        for author in self.cursor.execute("SELECT * FROM Authors"):
            authors.append(author)
        return authors

    ##########################################################
    ####################### PUBLISHER ########################
    ##########################################################
    # Insert a publisher
    def insert_publisher(self, publisher):
        self.cursor.execute(
            """
            INSERT INTO Publishers 
            VALUES(:ID, :name, :address, :country)
            """,
            (
                {
                    "ID": publisher.ID,
                    "name": publisher.name,
                    "address": publisher.address,
                    "country": publisher.country
                }
            )
        )
        self.conn.commit()
        print("Publisher {} has been inserted successfully!".format(publisher.ID))

    # Update a publisher
    def update_publisher(self, ID, publisher):
        if publisher.ID != "":
            self.cursor.execute(
                """
                UPDATE Publishers
                SET ID = :ID
                WHERE ID = :old
                """, (
                    {
                        "ID": publisher.ID,
                        "old": ID
                    }
                )
            )
            self.conn.commit()
            ID = publisher.ID
        if publisher.name != "":
            self.cursor.execute(
                """
                UPDATE Publishers
                SET name = :name
                WHERE ID = :old
                """, (
                    {
                        "name": publisher.name,
                        "old": ID
                    }
                )
            )
            self.conn.commit()
        if publisher.address != "":
            self.cursor.execute(
                """
                UPDATE Publishers
                SET address = :address
                WHERE ID = :old
                """, (
                    {
                        "address": publisher.address,
                        "old": ID
                    }
                )
            )
            self.conn.commit()
        if publisher.country != "":
            self.cursor.execute(
                """
                UPDATE Publishers
                SET country = :country
                WHERE ID = :old
                """, (
                    {
                        "country": publisher.country,
                        "old": ID
                    }
                )
            )
            self.conn.commit()
        print("Publisher {} has been updated successfully!".format(ID))

    # Delete a publisher
    def delete_publisher(self, ID):
        self.conn.cursor.execute(
            """
            DELETE FROM Publisher
            WHERE ID = ID
            """, (
                    {
                        "ID": ID
                    }
                )
        )
        self.conn.commit()
        print("Publisher {} has been deleted successfully!".format(ID))

    # Get all publishers
    def get_publishers(self):
        publishers = []
        for publisher in self.cursor.execute("SELECT * FROM Publishers"):
            publishers.append(publisher)
        return publishers

    ##########################################################
    ####################### BORROWERS ########################
    ##########################################################
    # Insert a borrower
    def insert_borrower(self, borrower):
        self.cursor.execute(
            """
            INSERT INTO Borrowers
            VALUES(:ID, :name, :email, :contact_number)
            """,
            (
                {
                    "ID": borrower.ID,
                    "name": borrower.name,
                    "email": borrower.email,
                    "contact_number": borrower.contact_number
                }
            )
        )
        self.conn.commit()
        print("Borrower {} has been added successfully!".format(borrower.ID))

    # Update a book
    def update_borrower(self, ID, borrower):
        if borrower.ID != "":
            self.cursor.execute(
                """
                UPDATE Borrowers
                SET ID = :ID
                WHERE ID = :old
                """, (
                    {
                        "ID": borrower.ID,
                        "old": ID
                    }
                )
            )
            self.conn.commit()
            ID = borrower.ID
        if borrower.name != "":
            self.cursor.execute(
                """
                UPDATE Borrowers
                SET name = :name
                WHERE ID = :old
                """, (
                    {
                        "name": borrower.name,
                        "old": ID
                    }
                )
            )
            self.conn.commit()
        if borrower.email != "":
            self.cursor.execute(
                """
                UPDATE Borrowers
                SET email = :email
                WHERE ID = :old
                """, (
                    {
                        "email": borrower.email,
                        "old": ID
                    }
                )
            )
            self.conn.commit()
        if borrower.contact_number != "":
            self.cursor.execute(
                """
                UPDATE Borrowers
                SET contact_number = :contact_number
                WHERE ID = :old
                """, (
                    {
                        "ID": borrower.contact_number,
                        "old": ID
                    }
                )
            )
            self.conn.commit()
        print("Borrower {} has been updated successfully!".format(ID))

    # Delete a book
    def delete_borrower(self, ID):
        self.cursor.execute(
            """
            DELETE FROM Books
            WHERE ID = ID
            """, (
                    {
                        "ID": ID
                    }
                )
        )
        self.conn.commit()
        print("Borrower {} has been deleted successfully!".format(ID))

    # Get all books
    def get_borrowers(self):
        borrowers = []
        for borrower in self.cursor.execute("SELECT * FROM Borrowers"):
            borrowers.append(borrower)
        return borrowers

# if __name__ == '__main__':
def main():
    usr_input = int(input("""\
    [1]. Insert book
    [2]. Update book
    [3]. Delete book
    [4]. Get books
    [5]. Insert Author
    [6]. Update Author
    [7]. Delete Author
    [8]. Get Author
    [9]. Insert Publisher
    [10]. Update Publisher
    [11]. Delete Publisher
    [12]. Get Publishers
    [13]. Insert Borrower
    [14]. Update Borrower
    [15]. Delete Borrower
    [16]. Get Borrower
    [17]. EXIT
    Enter a number: """))
    Lib1 = Library()

    # Clear output
    clear_output()  # method 1
    os.system('cls' if os.name == 'nt' else 'clear')  # backup if method 1 fails

    match usr_input:
        # -----------------------------------------------------
        # Books
        # -----------------------------------------------------
        # create book
        case 1:
            isbn = input("Enter ISBN number: ")
            title = input("Enter title: ")
            author = input("Enter author name: ")
            pub = input("Enter publisher: ")
            date = input("Enter publication date: ")
            newBook = Book(title, author, pub, date, isbn)
            Lib1.insert_book(newBook)

        # update book
        case 2:
            # Display the list of objects in the table
            print("-" * 100)
            print(f"{'Books':^100}")
            print("-" * 100)
            for each in Lib1.get_books():
                print(each)
            old_isbn = input("Enter the ISBN of the book you want to modify: ")

            # Clear output
            clear_output() #method 1
            os.system('cls' if os.name == 'nt' else 'clear') #backup if method 1 fails

            isbn = input("Enter ISBN number: ")
            title = input("Enter title: ")
            author = input("Enter author name: ")
            pub = input("Enter publisher: ")
            date = input("Enter publication date: ")
            new = Book(title, author, pub, date, isbn)
            Lib1.update_book(old_isbn, new)

        # delete book
        case 3:
            # Display the list of objects in the table
            print("-" * 100)
            print(f"{'Books':^100}")
            print("-" * 100)
            for each in Lib1.get_books():
                print(each)
            isbn = input("Enter the ISBN of the book you want to delete: ")

            # Clear output
            clear_output()  # method 1
            os.system('cls' if os.name == 'nt' else 'clear')  # backup if method 1 fails

            Lib1.delete_book(isbn)

        # get book
        case 4:
            print("-" * 100)
            print(f"{'Books':^100}")
            print("-" * 100)
            for each in Lib1.get_books():
                print(each)
        # -----------------------------------------------------
        # Authors
        # -----------------------------------------------------
        # create author
        case 5:
            ID = input("Enter author ID number: ")
            name = input("Enter author's name: ")
            birth_date = input("Enter author's birth date: ")
            origin = input("Enter author's origin: ")
            newAuthor = Author(ID, name, birth_date, origin)
            Lib1.insert_author(newAuthor)

        # update author
        case 6:
            # Display the list of objects in the table
            print("-" * 100)
            print(f"{'Authors':^100}")
            print("-" * 100)
            for each in Lib1.get_authors():
                print(each)
            old_id = input("Enter the ID of the author you want to modify: ")

            # Clear output
            clear_output()  # method 1
            os.system('cls' if os.name == 'nt' else 'clear')  # backup if method 1 fails

            ID = input("Enter author ID number: ")
            name = input("Enter author's name: ")
            birth_date = input("Enter author's birth date: ")
            origin = input("Enter author's origin: ")
            newAuthor = Author(ID, name, birth_date, origin)
            Lib1.update_author(old_id, newAuthor)

        # delete author
        case 7:
            # Display the list of objects in the table
            print("-" * 100)
            print(f"{'Authors':^100}")
            print("-" * 100)
            for each in Lib1.get_authors():
                print(each)
            ID = input("Enter the ID of the author you want to delete: ")

            # Clear output
            clear_output()  # method 1
            os.system('cls' if os.name == 'nt' else 'clear')  # backup if method 1 fails

            Lib1.delete_author(ID)

        # get author
        case 8:
            print("-" * 100)
            print(f"{'Authors':^100}")
            print("-" * 100)
            for each in Lib1.get_authors():
                print(each)

        # -----------------------------------------------------
        # Publishers
        # -----------------------------------------------------
        # create publisher
        case 9:
            ID = input("Enter publisher's ID number: ")
            name = input("Enter publisher's name: ")
            address = input("Enter publisher's address: ")
            country = input("Enter publisher's country: ")
            newPub = Publisher(ID, name, address, country)
            Lib1.insert_publisher(newPub)

        # update publisher
        case 10:
            # Display the list of objects in the table
            print("-" * 100)
            print(f"{'Publishers':^100}")
            print("-" * 100)
            for each in Lib1.get_publishers():
                print(each)
            old_id = input("Enter the ID of the publisher you want to modify: ")

            # Clear output
            clear_output()  # method 1
            os.system('cls' if os.name == 'nt' else 'clear')  # backup if method 1 fails

            ID = input("Enter publisher's ID number: ")
            name = input("Enter publisher's name: ")
            address = input("Enter publisher's address: ")
            country = input("Enter publisher's country: ")
            newPub = Publisher(ID, name, address, country)
            Lib1.update_publisher(old_id, newPub)

        # delete publisher
        case 11:
            # Display the list of objects in the table
            print("-" * 100)
            print(f"{'Publishers':^100}")
            print("-" * 100)
            for each in Lib1.get_publishers():
                print(each)
            ID = input("Enter the ID of the borrower you want to delete: ")

            # Clear output
            clear_output()  # method 1
            os.system('cls' if os.name == 'nt' else 'clear')  # backup if method 1 fails

            Lib1.delete_publisher(ID)

        # get publisher
        case 12:
            print("-" * 100)
            print(f"{'Publishers':^100}")
            print("-" * 100)
            for each in Lib1.get_publishers():
                print(each)

        # -----------------------------------------------------
        # Borrowers
        # -----------------------------------------------------
        # create borrower
        case 13:
            ID = input("Enter borrower's ID number: ")
            name = input("Enter borrower's name: ")
            email = input("Enter borrower's email: ")
            contact = input("Enter borrower's contact number: ")
            newBorrower = Borrower(ID, name, email, contact)
            Lib1.insert_borrower(newBorrower)

        # update borrower
        case 14:
            # Display the list of objects in the table
            print("-" * 100)
            print(f"{'Borrowers':^100}")
            print("-" * 100)
            for each in Lib1.get_borrowers():
                print(each)
            old_id = input("Enter the ID of the borrower you want to modify: ")

            # Clear output
            clear_output()  # method 1
            os.system('cls' if os.name == 'nt' else 'clear')  # backup if method 1 fails

            ID = input("Enter borrower's ID number: ")
            name = input("Enter borrower's name: ")
            email = input("Enter borrower's email: ")
            contact = input("Enter borrower's contact number: ")
            newBorrower = Borrower(ID, name, email, contact)
            Lib1.update_borrower(old_id, newBorrower)

        # delete borrower
        case 15:
            # Display the list of objects in the table
            print("-" * 100)
            print(f"{'Borrowers':^100}")
            print("-" * 100)
            for each in Lib1.get_borrowers():
                print(each)
            ID = input("Enter the ID of the borrower you want to delete: ")

            # Clear output
            clear_output()  # method 1
            os.system('cls' if os.name == 'nt' else 'clear')  # backup if method 1 fails

            Lib1.delete_borrower(ID)

        # get borrower
        case 16:
            print("-" * 100)
            print(f"{'Borrowers':^100}")
            print("-" * 100)
            for each in Lib1.get_borrowers():
                print(each)

        case default:
            pass

    # EXIT
    if usr_input != 17:
        continue_statement = input("Press ENTER to continue!")

        # Clear output
        clear_output()  # method 1
        os.system('cls' if os.name == 'nt' else 'clear')  # backup if method 1 fails

        main()
    else:
        return

if __name__ == '__main__':
    main()

