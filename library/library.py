class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id

class Library:
    def __init__(self, location, librarian_id):
        self.location = location
        self.librarian_id = librarian_id
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, book):
        pass

class Librarian:
    def __init__(self, name, librarian_id):
        self.name = name
        self.librarian_id = librarian_id
