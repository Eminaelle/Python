from book import Book, NullBook

class Library:
    """
    A class to represent a library containing a collection of books.
    
    @ivar books: A list of Book objects representing the books in the library.
    """
    def __init__(self) -> None:
        """
        Initializes a new Library instance with an empty list of books.
        """
        self.books: list[Book] = []

    def __str__(self):
        """
        Returns a string representation of all available books in the library.

        @return: A formatted string listing all available books.
        """
        books_available = [str(book) for book in self.books if book.is_available()]
        return f"The available books are : {',\n'.join(books_available)}"
    

    def add_book(self, book: Book):
        """
        Adds a book to the library collection.

        @param book: The Book object to add.
        @raise ValueError: If the book is None.
        """
        if book:
            self.books.append(book)
        else:
            raise ValueError("Missing book")

    def delete_book(self, book: Book):
        """
        Removes a book from the library collection.

        @param book: The Book object to remove.
        @raise ValueError: If the book does not exist in the library.
        """
        try:
            self.books.remove(book)
        except ValueError:
            raise ValueError(f"{book} does not exist in the library")

    def book_enter(self, book:Book) -> None:
        """
        Processes the return of a book to the library, making it available again.

        @param book: The Book object that is being returned.
        """
        if not book.is_available() and book in self.books:
            self.delete_book(book)
            book.statut = "Available"
            self.add_book(book)
        elif book.is_available():
            print(f"{book} is available and has not been.")
        else:
            print(f"{book} does not exist in the library.")

        
    def book_exit(self, book: Book) -> None:
        """
        Processes the borrowing of a book from the library, marking it as borrowed.

        @param book: The Book object that is being borrowed.
        """
        if book is None:
            print("The book does not exist.")
        elif isinstance(book, NullBook):
            print("The book provided is not valid.")
        elif book not in self.books:
            print("The book does not exist in the library.")
        else:
            if book.is_available():
                self.delete_book(book)
                book.statut = "Borrowed"
                self.add_book(book)
            else:
                print(f"{book} is not available and so cannot be borrowed")
    
    
    def add_books(self, book_list: list[dict]):
        """
        Adds multiple books to the library collection from a list of book dictionaries.

        @param book_list: A list of dictionaries, each representing a book to add.
        @raise ValueError: If the list of books is empty.
        """
        if book_list:
            for book in book_list:
                self.add_book(Book(book["Title"], book["Author"], book["Statut"]))
            print(f"The {len(book_list)} books have been added in the library")
        else:
            raise ValueError("The list of book is empty")
        
    def find_book_by_title(self, title: str) -> Book:
        """
        Searches for a book by its title.

        @param title: The title of the book to find.
        @return: The Book object if found, otherwise a NullBook instance.
        """
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return NullBook()