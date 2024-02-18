import sys

def sort_heapsort(list):
    try:
        list_lenght = len(list)
    except TypeError:
        raise ValueError("The list to sort is empty or doesn't exist")

    # Les Noeuds sans les feuilles (nombre d'éléments/2 -1) de la plus grande jusqu'à 0
    for i in range(list_lenght // 2 - 1, -1, -1):
        # Initialisation du tas
        restore_heap_properties(list, list_lenght, i)

    for i in range(list_lenght-1, 0,-1):
        # On échange la valeur max qui est remontée à la racine avec l'élément le plus loin et non trié de la liste
        list[i], list[0] = list[0], list[i]
        # i va diminuer à chaque tour, restore_heap_properties s'arrêtera donc chaque tour à un indice de moins
        restore_heap_properties(list, i, 0)


# Cela défini les propriétés du tas, pour que les parents soient bien supérieurs à leurs enfants
def restore_heap_properties(list, n, i):
    # on initialise le premier noeud
    maxVal = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and list[maxVal] < list[left]:
        maxVal = left

    if right < n and list[maxVal] < list[right]:
        maxVal = right

    if maxVal != i:
        list[i], list[maxVal] = list[maxVal], list[i]
        restore_heap_properties(list, n, maxVal)
