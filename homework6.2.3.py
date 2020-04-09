from random import *
# n - rows
# m - columns
n = 5
m = 4
# create matr
matr = [0] * (n+1)
for i in range(n+1):
    matr[i] = [0] * (m+1)

for i in range (n):
    for j in range (m):
        matr[i][j] = int(input("Enter value in matrix: "))
        matr[i][m] = matr[i][m] + matr[i][j]
        matr[n][j] = matr[n][j] + matr[i][j]
for i in range(n+1):
    for j in range (m+1):
        print("%5d" %matr[i][j],end="")
    print()
print("The last raw and the last column is the sum of elements in according raw and according column")
