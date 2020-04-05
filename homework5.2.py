counter = 1
kratne_5 = 0
while counter <= 10:
    a = int (input ("Input your natural number more than 2: "))
    if a<=2:
        print ("Your number less than 2")
    else:
        counter +=1
        if a%5==0:
            kratne_5 += 1
print ("%d numbers are kratne '5'" %(kratne_5))

