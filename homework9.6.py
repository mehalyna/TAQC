#Написати функцію is_prime, яка приймає 1 аргумент - число від 0 до 1000,
#і повертає True, якщо воно просте, і False - в іншому випадку

a = int(input("Input number between 0..1000: "))

              
def is_prime(a):
    if a < 0 or a > 1000:
        return "Invalid number"
    for x in range (2, a):
        if a % x == 0:
            return False
    return True

print("%d -" %(a), is_prime(a))
