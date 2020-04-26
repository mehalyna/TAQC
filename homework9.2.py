#Написати функцію is_year_leap, приймає 1 аргумент - рік, і повертає True,
#якщо рік високосний, і False в іншому випадку.

print("Enter Year and program will verify is year leap or not")
a = int(input("Input Year: "))
def is_year_leap(a):
    if a%4==0 :
        return ("True")
    else :
        return ("False")
print(is_year_leap(a))
