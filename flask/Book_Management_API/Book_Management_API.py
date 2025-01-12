from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory data structure to store books
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "published_year": 1925},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "published_year": 1960},
    {"id": 3, "title": "1984", "author": "George Orwell", "published_year": 1949},
    {"id": 4, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "published_year": 1951},
    {"id": 5, "title": "Pride and Prejudice", "author": "Jane Austen", "published_year": 1813}
]

# Helper function to find a book by ID
def find_book_by_id(book_id):
    for book in books:
        if book['id'] == book_id:
            return book
    return None

# GET /books: Retrieve a list of all books
@app.route('/', methods=['GET'])
def get_books():
    return jsonify(books)

# GET /books/<id>: Retrieve a specific book by its ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = find_book_by_id(id)
    if book is None:
        abort(404, description="Book not found")
    return jsonify(book)

# POST /books: Add a new book
@app.route('/books', methods=['POST'])
def create_book():
    if not request.json or not 'title' in request.json or not 'author' in request.json or not 'published_year' in request.json:
        abort(400, description="Invalid request: Missing required fields")
    
    new_book = {
        "id": len(books) + 1,
        "title": request.json['title'],
        "author": request.json['author'],
        "published_year": request.json['published_year']
    }
    books.append(new_book)
    return jsonify(new_book), 201

# PUT /books/<id>: Update an existing book by its ID
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = find_book_by_id(id)
    if book is None:
        abort(404, description="Book not found")
    
    if not request.json:
        abort(400, description="Invalid request: No data provided")
    
    book['title'] = request.json.get('title', book['title'])
    book['author'] = request.json.get('author', book['author'])
    book['published_year'] = request.json.get('published_year', book['published_year'])
    
    return jsonify(book)

# DELETE /books/<id>: Delete a book by its ID
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = find_book_by_id(id)
    if book is None:
        abort(404, description="Book not found")
    
    books.remove(book)
    return jsonify({"message": "Book deleted successfully"})

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404

# Error handler for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)