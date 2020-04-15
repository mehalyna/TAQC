#Створіть словник, зв'язавши його з змінною school, і наповніть його даними, які б відображали
#кількість учнів в десяти різних класах (наприклад, 1а, 1б, 2б, 6а, 7в тощо.). Дізнайтеся
#скільки людей в певному класі.
#Уявіть, що в школі відбулися зміни, додайте їх в словник:
#- В трьох класах змінилося кількість учнів;
#- В школі з'явилося два нових класу;
#- В школі розформували один з класів. Виведіть вміст словника на екран.


import random 
school = {'1a': 19, '1b': 17, '1c': 21, '2a': 20, '2b': 25, '3a': 23, '3c': 19, '5a': 17, '5d': 20, '5b': 16}
print("School:",school)
# count of students
# new classes
keys = []
for key in school.keys():
    keys.append(key)
#print(keys)

for stud in range(3):
    school[random.choice(keys)] = int(input("Input new count of students, please: "))
for clas in range(2):
    school[int(input("Input new class, please: "))] = int(input("Input count of students in new class, please: "))
# -1 class
x = school.get("5d")
school["5b"] = 16 + int(x / 2)
school["5a"] = 17 + int(x / 2)
print("School after changes:",school)

