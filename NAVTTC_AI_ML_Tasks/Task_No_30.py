import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[1:4])   # Elements from index 1 to 3
print(arr[:3])    # First three elements
print(arr[::2])   # Every 2nd element

import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Slice rows and columns
print(matrix[0:2, 1:3])   # First 2 rows, columns 1-2
print(matrix[:, 0])       # All rows, first column

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[::-1])   # Reverse array
print(arr[-3:-1])  # Elements from -3 to -2