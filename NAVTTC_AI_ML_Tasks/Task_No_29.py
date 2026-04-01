import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Access elements
print(arr[0])   # First element
print(arr[2])   # Third element
print(arr[-1])  # Last element

import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Access elements
print(matrix[0, 1])  # Row 0, Column 1 → 2
print(matrix[2, 2])  # Last element → 9

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

# Slice elements
print(arr[1:4])   # Elements from index 1 to 3
print(arr[:3])    # First three elements
print(arr[::2])   # Step slicing (every 2nd element)