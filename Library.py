# Name: Jeremy (蕭智強)
# ID: 10890402

import sqlite3
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

    # Update a book
    def update_book(self, isbn, book):
        self.cursor.execute(
            """
            UPDATE Books
            SET ISBN = :ISBN, title = :title, author = :author, publisher = :publisher, publication_date = :publication_date
            WHERE ISBN = :old
            """, (
                {
                    "ISBN": book.ISBN,
                    "title": book.title,
                    "author": book.author,
                    "publisher": book.publisher,
                    "publication_date": book.publication_date,
                    "old": isbn
                }
            )
        )
        self.conn.commit()

    # Delete a book
    def delete_book(self, ISBN):
        self.cursor.execute(
            """
            DELETE FROM Books
            WHERE ISBN = ISBN
            """
        )
        self.conn.commit()

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

    # Update an author
    def update_author(self, ID, author):
        self.cursor.execute(
            """
            UPDATE Authors
            SET(:ID, :name, :birth_date, :origin)
            WHERE ID = ID
            """, (
                {
                    "ID": author.ID,
                    "name": author.name,
                    "birth_date": author.birth_date,
                    "origin": author.origin
                }
            )
        )
        self.conn.commit()

    # Delete an author
    def delete_author(self, ID):
        self.cursor.execute(
            """
            DELETE FROM Authors
            WHERE ID = ID
            """
        )
        self.conn.commit()

    # Get all authors
    def get_authors(self):
        authors = []
        for author in self.conn.cursor.execute("SELECT * FROM Authors"):
            authors.append(Author(*author))
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

    # Update a publisher
    def update_publisher(self, ID, publisher):
        self.conn.cursor.execute(
            """
            UPDATE Publishers
            SET(:name, :address, :country)
            WHERE ID = ID
            """, (
                {
                    "ID": publisher.ID,
                    "name": publisher.name,
                    "address": publisher.address,
                    "country": publisher.country
                }
            )
        )
        self.conn.commit()

    # Delete a publisher
    def delete_publisher(self, ID):
        self.conn.cursor.execute(
            """
            DELETE FROM Publisher
            WHERE ID = ID
            """
        )
        self.conn.commit()

    # Get all publishers
    def get_publishers(self):
        publishers = []
        for publisher in self.conn.cursor.execute("SELECT * FROM Publisher"):
            publishers.append(Publisher(*publisher))
        return publishers

    ##########################################################
    ####################### BORROWERS ########################
    ##########################################################
    # Insert a borrower
    def insert_borrower(self, borrower):
        self.cursor.execute(
            """
            INSERT INTO Books
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
        print("books", self.get_books())

    # Update a book
    def update_borrower(self, ID, borrower):
        self.cursor.execute(
            """
            UPDATE Books
            SET(:ID, :name, :email, :contact_number)
            WHERE ID = ID
            """, (
                {
                    "ID": borrower.ID,
                    "name": borrower.name,
                    "email": borrower.email,
                    "contact_number": borrower.contact_number
                }
            )
        )
        self.conn.commit()

    # Delete a book
    def delete_borrower(self, ID):
        self.cursor.execute(
            """
            DELETE FROM Books
            WHERE ID = ID
            """
        )
        self.conn.commit()

    # Get all books
    def get_borrowers(self):
        borrowers = []
        for borrower in self.cursor.execute("SELECT * FROM Borrowers"):
            borrowers.append(Borrower(*borrower))
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
    Enter a number:"""))
    Lib1 = Library()
    if usr_input == 1:
        isbn = input("Enter ISBN number:")
        title = input("Enter title:")
        author = input("Enter author name:")
        pub = input("Enter publisher:")
        date = input("Enter publication date:")
        newBook = Book(title, author, pub, date, isbn)
        Lib1.insert_book(newBook)

    elif usr_input == 2:
        old_isbn = input("Enter the ISBN of the book you want to modify: ")
        isbn = input("Enter ISBN number:")
        title = input("Enter title:")
        author = input("Enter author name:")
        pub = input("Enter publisher:")
        date = input("Enter publication date:")
        new = Book(title, author, pub, date, isbn)
        Lib1.update_book(old_isbn, new)

    elif usr_input == 3:
        isbn = input("Enter the ISBN of the book you want to delete: ")
        Lib1.delete_book(isbn)

    elif usr_input == 4:
        print(Lib1.get_books())

    elif usr_input == 5:
        ID = input("Enter author ID number:")
        name = input("Enter author's name:")
        birth_date = input("Enter author's birth date:")
        origin = input("Enter author's origin:")
        newAuthor = Author(ID, name, birth_date, origin)
        Lib1.insert_author(newAuthor)

    elif usr_input == 6:
        old_id = input("Enter the ID of the author you want to modify: ")
        ID = input("Enter author ID number:")
        name = input("Enter author's name:")
        birth_date = input("Enter author's birth date:")
        origin = input("Enter author's origin:")
        newAuthor = Author(ID, name, birth_date, origin)
        Lib1.update_author(newAuthor)

    elif usr_input == 7:
        ID = input("Enter the ID of the author you want to delete: ")
        Lib1.delete_author(ID)

    elif usr_input == 8:
        print(Lib1.get_authors())

    else:
        pass

    # EXIT
    if usr_input != 17:
        continue_statement = input("Press ENTER to continue!")
        main()
    else:
        return

main()

