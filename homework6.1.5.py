from random import *
print("Hello! Let's play. Enter N to print N random numbers")
n = int(input("N: "))
a = []
withoutNegative = []
# create list a
for i in range(n):
    a.append(int(randint(-20,20)))
print (a)

# add numbers >=0 to another list
for i in a:
    if i>=0:
        withoutNegative.append(i)


print ("The list without negative numbers: ", withoutNegative)

