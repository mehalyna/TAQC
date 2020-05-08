a = int(input("Input number: "))

def is_repdigit(a):
    if a == 0:
        return True
    b = str(a)
    for i in range(1, len(b)):
        if b[0] != b[i]:
            return False
    return True

print(is_repdigit(a))
