from random import *
# n - rows
# m - columns
n = 3
m = 3
# create matr1
matr1 = [0] * n
for i in range (n):
    matr1[i] = [0] * m

for i in range (n):
    for j in range (m):
        matr1[i][j] = int(input("Enter value in matrix 1: "))
# create matr2
matr2 = [0] * n
for i in range (n):
    matr2[i] = [0] * m
for i in range (n):
    for j in range (m):
        matr2[i][j] = int(input("Enter value in matrix 2: "))
print ("Matrix 1 : ")
for i in range(n):
    for j in range(m):
        print("%5d" %matr1[i][j],end="")
    print()
print ("Matrix 2 : ")
for i in range(n):
    for j in range(m):
        print("%5d" %matr2[i][j],end="")
    print()
#create matr3
matr3 = [0] * n
for i in range (n):
    matr3[i] = [0] * m
print ("Matrix 3 : ")
for i in range(n):
    for j in range(m):
        if matr1[i][j] >= matr2[i][j]:
            matr3[i][j] = matr1[i][j]
        else :
            matr3[i][j] = matr2[i][j]
        print("%5d" %matr3[i][j],end="")
    print()
#        matr[i][m] = matr[i][m] + matr[i][j]
#        matr[n][j] = matr[n][j] + matr[i][j]
##for i in range(n+1):
##    for j in range (m+1):
##        
    
