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

def main():
    # Checking if the numer of arguments are ok
    check_arg(sys.argv)
    # Extraction of the data in a list of dictionary
    person_data = read_csv(sys.argv[1])
    # Extraction of the age data to put them in a list 
    ages = data_extraction(person_data)
    for number in ages:
        print(number, end=' ')   
    # Calculation of the average
    average = calculate_average(ages)
    print(f"The average of the age is {average}")

#def sorting_list(list):

    
def calculate_average(list):
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

def data_extraction(list):
    data = []
    for person in list:
        try:
            data.append(int(person['Age']))
        except ValueError:
            print("The data under 'Age' aren't integer")
            sys.exit()
    return data

def check_arg(argv):
    if len(argv) != 2:
        print("Put name the name file in arguments")
        sys.exit()

def read_csv(arg_file):
    with open(arg_file, 'r') as file:
        data = []
        for row in csv.DictReader(file):
            data.append(row)
        return data

main()