a = []
mult = 1
for i in range(5):
    a.append(int(input ("Input number into list: ")))
    mult = mult * a[i]
print ("The list is: " , a)
b = sum(a)
print ("The sum of numbers in list: %d" %(b))
print ("The dob of numbers in list: %d" %(mult))
