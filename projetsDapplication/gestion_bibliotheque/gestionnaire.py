import sys
import csv
from book import Book
from library import Library
from user import User

def main():
    check_arg(sys.argv)
    books = data_extraction(sys.argv[1])
    library = Library()
    library.add_books(books)
    #print(library)
    user1 = User.get()

    user1.borrow_book(library, book_title="The hobbit")
    user1.borrow_book(library, book_title="War and Peace")
    print(user1)
    user1.return_book(library, book_title="the hobbit")
    print(user1)
    #print(library)



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
        raise PermissionError(f"Error: Permission denied to read the file '{file_path}'.")
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