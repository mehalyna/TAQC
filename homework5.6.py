counter = 0
positive = 0
negative = 0
x = 0.0
y = 0.0
print ("Hello! Input several numbers to calculate % of positive and negative numbers")
print ("Enter 0 to stop")
while 1==1:
    a = int (input ("Input any number: "))
    if a > 0:
        positive += 1
    if a < 0:
        negative += 1
    counter += 1
    if a==0:
        counter -= 1
        break
x=positive*100/counter
y=negative*100/counter
print ("%f%% positive numbers" %(x))
print ("%f%% negative numbers" %(y))
