#Написати функцію square, яка приймає 1 аргумент - сторону квадрата, і
#повертає 3 значення (за допомогою кортежу): периметр квадрата, площу
#квадрата і діагональ квадрата.

from math import *
a = int(input("Length of side: "))

def square(a):
    p = 4 * a
    s = a ** 2
    d = a * sqrt(2)
    return (p, s, d)
    
print("Tuple: ", square(a))
