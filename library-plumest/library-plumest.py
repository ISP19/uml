class Book:
    """ The Book object

    Args:
        name (str): name of this book.
        quantity (int): quantity of this book
    """

    def __init__(self, name: str, quantity: int = 1):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return self.name


class Category:
    """ The Category object contains a lot of Books

    Args:
        books (list): list of Book object
    """
    CATEGORY_CODE = 0

    def __init__(self, books: list):
        Category.CATEGORY_CODE += 1

        self.books = books
        self.category_code = Category.CATEGORY_CODE

    def total_books(self) -> int:
        """ Return number of all books in this category."""
        # code omitted

    def add_new_book(self, book: Book):
        """ Add new Book to this Category"""
        # code omitted


class Library:
    """ The Library object contains a lot of Category

    Args:
        categories (list): list of Category object
    """

    def __init__(self, categories: list):
        self.categories = categories

    def search_book(self, book_name: str) -> Category or None:
        """ Return categories that have 'book_name' book"""
        # code omitted

    def add_new_category(self, category: Category):
        """ Add new Category to Library"""
	# code omitted
