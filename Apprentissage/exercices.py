import random


def main():
    capital = 1000
    i=1000000
    while i > 0 and capital > 0:
        capital = jeu(choix_jeu(),capital)
        i -= 1
    print(capital)
    
def choix_jeu():
    piece = ["pile", "face"]
    generation = random.choices(piece, k=1)
    if "pile" in generation:
        return "a"
    else:
        return "b"
    
def lance_A():
    piece = ["pile", "face"]
    generation = random.choices(piece, [49, 51], k=1)
    return generation

def lance_B(capital):
    piece = ["pile", "face"]
    if capital % 3 == 0:
        generation = random.choices(piece, [9, 91], k=1)
    else:
        generation = random.choices(piece, [74, 26], k=1)
    return generation

def jeu(type, capital):
    if type == "a":
        if "pile" in lance_A():
            capital += 1
        else:
            capital -= 1
    else:
        if "pile" in lance_B(capital):
            capital += 1
        else:
            capital -= 1
    
    return capital 
main()