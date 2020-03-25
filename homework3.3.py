x = int (input ("Enter a number: "))
if x>0 :
    print (x, 'is a positive number')
    x = str(x)
    print(len(x), '- digit number')
elif x == 0 :
    print ("number is '0'")
else :
    print (x, 'is a negative number')
    x = str(-x)
    print(len(x), '- digit number')
