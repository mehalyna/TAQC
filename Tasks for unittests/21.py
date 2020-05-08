from math import*

def is_sastry(n):
    num = int(str(n) + str(n+1))
    print(num)
    if sqrt(num) == int(sqrt(num)):
        return True
    else:
        return False

print(is_sastry(106755))
