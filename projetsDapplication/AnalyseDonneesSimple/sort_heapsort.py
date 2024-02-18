import sys

def sort_heapsort(lst):
    """
    Sorts a list in ascending order using the heap sort algorithm.

    This function first converts the input list into a max heap and then
    repeatedly extracts the maximum element from the heap, placing it at the
    correct position in the list.

    Parameters:
    lst (list): The list to be sorted. Must contain elements of the same type
                that are comparable (e.g., all integers, floats, or strings).

    Raises:
    TypeError: If the elements of the list are not all of the same type.

    Returns:
    None: The function sorts the list in place and does not return a value.
    """
    check_valid_list(lst)
    list_lenght = len(lst)
        
    # Les Noeuds sans les feuilles (nombre d'éléments/2 -1) de la plus grande jusqu'à 0
    for i in range(list_lenght // 2 - 1, -1, -1):
        # Initialisation du tas
        restore_heap_properties(lst, list_lenght, i)

    for i in range(list_lenght-1, 0,-1):
        # On échange la valeur max qui est remontée à la racine avec l'élément le plus loin et non trié de la liste
        lst[i], lst[0] = lst[0], lst[i]
        # i va diminuer à chaque tour, restore_heap_properties s'arrêtera donc chaque tour à un indice de moins
        restore_heap_properties(lst, i, 0)


# Cela défini les propriétés du tas, pour que les parents soient bien supérieurs à leurs enfants
def restore_heap_properties(lst, n, i):
    """
    Restores the heap properties of a sublist assumed to be a heap, starting
    from a node index 'i' to ensure that the subtree rooted at index 'i' is a heap.

    This function is used internally by the heap sort algorithm to maintain
    the heap condition after elements are removed from the heap.

    Parameters:
    lst (list): The list representing the heap.
    n (int): The number of elements in the heap to consider. This parameter
             allows the function to work on a sublist of the original list.
    i (int): The index of the root node of the subtree being heapified.

    Returns:
    None: The function modifies the list in place and does not return a value.
    """
    # on initialise le premier noeud
    maxVal = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and lst[maxVal] < lst[left]:
        maxVal = left

    if right < n and lst[maxVal] < lst[right]:
        maxVal = right

    if maxVal != i:
        lst[i], lst[maxVal] = lst[maxVal], lst[i]
        restore_heap_properties(lst, n, maxVal)

def check_valid_list(lst):
    """
    Checks if the input list is valid for sorting. The list is considered valid
    if it is not empty and all elements are of the same type (either all integers,
    floats, or strings).

    Parameters:
    lst (list): The list to be checked.

    Raises:
    TypeError: If the elements of the list are not all of the same type.

    Returns:
    list: Returns an empty list if the input list is empty or does not exist. Otherwise,
          the function returns None and performs no action.
    """
    if not lst:
        print("The list to sort is empty or doesn't exist")
        return []
    if isinstance(lst[0], (int, float)):
        if not all(isinstance(x, (int, float)) for x in lst):
            raise TypeError("All elements must be the same type")
    if isinstance(lst[0], (str)):
        if not all(isinstance(x, (str)) for x in lst):
            raise TypeError("All elements must be the same type")