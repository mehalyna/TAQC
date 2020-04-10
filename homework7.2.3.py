#Задано символьний рядок. Розробити програму, яка будує і друкує в
#алфавітному порядку множину малих, множину великих латинських  літер,
#які містяться у заданому рядку, і множину цифр, яких немає у рядку

r = "Alwa2Ys laU4gh 3When yOu 9cAn. IT iS2 cHeap2 mE0DicIne"
print(r)
num = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
mal = {'a'}
vel = {'A'}
for i in range (98,123):
    mal.add(chr(i))

for i in range (66,91):
    vel.add(chr(i))
#print(mal, vel)
    
# create new sets of letters which are in r
# create new set of numbers which are not in r
new_mal = set()
new_vel = set()
new_num = set()
for i in (r):
    if i in mal:
        new_mal.add(i)
    elif i in vel:
        new_vel.add(i)
    elif i in r:
        new_num.add(i)
num1 = num.difference(new_num)
print(sorted(new_mal))
print(sorted(new_vel))
print(sorted(num1))
    
