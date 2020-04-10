#Задано n рядочків символів.  Розробити програму, яка визначає і
#друкує окремо приголосні та голосні малі літери латинського
#алфавіту, які є в кожному рядку.

from random import *
n = int(input("Enter count of rows: "))
a = []
for i in range (n):
    a.append(input("Enter text: "))

wolves = {'a', 'e', 'i', 'o', 'u', 'y'}
conson = []
for i in range (98,123):
    if chr(i) not in wolves:
        conson.append(chr(i))

for i in range (n):
    count = 0
    #row = a[i]
    for char in a[i]:
        if char in conson:
            count += 1
    print("Row %d contains %d consonant letters" %(i+1,count))
    
