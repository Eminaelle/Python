def main():
    x = float(input("What's x? "))
    y = float(input("What's y? "))

    z = round(x+y)
    print(f"{z:,}")

def square(n):
    return pow(n,2)

main()