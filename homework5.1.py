from random import *
x = int(randint(0,100))
#print(x)
counter = 0
print ("Hello! I'm random generator. I generated some number, try to guess it")
a = int (input ("Input your number beetwen 0 and 100: "))
while a!=x and counter<9:
    counter +=1
    if a < x and a > 0:
        print ("Your number is less than generated number")
    elif a > x and a<=100:
        print ("Your number is more than generated number")
    elif a < 0 and a > 100:
        print ("Input your number beetwen 0 and 100: ")
    a = int (input ("Input your number beetwen 0 and 100: "))
else :
    if a==x:
        print ("Congratulations! You guessed it.")
    else :
        print ("You didn't guess.")
        print ("Generated number is %d" %(x))
