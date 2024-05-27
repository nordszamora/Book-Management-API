from flask import Blueprint, request, jsonify

from app.models import Book
from . import db

rest_api = Blueprint('blue_print', __name__)

@rest_api.route('/books', methods=['GET', 'POST'])
def book_list():
    # Read list of books
    if request.method == 'GET':
       list_of_books = Book.query.all()

       books = []
       for book in list_of_books:
           books.append({
              'id': book.id,
              'isbn': book.isbn,
              'title': book.title,
              'author': book.author,
              'genre': book.genre,
              'year': book.year,
              'publisher': book.publisher,
              'quantity': book.quantity,
              'price': book.price
           })

       return jsonify(books), 200

    # Add new book
    elif request.method == 'POST':
       add_book = Book(
          isbn = request.json.get('isbn'),
          title = request.json.get('title'),
          author = request.json.get('author'),
          genre = request.json.get('genre'),
          year = request.json.get('year'),
          publisher = request.json.get('publisher'),
          quantity = request.json.get('quantity'),
          price = request.json.get('price')
       )

       db.session.add(add_book)
       db.session.commit()

       return jsonify({'message': 'Book added!'}), 201

@rest_api.route('/books/<isbn>', methods=['GET', 'PUT', 'DELETE'])
def books(isbn):
    # Read single book
    if request.method == 'GET':
       book = Book.query.filter_by(isbn=isbn).first()

       return jsonify({
           'id': book.id,
           'isbn': book.isbn,
           'title': book.title,
           'author': book.author,
           'genre': book.genre,
           'year': book.year,
           'publisher': book.publisher,
           'quantity': book.quantity,
           'price': book.price
       }), 200
    
    # Update book
    elif request.method == 'PUT':
        update_book = Book.query.filter_by(isbn=isbn).first()

        update_book.isbn = request.json.get('isbn')
        update_book.title = request.json.get('title')
        update_book.author = request.json.get('author')
        update_book.genre = request.json.get('genre')
        update_book.year = request.json.get('year')
        update_book.publisher = request.json.get('publisher')
        update_book.quantity = request.json.get('quantity')
        update_book.price = request.json.get('price')

        db.session.add(update_book)
        db.session.commit()

        return jsonify({'message': 'Book updated!'}), 201
    
    # Delete book
    elif request.method == 'DELETE':
        delete_book = Book.query.filter_by(isbn=isbn).first()

        db.session.delete(delete_book)
        db.session.commit()

        return jsonify({'message': 'Book deleted!'}), 200
    