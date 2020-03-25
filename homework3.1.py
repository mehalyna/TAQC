x = int (input ('enter year: '))
a = (x//100) + 1
if x%4==0 :
    print (x, 'leap year and', a, 'century')
else :
    print (x, 'not leap year and', a, 'century')
