class Book:
    def __init__(self, name: str, quantity: int = 1):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return self.name


class Category:
    CATEGORY_CODE = 0

    def __init__(self, books: list):  # books is a list of Book
        Category.CATEGORY_CODE += 1

        self.books = books
        self.category_code = Category.CATEGORY_CODE

    def total_books(self) -> int:
        """ Return number of all books in this category."""
        # code omitted
        return 0

    def Add_new_book(self, book: Book):
        """ Add new Book to this Category"""
        # code omitted
        pass


class Library:
    def __init__(self, categories: list):  # categories is a list of Category
        self.categories = categories

    def search_book(self, book_name: str) -> Category:
        """ Return categories that have 'book_name' book"""
        # code omitted
        pass
