from book import Book, NullBook

class Library:
    def __init__(self) -> None:
        self.books: list[Book] = []

    def __str__(self):
        books_available = [str(book) for book in self.books if book.is_available()]
        return f"The available books are : {',\n'.join(books_available)}"
    

    def add_book(self, book: Book):
        if book:
            self.books.append(book)
        else:
            raise ValueError("Missing book")

    def delete_book(self, book: Book):
        try:
            self.books.remove(book)
        except ValueError:
            raise ValueError(f"{book} does not exist in the library")

    def book_enter(self, book:Book) -> None:
        if not book.is_available() and book in self.books:
            self.delete_book(book)
            book.statut = "Available"
            self.add_book(book)
        elif book.is_available():
            print(f"{book} is available and has not been.")
        else:
            print(f"{book} does not exist in the library.")

        
    def book_exit(self, book: Book) -> None:
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
        if book_list:
            for book in book_list:
                self.add_book(Book(book["Title"], book["Author"], book["Statut"]))
            print(f"The {len(book_list)} books have been added in the library")
        else:
            raise ValueError("The list of book is empty")
        
    def find_book_by_title(self, title: str) -> Book:
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return NullBook()