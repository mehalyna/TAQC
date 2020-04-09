from random import *

m = int(input("M - ?  "))
n = int(input("N - ?  "))

matr = [0] * m
for i in range(m):
    matr[i] = [0] * n

for i in range(m):
    for j in range(n):
        matr[i][j] = randint(1,100)
        print("%5d" %matr[i][j],end="")
    print()

print("******")

print(matr)
# some preparation
minlist = []

# move through columns
for j in range(n):
    # move inside column through row
    temp = []
    for i in range(m):
        # push elements in the temp list
        temp.append(matr[i][j])
    # find min in temp list
    # append min to minlist
    minlist.append(min(temp))

print(minlist)
# outside loops find max in minlist
print("Max from minlist = %d" %(max(minlist)))



