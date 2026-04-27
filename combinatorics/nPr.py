import math
import random

def nPr(n, r):
    if r > n or n < 0 or r < 0:
        return 0
    return math.factorial(n) / math.factorial(n - r)

def printMatrix(matrix, m, n):
    for i in range(m):
        print("[ ", end="")
        for j in range(n):
            print(matrix[i][j], end=" ")
        print("]")
        print()

m = 7
n = 20
matrix = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]

printMatrix(matrix=matrix, m=m, n=n)

print(nPr(6, 3))



