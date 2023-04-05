from flask import Flask, request, jsonify
import datetime
import data_book as bk

app = Flask(__name__)

@app.route('/delete', methods=['POST'])
def delete_book():
    title = request.form.get('title')
    _book = bk.find_title(title)

    if _book:
        bk.delete_book(title)
        return jsonify({'message': 'Book deleted successfully'}), 200
    else: 
        return jsonify({'message': 'Book not found'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True) #127.0.0.1