import numpy as np

# Create array from list
arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))

# 2D array (matrix)
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix)
print("Shape:", matrix.shape)

zeros = np.zeros((3, 3))
ones = np.ones((2, 4))

print("Zeros:\n", zeros)
print("Ones:\n", ones)

arr = np.arange(0, 10, 2)

print(arr)

rand_arr = np.random.rand(3, 3)

print(rand_arr)

# Identity matrix
identity = np.eye(4)

print(identity)