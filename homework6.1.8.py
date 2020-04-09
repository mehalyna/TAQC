from random import *
a = []
# create list a
for i in range(10):
    a.append(int(randint(0,100)))
print ('a =', a)

print ('The max number is: %d'  %(max(a)))
print ('The min number is: %d'  %(min(a)))
#swap min and max
if a1!=a2:
    a[a.index(max(a))],a[a.index(min(a))]=a[a.index(min(a))],a[a.index(max(a))]
    print ("Swaped min and max number: ", a)


