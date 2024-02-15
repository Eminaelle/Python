import secrets
import string
def main():
    print("Password Generator")
    
    # Ask the user what longueur does he want
    width = get_width()
    
    # Does the password contain numbers ? return boolean
    number = include("numbers")

    # Does the password contain special characters ? return boolean
    special = include("special characters")
   
    # Generate the password + return boolean 
    password,ok = generate(width, number, special)
   
    # Generate the password again if it is not according the user's choice
    while not ok:
       password,ok = generate(width, number, special)

    # Print the password
    print(password)

def get_width():
    while True:
        try:
            width = int(input("How long do you want it ? (min 8 / max 64) "))
            if 8 <= width <= 64:
                return width
            else:
                print("The value is incorrect. Please enter a number between 8 and 64")
        except ValueError:
            print("The value is incorrect. Please retry")

    
    
def include(data):
    while True:
        user_input = input(f"Do you want {data} ? Y/N : " )
        if user_input.upper() == "Y":
            return True
        elif user_input.upper() == "N":
            return False
        else:
            print("Invalid input, please enter Y or N.")
    
def generate(width, with_number, with_special):

    # Initialize the sequence with letters
    sequence = string.ascii_letters
    password = ''

    # Set flags based on user's choice 
    digit = not with_number
    letter = False
    special = not with_special

    # Add digits and/or special characters to the sequence if required
    if with_number:
        sequence += string.digits
    if with_special:
        sequence += "!'#$%&()*+,-./:;<=>?@[]^_`{|}~"

    # Generate the password    
    for i in range(width):
        character = secrets.choice(sequence)
        password += character
        if character in string.ascii_letters:
            letter = True
        elif with_number and character.isdigit():
            digit = True
        elif with_special and character in "!'#$%&()*+,-./:;<=>?@[]^_`{|}~":
            special = True

    # Return the generated password ans if it is according the user's choice
    return password, letter and digit and special

    


main()