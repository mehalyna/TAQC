from random import *
a = []
positive = 0
negative = 0
equivalent = 0
for i in range(20):
    a.append(int(randint(-5,4)))
print (a)

for i in a:
    if i>0:
        positive += 1
    elif i<0:
        negative +=1
    elif i==0:
        equivalent +=1
        
print ("Count of positive numbers is: %d" %(positive))
print ("Count of negative numbers is: %d" %(negative))
print ("Count of equivalent to '0' numbers is: %d" %(equivalent))
