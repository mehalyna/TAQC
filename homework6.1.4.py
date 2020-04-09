from random import *
print("Hello! Let's play. Enter N to print N random numbers bwwtwen -5 and 5")
n = int(input("N: "))
a = []
positive = []
negative = []

for i in range(n):
    a.append(int(randint(-5,5)))
    print (a[i])

for i in a:
    if i>0 and i!=0:
        positive.append([i])
    elif i<0 and i!=0:
        negative.append([i])
        
print ("The list of positive numbers: ", positive)
print ("The list of negative numbers: ", negative)
