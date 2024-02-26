from book import Book, NullBook

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
        return f'{self.name} has yet to borrow a book'
    
    @classmethod
    def get(cls):
        """
        Creates a new User instance based on user input.

        @return: A User instance with the provided name.
        """
        name = input("What's your name? ").capitalize()
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

    def __eq__(self, other) -> bool:
        return self.name.lower() == other.name.lower()
    