#Написати функцію date, яка приймає 3 аргументи - день, місяць і рік.
#Повернути True, якщо така дата є в нашому календарі, і False - в
#іншому випадку.

d = int(input("Input day: "))
m = int(input("Input month: "))
y = int(input("Input year: "))

              
def date(d, m, y):
    if y < 0 or y > 3000:
        return False
    if m <= 0 or m >= 13:
        return False
    if d <= 0 or d >=32:
        return False
    if d == 29:
        if m ==2 and y%4!=0 :
            return False
    if d == 30 and m == 2:
        return False
    if d == 31 and m not in [1, 3, 5, 7, 8, 10, 12]:
        return False
    return True


print("Date %d/%d/%d is: " %(d, m, y), date(d, m, y))
