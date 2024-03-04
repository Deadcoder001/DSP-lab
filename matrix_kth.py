import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

k = int(input("Enter the row: "))
column_k = matrix[:, k]

# Print the result
print(column_k)
