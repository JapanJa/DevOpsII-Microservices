import sqlite3
import os

# File and path for database
db_folder = os.path.join(os.path.dirname(__file__), "db_books.db")

def book_list():
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT id, title, author, price, stock
        FROM books
        ORDER BY title
    """
    cursor = conn.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        record = {
            'id': row[0],
            'title': row[1],
            'author': row[2],
            'price': row[3],
            'stock': row[4]
        }
        data.append(record)
    
    conn.close()
    return data

def find_book(id):
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT id, title, author, price, stock
        FROM books
        WHERE id=?
    """
    val = (id,)
    cursor = conn.execute(sql,val)
    rows = cursor.fetchone()

    record = {
        'id': rows[0],
        'title': rows[1],
        'author': rows[2],
        'price': rows[3],
        'stock': rows[4]
    }
    data.append(record)
    
    conn.close()
    return data

def add_book(id,title,author,price,stock):
    conn = sqlite3.connect(db_folder)
    sql = """
        INSERT INTO books(id,title,author,price,stock)
        VALUES(?,?,?,?,?)
    """
    val = (id,title,author,price,stock)
    cursor = conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Book added successfully"


def delete_book(id):
    conn = sqlite3.connect(db_folder)
    sql = """
        DELETE FROM books
        WHERE id = ?
    """
    cursor = conn.execute(sql, (id,))
    conn.commit()
    conn.close()
    return "Book deleted successfully"

def update_book(id,title,author,price,stock):
    conn = sqlite3.connect(db_folder)
    sql = """
        UPDATE books SET title = ?, author = ?, price = ?, stock = ?
        WHERE id = ?
    """
    val = (title, author, price, stock, id)
    cursor = conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Book updated successfully"
