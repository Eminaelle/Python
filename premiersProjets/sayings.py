import cowsay

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(cowsay.get_output_string("stegosaurus",f"hello, {name}"))

def goodbye(name):
    print(f"goodbye, {name}")


if __name__ == "__main__":
    main()