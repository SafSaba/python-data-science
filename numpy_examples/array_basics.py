import numpy as np


# From a Python list
list_a = [1, 2, 3, 4]
np_array_a = np.array(list_a)
print(f"Array from list: {np_array_a}")
print(f"Type of array: {type(np_array_a)}")

# Create a 2D array (matrix)
list_b = [[1, 2, 3], [4, 5, 6]]
np_array_b = np.array(list_b)
print(f"2D Array (Matrix):\n{np_array_b}")


print("\n--- 2. Array Attributes ---")
print(f"Shape of 1D array: {np_array_a.shape}")   # (4,) -> 4 elements
print(f"Shape of 2D array: {np_array_b.shape}")   # (2, 3) -> 2 rows, 3 columns
print(f"Data type of array: {np_array_a.dtype}")  # int64
print(f"Number of dimensions: {np_array_b.ndim}") # 2



print("\n--- 3. Special Array Creation ---")

# An array of all zeros
zeros_array = np.zeros((2, 4)) # 2 rows, 4 columns
print(f"Zeros array:\n{zeros_array}")

# An array of all ones
ones_array = np.ones((3, 3))
print(f"Ones array:\n{ones_array}")

# An array with a range of elements
range_array = np.arange(0, 10, 2) # Start, stop (exclusive), step
print(f"Range array: {range_array}")

# An array with a specific number of points between two values
linspace_array = np.linspace(0, 1, 5) # Start, stop (inclusive), number of points
print(f"Linspace array: {linspace_array}")

# Identity matrix
identity_matrix = np.eye(3)
print(f"Identity matrix:\n{identity_matrix}")

# Random arrays
random_array = np.random.rand(2, 2) # Uniform distribution [0, 1)
print(f"Random array (uniform):\n{random_array}")

random_int_array = np.random.randint(0, 100, (3, 3)) # Random integers
print(f"Random integer array:\n{random_int_array}")