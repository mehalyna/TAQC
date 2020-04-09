from random import *

#m = int(input("M - ?  "))
n = int(input("N - ?  "))

matr = [0] * n
for i in range(n):
    matr[i] = [0] * n

for i in range(n):
    for j in range(n):
        matr[i][j] = randint(1,100)
        print("%5d" %matr[i][j],end="")
    print()

print("******")

for i in range(n):
    temp = matr[i][i]
    matr[i][i] = matr[i][n-2-i+1]
    matr[i][n-2-i+1] = temp

for i in range(n):
    for j in range(n):
        print("%5d" %matr[i][j],end="")
    print()
