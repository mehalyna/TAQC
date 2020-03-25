figure = input ("please, enter a figure: rectangle, triangle or circle: ")
if figure == 'rectangle' :
    a = int (input ("Enter width: "))
    b = int (input ("Enter height: "))
    s = a*b
    print (s, 'square')
elif figure == 'triangle' :
    a = int (input ("Enter length of side a: "))
    b = int (input ("Enter length of side b: "))
    c = int (input ("Enter length of side c: "))
    p = (a + b + c)/2
    s1 = p * (p - a)*(p - b)*(p - c)
    from math import sqrt
    s = sqrt(s1)
    print (s, 'square')
elif figure == 'circle':
    r = int (input ("Enter radius: "))
    from math import pi
    s = pi*(r**2)
    print (s, 'square')
else :
    print ('You need to select a figure: rectangle, triangle or circle')
    
