def is_pandigit(n):
#    print(set(str(n)))
    return len(set(str(n))) == 10

print(is_pandigit(1234567890))
