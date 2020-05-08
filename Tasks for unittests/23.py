def last_dig (a, b, c):
    if ((abs(a) % 10) * (abs(b) % 10)) == (abs(c) % 10):
        return True
    return False

print(last_dig(26, -21, 125))
