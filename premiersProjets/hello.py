def main():
    # Ask user their name & Remove whitespace from str & Capitalize user's name
    userName = input("What's your name? ").strip().title()
    hello(userName)


    #Split user's name
    #first, last = userName.split(" ")

    # Say hello to user
    #print(f"hello, {userName}")


def hello(aName="world"):
    print("Hello", aName)

main()