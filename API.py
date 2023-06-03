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

# -----------------------------------------------------
# Authors
# -----------------------------------------------------
def get_author_by_id(id):
    author = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM Authors WHERE ID = ?", (id,))
        i = cur.fetchone()

        # convert row object into dictionary
        author['ID'] = i['ID']
        author['name'] = i['name']
        author['birth_date'] = i['birth_date']
        author['origin'] = i['origin']
    except:
        author = {}
    finally:
        conn.close
    return author

# create author
def insert_author(author):
    inserted_author = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO Authors 
            VALUES(:ID, :name, :birth_date, :origin)
            """,
            (
                {
                    "ID": author['ID'],
                    "name": author['name'],
                    "birth_date": author['birth_date'],
                    "origin": author['origin']
                }
            )
        )
        conn.commit()

        inserted_author = get_author_by_id(author['ID'])
    except:
        conn.rollback()
    finally:
        conn.close()

    return inserted_author

# update author
def update_author(ID, author):
    updated_author = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        if author['ID'] != "":
            cur.execute(
                """
                UPDATE Authors
                SET ID = :ID
                WHERE ID = :old
                """, (
                    {
                        "ID": author['ID'],
                        "old": ID
                    }
                )
            )
            conn.commit()
            ID = author['ID']
        if author['name'] != "":
            cur.execute(
                """
                UPDATE Authors
                SET name = :name
                WHERE ID = :old
                """, (
                    {
                        "name": author['name'],
                        "old": ID
                    }
                )
            )
            conn.commit()
        if author['birth_date'] != "":
            cur.execute(
                """
                UPDATE Authors
                SET birth_date = :birth_date
                WHERE ID = :old
                """, (
                    {
                        "birth_date": author['birth_date'],
                        "old": ID
                    }
                )
            )
            conn.commit()
        if author['origin'] != "":
            cur.execute(
                """
                UPDATE Authors
                SET origin = :origin
                WHERE ID = :old
                """, (
                    {
                        "origin": author['origin'],
                        "old": ID
                    }
                )
            )
            conn.commit()

        updated_author = get_author_by_id(ID)
    except:
        conn.rollback()
    finally:
        conn.close()

    return updated_author

# delete author
def delete_author(ID):
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(
            """
            DELETE FROM Authors
            WHERE ID = :ID
            """, (
                    {
                        "ID": ID
                    }
                )
        )
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()

    return 'Author deleted successfully'

# get books
def get_authors():
    allAuthors = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM Authors")
        authors = cur.fetchall()

        # convert row object into dictionary
        for i in authors:
            author = {}
            author['ID'] = i['ID']
            author['name'] = i['name']
            author['birth_date'] = i['birth_date']
            author['origin'] = i['origin']
            allAuthors.append(author)
    except:
        allAuthors = []
    finally:
        conn.close
    return allAuthors

# -----------------------------------------------------
# Publishers
# -----------------------------------------------------
def get_publisher_by_id(id):
    publisher = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM Publishers WHERE ID = ?", (id,))
        i = cur.fetchone()

        # convert row object into dictionary
        publisher['ID'] = i['ID']
        publisher['name'] = i['name']
        publisher['address'] = i['address']
        publisher['country'] = i['country']
    except:
        publisher = {}
    finally:
        conn.close
    return publisher

# create publisher
def insert_publisher(publisher):
    inserted_publisher = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO Publishers 
            VALUES(:ID, :name, :address, :country)
            """,
            (
                {
                    "ID": publisher['ID'],
                    "name": publisher['name'],
                    "address": publisher['address'],
                    "country": publisher['country']
                }
            )
        )
        conn.commit()

        inserted_publisher = get_publisher_by_id(publisher['ID'])
    except:
        conn.rollback()
    finally:
        conn.close()

    return inserted_publisher

# update publisher
def update_publisher(ID, publisher):
    updated_publisher = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        if publisher['ID'] != "":
            cur.execute(
                """
                UPDATE Publishers
                SET ID = :ID
                WHERE ID = :old
                """, (
                    {
                        "ID": publisher['ID'],
                        "old": ID
                    }
                )
            )
            conn.commit()
            ID = publisher['ID']
        if publisher['name'] != "":
            cur.execute(
                """
                UPDATE Publishers
                SET name = :name
                WHERE ID = :old
                """, (
                    {
                        "name": publisher['name'],
                        "old": ID
                    }
                )
            )
            conn.commit()
        if publisher['address'] != "":
            cur.execute(
                """
                UPDATE Publishers
                SET address = :address
                WHERE ID = :old
                """, (
                    {
                        "address": publisher['address'],
                        "old": ID
                    }
                )
            )
            conn.commit()
        if publisher['country'] != "":
            cur.execute(
                """
                UPDATE Publishers
                SET country = :country
                WHERE ID = :old
                """, (
                    {
                        "country": publisher['country'],
                        "old": ID
                    }
                )
            )
            conn.commit()

        updated_publisher = get_publisher_by_id(ID)
    except:
        conn.rollback()
    finally:
        conn.close()

    return updated_publisher

# delete publisher
def delete_publisher(ID):
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(
            """
            DELETE FROM Publishers
            WHERE ID = :ID
            """, (
                    {
                        "ID": ID
                    }
                )
        )
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()

    return 'Publisher deleted successfully'

# get publisher
def get_publishers():
    allPublishers = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM Publishers")
        publishers = cur.fetchall()

        # convert row object into dictionary
        for i in publishers:
            publisher = {}
            publisher['ID'] = i['ID']
            publisher['name'] = i['name']
            publisher['address'] = i['address']
            publisher['country'] = i['country']
            allPublishers.append(publisher)
    except:
        allPublishers = []
    finally:
        conn.close
    return allPublishers

# -----------------------------------------------------
# Borrowers
# -----------------------------------------------------
def get_borrower_by_id(id):
    borrower = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM Borrowers WHERE ID = ?", (id,))
        i = cur.fetchone()

        # convert row object into dictionary
        borrower['ID'] = i['ID']
        borrower['name'] = i['name']
        borrower['email'] = i['email']
        borrower['contact_number'] = i['contact_number']
    except:
        borrower = {}
    finally:
        conn.close
    return borrower

# create publisher
def insert_borrower(borrower):
    inserted_borrower = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO Borrowers
            VALUES(:ID, :name, :email, :contact_number)
            """,
            (
                {
                    "ID": borrower['ID'],
                    "name": borrower['name'],
                    "email": borrower['email'],
                    "contact_number": borrower['contact_number']
                }
            )
        )
        conn.commit()

        inserted_borrower = get_borrower_by_id(borrower['ID'])
    except:
        conn.rollback()
    finally:
        conn.close()

    return inserted_borrower

# update publisher
def update_borrower(ID, borrower):
    updated_borrower = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        if borrower['ID'] != "":
            cur.execute(
                """
                UPDATE Borrowers
                SET ID = :ID
                WHERE ID = :old
                """, (
                    {
                        "ID": borrower['ID'],
                        "old": ID
                    }
                )
            )
            conn.commit()
            ID = borrower['ID']
        if borrower['name'] != "":
            cur.execute(
                """
                UPDATE Borrowers
                SET name = :name
                WHERE ID = :old
                """, (
                    {
                        "name": borrower['name'],
                        "old": ID
                    }
                )
            )
            conn.commit()
        if borrower['email'] != "":
            cur.execute(
                """
                UPDATE Borrowers
                SET email = :email
                WHERE ID = :old
                """, (
                    {
                        "email": borrower['email'],
                        "old": ID
                    }
                )
            )
            conn.commit()
        if borrower['contact_number'] != "":
            cur.execute(
                """
                UPDATE Borrowers
                SET contact_number = :contact_number
                WHERE ID = :old
                """, (
                    {
                        "ID": borrower['contact_number'],
                        "old": ID
                    }
                )
            )
            conn.commit()
    except:
        conn.rollback()
    finally:
        updated_borrower = get_borrower_by_id(ID)
        conn.close()

    return updated_borrower

# delete borrower
def delete_borrower(ID):
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(
            """
            DELETE FROM Borrowers
            WHERE ID = :ID
            """, (
                    {
                        "ID": ID
                    }
                )
        )
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()

    return 'Borrower deleted successfully'

# get borrowers
def get_borrowers():
    allBorrowers = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM Borrowers")
        borrowers = cur.fetchall()

        # convert row object into dictionary
        for i in borrowers:
            borrower = {}
            borrower['ID'] = i['ID']
            borrower['name'] = i['name']
            borrower['email'] = i['email']
            borrower['contact_number'] = i['contact_number']
            allBorrowers.append(borrower)
    except:
        allBorrowers = []
    finally:
        conn.close
    return allBorrowers



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>> APIs <<<<<<<<<<<<<<<<<<<<<<<
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>>>>>>>>> BOOKS <<<<<<<<<<<<<<<<<<<<<<
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

# >>>>>>>>>>>>>>>>>> AUTHORS <<<<<<<<<<<<<<<<<<<<
@app.route('/api/authors/add', methods=['POST'])
def addAuthor():
    author = request.get_json()
    return jsonify(insert_author(author))
@app.route('/api/authors/update/<string:ID>', methods=['PUT'])
def putAuthor(ID):
    author = request.get_json()
    return jsonify(update_author(ID, author))
@app.route('/api/authors/delete/<string:id>', methods=['DELETE'])
def deleteAuthor(id):
    return delete_author(id)
@app.route('/api/authors', methods=['GET'])
def getAuthors():
    return get_authors()


# >>>>>>>>>>>>>>>> PUBLISHERS <<<<<<<<<<<<<<<<<<
@app.route('/api/publishers/add', methods=['POST'])
def addPublisher():
    publisher = request.get_json()
    return jsonify(insert_publisher(publisher))
@app.route('/api/publishers/update/<string:id>', methods=['PUT'])
def putPublisher(id):
    publisher = request.get_json()
    return jsonify(update_publisher(id, publisher))
@app.route('/api/publishers/delete/<string:id>', methods=['DELETE'])
def deletePublisher(id):
    return delete_publisher(id)
@app.route('/api/publishers', methods=['GET'])
def getPublishers():
    return get_publishers()


# >>>>>>>>>>>>>>>> BORROWERS <<<<<<<<<<<<<<<<<<
@app.route('/api/borrowers/add', methods=['POST'])
def addBorrower():
    borrower = request.get_json()
    return jsonify(insert_borrower(borrower))
@app.route('/api/borrowers/update/<string:id>', methods=['PUT'])
def putBorrower(id):
    borrower = request.get_json()
    return jsonify(update_borrower(id, borrower))
@app.route('/api/borrowers/delete/<string:id>', methods=['DELETE'])
def deleteBorrower(id):
    return delete_borrower(id)
@app.route('/api/borrowers', methods=['GET'])
def getBorrowers():
    return get_borrowers()

if __name__ == '__main__':
    app.run(debug=True)
