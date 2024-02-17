def main():
    x = float(input("What's x? "))
    #y = float(input("What's y? "))

    print("x square is", square(x))
    #print(f"{z:,}")

def square(n):
    return n * n

if __name__ == "__main__":
    main()