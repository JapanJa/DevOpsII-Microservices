from flask import Flask, request, jsonify
import datetime
import data_book as bk

app = Flask(__name__)

@app.route('/book/register', methods=['POST'])
def register():
    # Get the book information from the request
    title = request.form.get('title')
    author = request.form.get('author')
    price = request.form.get('price')
    stock = request.form.get('stock')

    # Check if the book already exists in the database
    books = bk.book_name()
    data = [x for x in books if x["title"] == title]
    if data:
        return jsonify({'message': 'Cannot create book - book already exists.'}), 401

    # Add the new book to the database
    bk.book_add(title, author, price, stock)
    return jsonify({'message': 'Book created successfully.'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
