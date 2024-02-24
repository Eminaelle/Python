from book import Book, NullBook
from library import Library

class User:
    """
    Represents a user of the library, capable of borrowing and returning books.
    
    @ivar name: The name of the user.
    @ivar borrowed_books: A list of Book objects that the user has currently borrowed.
    """
    def __init__(self, name: str, borrowed_books: list= []) -> None:
        """
        Initializes a new User instance.
        
        @param name: The name of the user.
        @param borrowed_books: An optional list of Book objects the user has borrowed.
        """
        self.name = name
        self.borrowed_books = borrowed_books[:]
    
    def __str__(self) -> str:
        """
        Returns a string representation of the user and their borrowed books.

        @return: A string detailing which books, if any, the user has borrowed.
        """
        if self.borrowed_books:
            borrowed_list = [str(book) for book in self.borrowed_books]
            return f"{self.name} borrowed the book(s) {', '.join(borrowed_list)}."
        return f"{self.name} has yet to borrow a book"
    
    @classmethod
    def get(cls):
        """
        Creates a new User instance based on user input.

        @return: A User instance with the provided name.
        """
        name = input("What's your name? ")
        return cls(name)

    @property
    def name(self):
        """
        The name of the user.
        """
        return self._name
    
    @name.setter
    def name(self, name):
        """
        Sets the name of the user, with validation.
        
        @param name: The name to set for the user.
        @raise ValueError: If the name is missing.
        """
        if not name:
            raise ValueError("Missing name")
        self._name = name

    def borrow_book(self, library: Library, book : Book= None, book_title: str= "") -> None:
        """
        Allows the user to borrow a book from the library.

        @param library: The Library instance from which to borrow a book.
        @param book: An optional specific Book object to borrow.
        @param book_title: An optional title of a book to borrow.
        @raise ValueError: If the library is missing or neither a book nor a book title is provided.
        """
        if not library:
            raise ValueError("Missing library")
        
        if book is not None:
            if isinstance(book, NullBook):
                print("The book provided is not valid.")
                return
            else:
                if library.book_exit(book):
                    self.borrowed_books.append(book)
        elif book_title:
            book = library.find_book_by_title(book_title)
            if isinstance(book, NullBook):
                print("Book not found")
                return
            else:
                if library.book_exit(book):
                    self.borrowed_books.append(book)
        else:
            raise ValueError("Either a book or a book title must be provided.")

    def return_book(self, library: Library, book : Book= None, book_title: str= "") -> None:
        """
        Allows the user to return a book to the library.

        @param library: The Library instance to return a book to.
        @param book: An optional specific Book object to return.
        @param book_title: An optional title of a book to return.
        @raise ValueError: If the library is missing or neither a book nor a book title is provided.
        """
        if not library:
            raise ValueError("Missing library")
        
        if book is not None:
            if isinstance(book, NullBook):
                print("The book provided is not valid.")
                return
            else:
                if library.book_enter(book):
                    self.borrowed_books.remove(book)

        elif book_title:
            book = library.find_book_by_title(book_title)

            if isinstance(book, NullBook):
                print("Book not found")
                return
            else:
                if library.book_enter(book):
                    self.borrowed_books.remove(book)

        else:
            raise ValueError("Either a book or a book title must be provided.")