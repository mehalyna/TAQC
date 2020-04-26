#Написати функцію season, яка приймає 1 аргумент - номер місяця (від 1 до 12),
#і повертає пору року, якій цей місяць належить (зима, весна, літо або осінь)

a = int(input("Input number of month: "))

def season(a):
    if a in (12, 1, 2):
        return ("winter")
    if a in (3, 4, 5):
        return ("spring")
    if a in (6, 7, 8):
        return ("summer")
    if a in (9, 10, 11):
        return ("autumn")
    if a < 0 or a > 12:
        return ("Unknown month")

print(season(a))
