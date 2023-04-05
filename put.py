from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_book as bk

app = Flask(__name__)

@app.route('/update', methods=['PUT'])
def update_book():
    # Get the book's information from the request
    bookname = request.form.get('bookname')
    price = request.form.get('price')
    stock = request.form.get('stock')

    # Check if the book exists in the database
    _book = bk.find_bookname(bookname)

    if _book:
        # Use an update query to update the book's information
        bk.update_book(bookname, price, stock)
        return jsonify({'message': 'Book updated successfully'}), 200
    else:
        return jsonify({'message': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True) #127.0.0.1
