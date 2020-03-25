s = int (input ('enter square: '))
from math import sqrt
a = sqrt(s)
r = int (input ('enter radius of circle: '))
d = 2*r
k = int (input ('enter length between wall and circle: '))
if (k + d) <= a :
       print ('it is possible')
else :
    print ('it is impossible')
