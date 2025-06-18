
import numpy as np

# Create a sample array to work with
arr = np.arange(0, 11)
print(f"Original array: {arr}")

print("\n--- 1. Basic Indexing ---")
print(f"Element at index 5: {arr[5]}")
print(f"Element at index 8: {arr[8]}")

print("\n--- 2. Slicing ---")
# Get elements from index 1 up to (but not including) index 5
print(f"Slice from index 1 to 5: {arr[1:5]}")
# Get elements from the start up to index 4
print(f"Slice from start to 4: {arr[:4]}")
# Get elements from index 5 to the end
print(f"Slice from index 5 to end: {arr[5:]}")

# Slicing an array returns a view, not a copy. Changes will affect the original array.
print("\n--- 3. Broadcasting ---")
slice_of_arr = arr[0:6]
print(f"Original slice: {slice_of_arr}")
slice_of_arr[:] = 99 # Set all values in the slice to 99
print(f"Modified slice: {slice_of_arr}")
print(f"Original array after modification: {arr}")

# To make a copy, use .copy()
arr_copy = arr.copy()
arr_copy[:] = 100
print(f"\nOriginal array is unaffected by copy's changes: {arr}")
print(f"The modified copy: {arr_copy}")


print("\n--- 4. Indexing in 2D Arrays ---")
arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(f"2D Array:\n{arr_2d}")

# Get a single element (row, column)
print(f"Element at row 1, col 2: {arr_2d[1, 2]}") # Returns 30
print(f"Element at row 0, col 0: {arr_2d[0][0]}") # Alternative syntax

# Slicing 2D arrays
# Get top-right corner (first 2 rows, columns 1 and 2)
print(f"Slice of top-right corner:\n{arr_2d[:2, 1:]}")


print("\n--- 5. Boolean Indexing ---")
arr_bool = np.arange(1, 11)
print(f"Boolean array source: {arr_bool}")
# Create a boolean condition
bool_condition = arr_bool > 5
print(f"Boolean condition (arr > 5): {bool_condition}")

# Use the condition to select elements
print(f"Elements greater than 5: {arr_bool[bool_condition]}")
print(f"Elements that are even: {arr_bool[arr_bool % 2 == 0]}")