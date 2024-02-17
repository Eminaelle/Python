#Pour le projet concernant les structures de données, je vous propose de créer un script Python pour l'Analyse de données simple en utilisant un fichier CSV. Ce projet vous permettra de pratiquer avec les listes et les dictionnaires, en mettant l'accent sur la lecture de données, leur traitement, et quelques statistiques de base.
#Objectifs du Projet

#Le but est de lire des données depuis un fichier CSV, de les stocker dans une structure de données appropriée, puis de calculer et afficher des statistiques simples telles que la moyenne, la médiane, et le mode d'une série de nombres.
#Données

#Supposons que vous ayez un fichier CSV nommé data.csv contenant les résultats d'une enquête sur l'âge des participants. 


#Étapes Suggérées

#Lecture du fichier CSV : Commencez par écrire une fonction pour lire les données depuis le fichier CSV et les stocker dans une structure de données, par exemple, une liste de dictionnaires où chaque dictionnaire représente une ligne du fichier (à l'exception de la ligne d'en-tête).

#Calcul des statistiques :
#  Moyenne : Calculez l'âge moyen des participants.
#  Médiane : Trouvez l'âge médian. Vous devrez peut-être trier la liste des âges pour cela.
#  Mode : Déterminez l'âge le plus fréquent parmi les participants.

#Affichage des résultats : Affichez les statistiques calculées de manière lisible pour l'utilisateur.

import csv
import sys

from sort_heapsort import sort_heapsort

def main():
    # Checking if the numer of arguments are ok
    check_arg(sys.argv)
    # Extraction of the data in a list of dictionary
    person_data = read_csv(sys.argv[1])
    # Extraction of the age data to put them in a list 
    ages = data_extraction(person_data)
    # Calculation of the average
    print(f"the ages are :{ages}")
    average = calculate_average(ages)
    print(f"The average of the age is {average}")
    # Calculation of the median
    median = calculate_median(ages)
    print(f"The median of the age is {median}")
    # Calculation of the mode
    mode = calculate_mode(ages)
    if not mode:
        print("There isn't a mode")
    else:
        print(f"The age(s) the more frequent(s) is {mode}")

def calculate_mode(list):
    frequence={}
    # Calculation of the frequence of each element of the list
    for element in list:
        if element in frequence:
            frequence[element] = int(frequence[element]) + 1
        else:
            frequence[element] = 1
        
    # Finding the element with the max frequence
    max_val = 0
    max_element = []
    for element in frequence:
        # If the element has the highest frequence the list is cleared and the element is added
        if frequence[element] > max_val:
            max_val = frequence[element]
            max_element = [element]
        # If the element has the same frequence of another we add it in the list
        elif frequence[element] == max_val:
            max_element.append(element)
    # Verification of the existance of a mode, 
    # if all the elements have the same frequence there is no mode
    if len(frequence) == len(max_element):
        return None
    else:
        return max_element  

def calculate_median(list):
    # Tri de la liste avec la fonction sort_heapsort qui modifie une liste et ne renvoie rien.
    sort_heapsort(list)
    if len(list) % 2 == 0:
        # If the list is even the median is egal of the average of the 2 central value
        return (list[len(list)//2-1] + list[len(list)//2]) / 2
    else:
        # If the list is odd the median is egal of the central value
        return list[len(list) // 2 ]
    
def calculate_average(list):
    # Return the average of a list
    i = 0
    total = 0
    for element in list:
        total += element
        i += 1
    if i!=0:
        return total/i
    else:
        print("The data are empty")
        sys.exit()

def data_extraction(Dict):
    # Take a dictionnary with an "Age" key and return a list with the ages
    data = []
    for person in Dict:
        try:
            data.append(int(person['Age']))
        except ValueError:
            print("The data under 'Age' aren't integer")
            sys.exit()
    return data

def check_arg(argv):
    if len(argv) != 2:
        print("Put the name of the data file in arguments")
        sys.exit()

def read_csv(arg_file):
    # Take a file and return a List of Dictionary
    with open(arg_file, 'r') as file:
        data = []
        for row in csv.DictReader(file):
            data.append(row)
        return data

main()