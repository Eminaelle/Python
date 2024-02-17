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
    people_data = read_csv(sys.argv[1])
    # Extraction of the age data to put them in a list 
    ages_list = data_extraction(people_data)
    # Calculation of the average
    print(f"the ages are :{ages_list}")
    average = calculate_average(ages_list)
    print(f"The average of the age is {average}")
    # Calculation of the median
    median = calculate_median(ages_list)
    print(f"The median of the age is {median}")
    # Calculation of the mode
    mode = calculate_mode(ages_list)
    if not mode:
        print("There isn't a mode")
    else:
        print(f"The age(s) the more frequent(s) is {mode}")


def calculate_mode(age_list):
    """
    Calculate the mode(s) of a list of ages.
    
    Parameters:
    age_list (list): A list of integer ages.
    
    Returns:
    list: A list of the most frequent age(s) found in age_list. Returns None if there is no mode.
    """
    frequency={}
    # Calculation of the frequency of each element of the list
    for element in age_list:
        if element in frequency:
            frequency[element] = int(frequency[element]) + 1
        else:
            frequency[element] = 1
        
    # Finding the element with the max frequency
    max_val = 0
    max_element = []
    for element in frequency:
        # If the element has the highest frequency the list is cleared and the element is added
        if frequency[element] > max_val:
            max_val = frequency[element]
            max_element = [element]
        # If the element has the same frequency of another we add it in the list
        elif frequency[element] == max_val:
            max_element.append(element)
    # Verification of the existance of a mode, 
    # if all the elements have the same frequency there is no mode
    if len(frequency) == len(max_element):
        return None
    else:
        return max_element  


def calculate_median(age_list):
    """
    Calculate the median age from a list of ages.
    
    Parameters:
    age_list (list): A list of integer ages, not necessarily sorted.
    
    Returns:
    float or int: The median age. If age_list has an even number of elements, returns the average of the two central elements.
    """
    # Tri de la liste avec la fonction sort_heapsort qui modifie une liste et ne renvoie rien.
    sort_heapsort(age_list)
    if len(age_list) % 2 == 0:
        # If the list is even the median is egal of the average of the 2 central value
        return (age_list[len(age_list)//2-1] + age_list[len(age_list)//2]) / 2
    else:
        # If the list is odd the median is egal of the central value
        return age_list[len(age_list) // 2 ]

def calculate_average(age_list):
    """
    Calculate the average age from a list of ages.
    
    Parameters:
    age_list (list): A list of integer ages.
    
    Returns:
    float: The average age. If the list is empty, the function exits the program.
    """
    
    if not age_list:  # Check if the list is empty
        raise ValueError("The data are empty")
    try:
        average = sum(age_list) / len(age_list)
        return average
    except TypeError:  # Catch errors if age_list contains non-numeric values
        raise TypeError("Non-numeric value found")


def data_extraction(people_data):
    """
    Extracts age data from a list of dictionaries and returns a list of ages.
    
    Parameters:
    people_data (list of dict): A list of dictionaries, where each dictionary represents a person's data.
    
    Returns:
    list: A list of integer ages extracted from people_data.
    """
    data = []
    for person in people_data:
        try:
            data.append(int(person['Age']))
        except ValueError:
            print("The data under 'Age' aren't integer, please give in arguments a file .csv with Ages")
            sys.exit(1)
        except KeyError:
            print("There isn't Age in the key of the data file")
            sys.exit(1)

    return data

def check_arg(argv):
    if len(argv) != 2:
        print("Put the name of the data file in arguments")
        sys.exit()


def read_csv(file_path):  
    """
    Reads a CSV file and returns a list of dictionaries, each representing a row from the file.
    
    Parameters:
    file_path (str): The file path to the CSV file.
    
    Returns:
    list of dict: A list of dictionaries where each key is a column header from the CSV and each value is the corresponding entry for that column.
    """ 
    try:
        with open(file_path, 'r') as file:
            data = [row for row in csv.DictReader(file)]
            return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to read the file '{file_path}'.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()