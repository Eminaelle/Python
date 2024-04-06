import numpy as np

arr = np.array([1, 2, 4, 4, 5])
print(arr[1])  # Accès à un élément
print(arr[2:5])  # Slicing
arr = np.arange(6)
print(arr)
arr_reshaped = arr.reshape((2, 3))
print(arr_reshaped)
arr = np.array([1, 2, 3])
arr_plus_one = arr + 1
print(arr_plus_one)
arr = np.array([1, 2, 3])
sin_arr = np.sin(arr)
print(sin_arr)
arr = np.array([1, 2, 3, 4])
print(np.sum(arr))
print(np.mean(arr))
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Produit matriciel
prod = np.dot(a, b)

# Déterminant
det = np.linalg.det(a)

# Inverse
inv = np.linalg.inv(a)
print(prod, det, inv, sep='\n')

arr = np.array([1, 2, 3, 4])
condition = arr > 2
filtered_arr = arr[condition]
print(filtered_arr)