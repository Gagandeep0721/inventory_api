from flask import Blueprint, request, jsonify
from books_inventory.helpers import token_required, random_joke_generator
from books_inventory.models import db, Book, book_schema, books_schema


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/getdata')
def getdata():
    return {'some': 'value'}

#Create Book Endpoint
@api.route('/books', methods = ['POST'])
@token_required 
def create_book(our_user):

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    author = request.json['author']
    genre = request.json['genre']
    publisher = request.json['publisher']
    edition = request.json['edition']
    language = request.json['language']
    cost_of_prod = request.json['cost_of_prod']
    series = request.json['series']
    random_joke = random_joke_generator()
    user_token = our_user.token

    print(f"User Token: {our_user.token}")

    book = Book(name, description, price, author, genre, publisher, edition, language, 
                 cost_of_prod, series, random_joke, user_token)
    
    db.session.add(book)
    db.session.commit()

    response = book_schema.dump(book)

    return jsonify(response)

#Read 1 Single Book Endpoint
@api.route('/books/<id>', methods = ['GET'])
@token_required
def get_book(our_user, id):
    if id:
        book = Book.query.get(id)
        response = book_schema.dump(book)
        return jsonify(response)
    else:
        return jsonify({'message': 'ID is missing'}), 401
    

#Read all the books
@api.route('/books', methods = ['GET'])
@token_required
def get_books(our_user):
    token = our_user.token
    books = Book.query.filter_by(user_token = token).all()
    response = books_schema.dump(books)

    return jsonify(response)


#Update 1 Book by ID
@api.route('/books/<id>', methods = ['PUT'])
@token_required
def update_book(our_user,id):
    book = Book.query.get(id)

    book.name = request.json['name']
    book.description = request.json['description']
    book.price = request.json['price']
    book.author = request.json['author']
    book.genre = request.json['genre']
    book.publisher = request.json['publisher']
    book.edition = request.json['edition']
    book.language = request.json['language']
    book.cost_of_prod = request.json['cost_of_prod']
    book.series = request.json['series']
    book.random_joke = random_joke_generator()
    book.user_token = our_user.token

    

    db.session.commit()

    response = book_schema.dump(book)

    return jsonify(response)


#Delete 1 Book by ID
@api.route('/books/<id>', methods = ['DELETE'])
@token_required
def delete_book(our_user, id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()

    response = book_schema.dump(book)

    return jsonify(response)


