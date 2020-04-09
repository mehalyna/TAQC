from random import *
# n - rows
# m - columns
n = int(input("Enter n to create n×m matrix. n: "))
m = int(input("Enter m to create n×m matrix. m: "))
# create matr
matr = [0] * (n+1)
for i in range(n+1):
    matr[i] = [0] * (m+1)

for i in range (n):
    for j in range (m):
        matr[i][j] = randint(1,25)
        matr[i][m] = matr[i][m] + matr[i][j]
        matr[n][j] = matr[n][j] + matr[i][j]
#        print("%5d" %matr[i][j],end="")
for i in range(n+1):
    for j in range (m+1):
        print("%5d" %matr[i][j],end="")
    print()
print ("*******************************************")
#i+1=sum(i)
# sum of elements in rows and columns
#for i in range(n):
 #   matr[i+1][j]=matr[(sum(i))][j]
 #   print()





    
##for i in range (n):
##    print (" | ", end="")
##    for j in range (m):
##        print (" - ", end="")
##    print ()


