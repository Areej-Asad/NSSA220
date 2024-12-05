# 8 - ex1
import numpy as np

# Generate 1D array of 50 random integers between 0-99
array_1d = np.random.randint(0, 100, size=50)

# Generate 2D array of shape (10, 20) with random real numbers between 0-99
array_2d = np.random.uniform(0, 99, size=(10, 20))

# Print arrays
print("1D Array of 50 random integers:")
print(array_1d)

print("\n2D Array of size (10, 20) with random real numbers:")
print(array_2d)

# 8 - ex2
import numpy as np

arr1 = np.array([15, 8, 9, 10, 12, 7])
arr2 = np.array([7, 4, 4, 8, 11, 25])

dot_product = np.dot(arr1, arr2)
print("Dot product of arr1 and arr2:", dot_product)

array_2d = np.array([arr1, arr2])
print("\n2D array:")
print(array_2d)
