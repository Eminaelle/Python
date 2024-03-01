def main():
    yell("Today", "is", "Friday")


def yell(*words):
    # uppercased = map(str.upper, words)
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()
