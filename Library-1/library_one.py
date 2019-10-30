#6110545473 Chananchida
class Book:
    """A Book class"""
    def __init__(self, title: str, author: str, book_id):
        """Book constructor"""
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_lend = False
        self.detail = ''

    def lend_book(self):
        """Update status when lended"""
        self.is_lend = True

    def update_detail(self, detail: str):
        """Update detail"""
        self.detail = detail


class Library:
    """A Library class"""
    def __init__(self, location: str, librarian_name: str, librarian_id):
        """Library constructor"""
        self.location = location
        self.librarian = Librarian(librarian_name, librarian_id)
        self.books = []

    def add_book(self, book: Book):
        """Append new book to list"""
        self.books.append(book)

    def remove_book(self, book: Book):
        """Remove a specify book from list"""
        pass


class Librarian:
    """A Librarian class"""
    def __init__(self, name: str, librarian_id):
        """Librarian constructor"""
        self.name = name
        self.librarian_id = librarian_id

    def issue_book(self, book: Book):
        """Issue book"""
        pass

    def return_book(self, book: Book):
        """Return book after lend"""
        pass
