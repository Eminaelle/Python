from book import Book, NullBook
from user import User


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
        self.users: list[User] = []

    def __str__(self):
        """
        Returns a string representation of all available books in the library.

        @return: A formatted string listing all available books.
        """
        books_available = [str(book) for book in self.books if book.is_available()]
        return f"The available books are : {',\n'.join(books_available)}"

    def get_user_list(self):
        existent_user = [str(user) for user in self.users]
        return f"The users are : {existent_user}"

    def add_user(self, user: User) -> None:
        """
        Adds a new user to the library's user list, ensuring that each user is unique.

        @param user: The user to be added to the library.
        @type user: L{User}

        @raise ValueError: Raised if the user parameter is None, indicating that no user was provided.
        """
        if user is None:
            raise ValueError("Please enter an user.")
        if user not in self.users:
            self.users.append(user)

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

    def delete_book(self, book: Book):
        """
        Removes a book from the library collection.

        @param book: The Book object to remove.
        @raise ValueError: If the book does not exist in the library.
        """
        if isinstance(book, NullBook) or book is None:
            print("Book not found.")

        if not book.is_available():
            for user in self.users:
                if book in user.borrowed_books:
                    self.manage_book_circulation("return", user, book)
                    print(
                        f"{book} is being deleted of the library. {user.name} doesn't have to return it."
                    )
                    break
        try:
            self.books.remove(book)
        except ValueError:
            raise ValueError(f"{book} does not exist in the library")

    def manage_book_circulation(
        self, operation_type: str, user: User, book: Book = None, book_title: str = ""
    ) -> None:
        """
        Manages the circulation of books within the library, allowing users to borrow or return books.

        This method simplifies the process of borrowing and returning books by encapsulating the logic
        required to check the availability of a book, update its status, and maintain the user's list of
        borrowed books. It supports operations based on either a Book object or a book title.

        @param operation_type: Specifies the operation to be performed. Valid options are "borrow" or "return".
        @type operation_type: C{str}
        @param user: The user who is performing the operation. This user must already be registered with the library.
        @type user: L{User}
        @param book: (Optional) The book object to be borrowed or returned. If not provided, book_title must be used.
        @type book: L{Book}
        @param book_title: (Optional) The title of the book to be borrowed or returned. Used if the book object is not provided.
        @type book_title: C{str}

        @raise ValueError: Raised if:
                            - The operation type is not "borrow" or "return".
                            - Neither a book object nor a book title is provided, or if the provided book is invalid or not found in the library.
                            - The user is not registered in the library.

        This method encapsulates the logic for checking book availability, updating book status, and maintaining the list of books borrowed by a user. It can handle operations based on either a direct book object or a book title. Messages are printed to indicate the success or failure of the operation.

        Notes:
        - If a book is successfully borrowed, it will be added to the user's list of borrowed books.
        - If a book is successfully returned, it will be removed from the user's list of borrowed books.
        - The method prints messages to indicate the success or failure of the operation.
        """
        if not user:
            raise ValueError("Missing user")

        if user not in self.users:
            print(
                "Register the user in the library to be able to borrow or return a book"
            )
            return

        if book_title and not book:
            book = self.find_book_by_title(book_title)

        if book is None or isinstance(book, NullBook) or book not in self.books:
            raise ValueError("The book provided is not valid or hasn't been found.")

        def borrow_book():
            if not book.is_available():
                print(f"{book} is not available and so cannot be borrowed.")
                return False
            book.change_status()
            user.borrowed_books.append(book)
            print(f"Successfully borrowed {book.title}.")
            return True

        def return_book():
            if book.is_available():
                print(f"{book} has not been borrowed yet and can't be returned.")
                return False
            book.change_status()
            user.borrowed_books.remove(book)
            print(f"Successfully returned {book.title}.")
            return True

        if operation_type.lower() == "borrow":
            borrow_book()
        elif operation_type.lower() == "return":
            return_book()
        else:
            raise ValueError(
                "Invalid operation type. Please specify 'borrow' or 'return'."
            )

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
