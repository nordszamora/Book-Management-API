from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow import ValidationError
from flask_jwt_extended import (
    jwt_required, 
    create_access_token,
    get_jwt
)

from app.schema import AuthSchema, BookSchema
from app.models import Auth, Book
from . import jwt
from . import db

rest_api = Blueprint('blue_print', __name__)

@rest_api.route('/token/register', methods=['POST'])
def register():
    # Register new user
    auth_schema = AuthSchema()

    try:
      validated_data = auth_schema.load(request.json)

      username = validated_data['username']
      password = validated_data['password']
      if Auth.query.filter_by(username=username).first():
         return jsonify({'message': 'User already taken.'})
      
      hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

      new_account = Auth(
         username = username,
         password = hashed_password
      )

      db.session.add(new_account)
      db.session.commit()

      return jsonify({'message': 'Account registered.'})

    except ValidationError as error:
      return jsonify(error.messages), 400

@rest_api.route('/token/login', methods=['POST'])
def login():
    # Login user
    username = request.json.get('username')
    password = request.json.get('password')

    auth = Auth.query.filter_by(username=username).first()

    if auth and check_password_hash(auth.password, password):
       access_token = create_access_token(identity=username)
       return jsonify(access_token=access_token)
    
    return jsonify({'message': 'Incorrect credentials.'}), 401

blacklist = set()

@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in blacklist

@rest_api.route('/token/logout', methods=['POST'])
@jwt_required()
def logout():
    # Destroy token
    jti = get_jwt()['jti']
    blacklist.add(jti)
    return jsonify({'message': 'Log out.'}), 200

@rest_api.route('/books', methods=['GET', 'POST'])
def book_list():
    # Read list of books
    if request.method == 'GET':
       list_of_books = Book.query.all()

       book_schema = BookSchema(many=True)
       result = book_schema.dump(list_of_books)
       return jsonify(result), 200

    # Add new book
    elif request.method == 'POST':
       @jwt_required()
       def add_new_book():
           book_schema = BookSchema()

           try:
             validated_data = book_schema.load(request.json)

             if Book.query.filter_by(isbn=validated_data['isbn']).first():
                return jsonify({'message': 'ISBN must not be duplicated.'})

             add_book = Book(
                isbn = validated_data['isbn'],
                title = validated_data['title'],
                author = validated_data['author'],
                genre = validated_data['genre'],
                year = validated_data['year'],
                publisher = validated_data['publisher'],
                quantity = validated_data['quantity'],
                price = validated_data['price']
             )

             db.session.add(add_book)
             db.session.commit()

             return jsonify({'Book added': book_schema.dump(add_book)}), 201
           except ValidationError as error:
             return jsonify(error.messages), 400
        
       return add_new_book()
       
@rest_api.route('/books/<isbn>', methods=['GET', 'PUT', 'DELETE'])
def books(isbn):
    # Read single book
    if request.method == 'GET':
       book = Book.query.filter_by(isbn=isbn).first()

       book_schema = BookSchema()
       result = book_schema.dump(book)
       return jsonify(result), 200
    
    # Update book
    elif request.method == 'PUT':
        @jwt_required()
        def edit_book():
            update_book = Book.query.filter_by(isbn=isbn).first()
            
            book_schema = BookSchema()

            try:
              validated_data = book_schema.load(request.json)

              update_book.isbn = validated_data['isbn']
              update_book.title = validated_data['title']
              update_book.author = validated_data['author']
              update_book.genre = validated_data['genre']
              update_book.year = validated_data['year']
              update_book.publisher = validated_data['publisher']
              update_book.quantity = validated_data['quantity']
              update_book.price = validated_data['price']

              db.session.add(update_book)
              db.session.commit()

              return jsonify({'message': 'Book updated!'}), 201
            except ValidationError as error:
              return jsonify(error.messages), 400
            
        return edit_book()
        
    # Delete book
    elif request.method == 'DELETE':
        @jwt_required()
        def delete_book():
            delete_book = Book.query.filter_by(isbn=isbn).first()

            db.session.delete(delete_book)
            db.session.commit()

            return jsonify({'message': 'Book deleted!'}), 200
        
        return delete_book()
    