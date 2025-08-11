class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call Book's __init__
        self.file_size = file_size       # Unique to EBook


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call Book's __init__
        self.page_count = page_count     # Unique to PrintBook


class Library:
    def __init__(self):
        self.books = []  # Composition: list to store all book objects

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")
