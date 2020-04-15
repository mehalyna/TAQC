#У змінній записаний текст. Словом вважається послідовність непорожніх
#символів, які йдуть підряд, слова розділені одним або більше пробілом.
#Програмно створіть словник, в якому ключами є слова з речення, а
#значеннями – кількість входження в речення.

x = "good red  color ,  good color cat good red sun  sun , %$$@ %$$@ 6t'3x9"
x = x.split()
#print(x)
abc = {}   
uniq = []  
for a in x:
    if a not in uniq:
        uniq.append(a)
for i in range(len(uniq)):
    abc.update({uniq[i] : x.count(uniq[i])})
print("Dictionary: ", abc)
