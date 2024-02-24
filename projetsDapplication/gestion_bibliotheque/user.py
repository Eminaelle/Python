from book import Book, NullBook
from library import Library

class User:
    def __init__(self, name: str, borrowed_books: list= []) -> None:
        self.name = name
        self.borrowed_books = borrowed_books[:]
    
    def __str__(self) -> str:
        if self.borrowed_books:
            borrowed_list = [str(book) for book in self.borrowed_books]
            return f"{self.name} borrowed the book(s) {', '.join(borrowed_list)}."
        return f"{self.name} has yet to borrow a book"
    
    @classmethod
    def get(cls):
        name = input("What's your name? ")
        return cls(name)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    def borrow_book(self, library: Library, book : Book= None, book_title: str= "") -> None:
        if not library:
            raise ValueError("Missing library")
        
        if book is not None:
            if isinstance(book, NullBook):
                print("The book provided is not valid.")
            else:
                library.book_exit(book)
        elif book_title:
            book = library.find_book_by_title(book_title)
            if isinstance(book, NullBook):
                print("Book not found")
            else:
                library.book_exit(book)
                self.borrowed_books.append(book)
        else:
            raise ValueError("Either a book or a book title must be provided.")

    def return_book(self, book: Book, library: Library) -> None:
        if book and library:
            library.book_enter(book)
        elif not book:
            raise ValueError("Missing book")
        else:
            raise ValueError("Missing library")