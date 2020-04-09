# перший список
a = [1, 'cat', 'apple', 'cat', 3, 1, 'white', 'relax', 'cat', 'apple', 5, 'coconut']
print ("Hello! List 'a'= ", a)
# список унікальних елементів
b = []
c = []
for i in a:
    if a.count(i) == 1:
        b.append(i)
print ("List with not duplicated elements is: ", b)



