#Imagine a circle and two squares: a smaller and a bigger one.
#For the smaller one, the circle is a circumcircle and for the bigger one,
#an incircle.
#Create a function, that takes an integer (radius of the circle) and
#returns the square area of the square inside the circle.

def square_area(r):
    return 2 * r ** 2

print(square_area(5))
