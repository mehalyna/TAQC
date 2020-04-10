#Задано два символьних рядка із малих і великих латинських літер та цифр.
#Розробити програму, яка будує і друкує в алфавітному порядку множину
#літер, які є в обох масивах, і множини літер окремо першого і другого масивів.

r1 = "Alwa2Ys laU4gh 3When yOu 9cAn."
r2 = "SmIl2e 1ever6y da3Y p8LEa9562e"
print("r1:", r1)
print("r2:", r2)
num = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
mal = {'a'}
vel = {'A'}

for i in range (98,123):
    mal.add(chr(i))

for i in range (66,91):
    vel.add(chr(i))
letters = mal.union(vel)
#print(sorted(letters))

#create new str
r3 = r1 + r2

#create set of letters in r1, r2 and r3(in both of them)
let_r1 = set()
let_r2 = set()
for i in (r3) :
    if i in r1 and i in letters:
        let_r1.add(i)
    if i in r2 and i in letters:
        let_r2.add(i)
let_r3 = let_r1.union(let_r2)
    
print("Letters in r1: ", sorted(let_r1))
print("Letters in r2: ", sorted(let_r2))
print("Letters in r1 and in r2: ", sorted(let_r3))
