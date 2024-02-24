class Book:
    def __init__(self, title: str, author: str, statut="Available") -> None:
        self.title = title
        self.author = author
        self.statut = statut
    
    def __str__(self) -> str:
        return f"{self.title} written by {self.author}"
    
    @classmethod
    def get(cls):
        title = input("Title: ").strip().capitalize()
        author = input("Author: ").strip().capitalize()
        statut = input("Statut: ").strip().lower()
        return cls(title, author, statut)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title: str):
        if not title:
            raise ValueError("Missing title")
        self._title = title.strip().capitalize()
    
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author: str):
        if not author:
            raise ValueError("Missing author")
        self._author = author.strip().capitalize()

    @property
    def statut(self):
        return self._statut

    @statut.setter
    def statut(self, statut: str):
        if not statut:
            raise ValueError("Missing statut")
        if statut.strip().capitalize() not in ["Available", "Borrowed"]:
            raise ValueError("The statut is  not valid, have to be 'Available' or 'Borrowed'")
        self._statut = statut.strip().capitalize()

    def is_available(self) -> bool:
        if self.statut == "Available":
            return True
        return False
    
class NullBook(Book):
    def __ini__(self):
        self.title = "No Book Found"
        self.author = "N/A"
        self.statut = "Unaivalable"

    def is_available(self) -> bool:
        return False
    
    def __str__(self) -> str:
        return "This book does not exist."