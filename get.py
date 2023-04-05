from flask import Flask, request, jsonify
import datetime
import data_book as bk

app = Flask(__name__)



@app.route('/book', methods=['GET'])
def get_book():
    book_list = bk.book_list()
    return jsonify(book_list)

@app.route('/book/<int:book_id>', methods=['GET'])
def get_single_book(book_id):
    book = bk.find_book(book_id)
    return jsonify(book)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
