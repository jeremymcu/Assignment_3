import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


def connect_to_db():
    conn = sqlite3.connect("Library.DB")
    return conn


# -----------------------------------------------------
# Books
# -----------------------------------------------------
# create book
def insert_book(book):
    inserted_books = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO Books
            VALUES(:ISBN, :title, :author, :publisher, :publication_date)
            """,
            (
                {
                    "ISBN": book['ISBN'],
                    "title": book['title'],
                    "author": book['author'],
                    "publisher": book['publisher'],
                    "publication_date": book['publication_date']
                }
            )
        )
        conn.commit()

        inserted_books = get_book_by_isbn(book['ISBN'])
    except:
        conn.rollback()
    finally:
        conn.close()

    return inserted_books


def get_book_by_isbn(isbn):
    book = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM Books WHERE ISBN = ?", (isbn,))
        i = cur.fetchone()

        # convert row object into dictionary
        book['ISBN'] = i['ISBN']
        book['title'] = i['title']
        book['author'] = i['author']
        book['publisher'] = i['publisher']
        book['publication_date'] = i['publication_date']
    except:
        book = {}
    finally:
        conn.close
    return book


# update book
def update_book(isbn, book):
    updated_book = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        if book['ISBN'] != "":
            cur.execute(
                """
                UPDATE Books
                SET ISBN = :ISBN
                WHERE ISBN = :old
                """, (
                    {
                        "ISBN": book['ISBN'],
                        "old": isbn
                    }
                )
            )
            conn.commit()
            ISBN = book['ISBN']
        if book['title'] != "":
            cur.execute(
                """
                UPDATE Books
                SET title = :title
                WHERE ISBN = :old
                """, (
                    {
                        "title": book['title'],
                        "old": isbn
                    }
                )
            )
            conn.commit()
        if book['author'] != "":
            cur.execute(
                """
                UPDATE Books
                SET author = :author
                WHERE ISBN = :old
                """, (
                    {
                        "author": book['author'],
                        "old": isbn
                    }
                )
            )
            conn.commit()
        if book['publisher'] != "":
            cur.execute(
                """
                UPDATE Books
                SET publisher = :publisher
                WHERE ISBN = :old
                """, (
                    {
                        "publisher": book['publisher'],
                        "old": isbn
                    }
                )
            )
            conn.commit()
        if book['publication_date'] != "":
            cur.execute(
                """
                UPDATE Books
                SET publication_date = :publication_date
                WHERE ISBN = :old
                """, (
                    {
                        "publication_date": book['publication_date'],
                        "old": isbn
                    }
                )
            )
            conn.commit()

        updated_book = get_book_by_isbn(isbn)
    except:
        conn.rollback()
    finally:
        conn.close()

    return updated_book

# delete book
def delete_book(ISBN):
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(
            """
            DELETE FROM Books
            WHERE ISBN = :ISBN
            """, (
                    {
                        "ISBN": ISBN
                    }
                )
        )
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()

    return 'Book deleted successfully'

# get books
def get_books():
    allBooks = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM Books")
        books = cur.fetchall()

        # convert row object into dictionary
        for i in books:
            book = {}
            book['ISBN'] = i['ISBN']
            book['title'] = i['title']
            book['author'] = i['author']
            book['publisher'] = i['publisher']
            book['publication_date'] = i['publication_date']
            allBooks.append(book)
    except:
        allBooks = []
    finally:
        conn.close
    return allBooks

@app.route('/api/books/add', methods=['POST'])
def addBook():
    book = request.get_json()
    return jsonify(insert_book(book))


@app.route('/api/books/update/<string:isbn>', methods=['PUT'])
def putBook(isbn):
    book = request.get_json()
    return jsonify(update_book(isbn, book))

@app.route('/api/books/delete/<string:isbn>', methods=['DELETE'])
def deleteBook(isbn):
    return delete_book(isbn)

@app.route('/api/books', methods=['GET'])
def getBooks():
    return get_books()


if __name__ == '__main__':
    app.run(debug=True)
