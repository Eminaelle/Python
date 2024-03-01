class Book:
    """
    Represents a book with a title, author, and status.

    @ivar title: The title of the book.
    @ivar author: The author of the book.
    @ivar status: The current status of the book (default is 'Available').
    """

    def __init__(self, title: str, author: str, status="Available") -> None:
        """
        Initializes a new Book instance.

        @param title: The title of the book.
        @param author: The author of the book.
        @param status: The initial status of the book. Defaults to 'Available'.
        """
        self.title = title
        self.author = author
        self.status = status

    def __str__(self) -> str:
        """
        Returns a string representation of the book.

        @return: String describing the book title and author.
        """
        return f"{self.title} written by {self.author}"

    @classmethod
    def get(cls):
        """
        Class method to create a new Book instance from user input.

        @return: A new instance of Book with user-provided title, author, and status.
        """
        title = input("Title: ").strip().capitalize()
        author = input("Author: ").strip().capitalize()
        status = input("Statut: ").strip().lower()
        return cls(title, author, status)

    @property
    def title(self):
        """The title property."""
        return self._title

    @title.setter
    def title(self, title: str):
        """
        Sets the title of the book. Strips and capitalizes the input.

        @param title: The title of the book.
        @raise ValueError: If the title is missing.
        """
        if not title:
            raise ValueError("Missing title")
        self._title = title.strip().capitalize()

    @property
    def author(self):
        """The author property."""
        return self._author

    @author.setter
    def author(self, author: str):
        """
        Sets the author of the book. Strips and capitalizes the input.

        @param author: The author of the book.
        @raise ValueError: If the author is missing.
        """
        if not author:
            raise ValueError("Missing author")
        self._author = author.strip().capitalize()

    @property
    def status(self):
        """The status property."""
        return self._status

    @status.setter
    def status(self, status: str):
        """
        Sets the status of the book. Validates against 'Available' and 'Borrowed'.

        @param status: The status of the book.
        @raise ValueError: If the status is missing or not valid.
        """
        if not status:
            raise ValueError("Missing status")
        if status.strip().capitalize() not in ["Available", "Borrowed"]:
            raise ValueError(
                "The status is  not valid, have to be 'Available' or 'Borrowed'"
            )
        self._status = status.strip().capitalize()

    def is_available(self) -> bool:
        """
        Checks if the book is available.

        @return: True if the book is available, False otherwise.
        """
        return self.status == "Available"

    def change_status(self):
        """
        Change the status of a book.
        """
        if self.status == "Available":
            self.status = "Borrowed"
        else:
            self.status = "Available"

    def __eq__(self, other) -> bool:
        """
        Checks if this book is equal to another book based on their titles and authors.

        Equality is determined by having both the same title and author, ignoring case sensitivity.
        If the other object is not a Book instance, the comparison will not be performed and
        NotImplemented is returned.

        @param other: The object to compare with this Book instance.
        @return: True if both books have the same title and author (case-insensitive), False otherwise.
                 Returns NotImplemented if 'other' is not a Book instance.
        """
        if not isinstance(other, Book):
            # Return NotImplemented when the comparison is with an unsupported object type.
            return NotImplemented

        title = (self.title or "").lower() == (other.title or "").lower()
        author = (self.author or "").lower() == (other.author or "").lower()

        return title and author


class NullBook(Book):
    """
    Represents a null object pattern for a Book. Used when a search fails to find a book.
    """

    def __init__(self):
        """
        Initializes a NullBook instance with default values.
        """
        super().__init__("No Book Found", "N/A", "Unaivalable")

    def is_available(self) -> bool:
        """
        Always returns False for availability.

        @return: False, indicating the book is not available.
        """
        return False

    def __str__(self) -> str:
        """
        Returns a string indicating the book does not exist.

        @return: A string message about the non-existence of the book.
        """
        return "This book does not exist."
