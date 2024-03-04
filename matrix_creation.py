import numpy as np

n = int(input("Enter the size of the matrix: "))

matrix = np.zeros((n, n), dtype=int)

for i in range(n):
    for j in range(n):
        matrix[i, j] = int(input(f"Enter element at position ({i+1}, {j+1}): "))

print(matrix)
