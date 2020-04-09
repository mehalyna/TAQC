from random import *
# n - rows
# m - columns
n = int(input("Enter n to create n×m matrix. n: "))
m = int(input("Enter m to create n×m matrix. m: "))
# create matr
matr = [0] * n
for i in range(n):
    matr[i] = [0] * m

a = []

for i in range(n):
    for j in range(m):
        matr[i][j] = randint(0,999)
        print("%5d" %matr[i][j],end="")
        if len(str(matr[i][j])) == 2:
            a.append(matr[i][j])
    print()

print("Count of 2-length numbers is: %d" %(len(a)))
