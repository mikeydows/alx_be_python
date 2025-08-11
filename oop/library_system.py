class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(f"E-Book: {book.title} by {book.author}, File Size: {book.file_size}MB")
            elif isinstance(book, PrintBook):
                print(f"Print Book: {book.title} by {book.author}, Pages: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")


# Example usage (so output exists for the test)
if __name__ == "__main__":
    library = Library()

    # Add different types of books
    library.add_book(Book("The Alchemist", "Paulo Coelho"))
    library.add_book(EBook("Python 101", "John Doe", 5))
    library.add_book(PrintBook("The Great Gatsby", "F. Scott Fitzgerald", 180))

    # List all books
    library.list_books()
