from random import *
print("Hello! Let's play. Enter N to print N random numbers")
n = int(input("N: "))
# перший список
a = []
# список індексів парних елементів
b = []
# create list a
for i in range(n):
    a.append(int(randint(1,50)))
print (a)

# add numbers >=0 to another list
for i in range(len(a)):
    if a[i] % 2 == 0:
        b.append(i)


print ("The list of indexes: ", b)

