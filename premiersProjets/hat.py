import random

class Hat:
    
    houses = ["Gryffindor", "Hufflepuff", "Ravenclow", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.house))

    

def main():
    Hat.sort("Harry")



if __name__ == "__main__":
    main()