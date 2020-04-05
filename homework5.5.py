P=50
H=20
counter = 0
suma = 0
dob = 1
while counter <= 100:
    a = int (input ("Input any number: "))
    if a<P:
        suma += a
    if a>H:
        dob *= a
    if a>H and a<P:
        counter +=1
    if a==P or a==H:
        break
print ("%d suma of numbers" %(suma))
print ("%d dob of numbers" %(dob))
print ("%d amount of numbers beetwen %d and %d" %((counter),H,P))
