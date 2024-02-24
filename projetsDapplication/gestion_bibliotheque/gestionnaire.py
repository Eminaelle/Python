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
    print(user1)
    #print(library)



def data_extraction(file_path):
    try:
        with open(file_path) as file:
            data = [row for row in csv.DictReader(file)]
    except FileExistsError:
        raise FileExistsError(f"Error: The file '{file_path}' was not found")
    except PermissionError:
        raise PermissionError(f"Error: Permission denied to read the file '{file_path}'.")
    except Exception as e:
        Exception(f"An unexpected error occurred: {e}")
    else:
        return data
    
def check_arg(argv):
    if len(argv) != 2:
        raise ValueError("Put the name of the data file in arguments")
    

if __name__ == "__main__":
    main()