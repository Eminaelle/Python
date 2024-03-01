import sys
import csv
from book import Book, NullBook
from library import Library
from user import User


def main():
    check_arg(sys.argv)
    books = data_extraction(sys.argv[1])
    library = Library()
    library.add_books(books)
    user_actif = User.get()
    library.add_user(user_actif)

    while True:
        # Display the menu of options
        print(f"\n{user_actif.name}, Welcome to the Library")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Display available books")
        print("6. Change user")
        print("7. See the books borrowed")
        print("8. Exit")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            # Add a book
            title = input("Book title: ")
            author = input("Book author: ")
            library.add_book(Book(title, author, "Available"))
            print("Book added successfully.")

        elif choice == "2":
            # Remove a book
            title = input("Title of the book to remove: ")
            book = library.find_book_by_title(title)
            library.delete_book(book)
            print("Book removed successfully.")

        elif choice == "3":
            # Borrow a book
            title = input("Title of the book to borrow: ")
            try:
                library.manage_book_circulation("borrow", user_actif, book_title=title)
            except ValueError:
                print("The book does not exist or is missing. Please try again.")

        elif choice == "4":
            # Return a book
            title = input("Title of the book to return: ")
            try:
                library.manage_book_circulation("return", user_actif, book_title=title)
            except ValueError:
                print("The book does not exist or is missing. Please try again.")

        elif choice == "5":
            # Display available books
            print(f"\n{library}")

        elif choice == "6":
            new_user = User.get()
            if new_user is None:
                print("The name has not been correctly added")
            elif new_user in library.users:
                index = library.users.index(new_user)
                user_actif = library.users[index]
                print(f"{user_actif.name}, Welcome back to the Library.")
            else:
                library.add_user(new_user)
                user_actif = new_user
                print("New account created. You can now borrow books")
        elif choice == "7":
            print(user_actif)

        elif choice == "8":
            # Exit
            print("Thank you for using the library. See you soon!")
            break

        else:
            print("Invalid choice, please try again.")


def data_extraction(file_path):
    """
    Extracts data from a CSV file at the given file path.

    @param file_path: The path to the CSV file to be read.
    @return: A list of dictionaries, each representing a row from the CSV file.
    @raise FileExistsError: If the file does not exist at the given path.
    @raise PermissionError: If there is no permission to read the file.
    @raise Exception: If an unexpected error occurs during file reading.
    """
    try:
        with open(file_path) as file:
            data = [row for row in csv.DictReader(file)]
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The file '{file_path}' was not found")
    except PermissionError:
        raise PermissionError(
            f"Error: Permission denied to read the file '{file_path}'."
        )
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")
    else:
        return data


def check_arg(argv):
    """
    Checks if the correct number of command-line arguments has been passed.

    @param argv: The list of command-line arguments, including the script name.
    @raise ValueError: If the incorrect number of arguments is provided.
    """
    if len(argv) != 2:
        raise ValueError("Put the name of the data file in arguments")


if __name__ == "__main__":
    main()
