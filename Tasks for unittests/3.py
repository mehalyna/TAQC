#A quadratic equation a x² + b x + c = 0 has either 0, 1, or 2 distinct
#solutions for real values of x. Given a, b and c, you should return
#the number of solutions to the equation.

#print("Quadratic equation : %d x² + %d x + %d = 0" %(a, b, c))


def solutions(a, b, c):
    d = b**2 - 4*a*c
    if a == 0:
        return ("The equation in not quadratic. 1 solution")
    if d > 0:
        return (2)
    elif d == 0:
        return (1)
    else:
        return (0)

print("Number of solutions: ", solutions(2, 5, 2))
