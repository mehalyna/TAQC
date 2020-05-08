def oddish_or_evenish(a):
    summ = sum(int(i) for i in str(a))
    if summ % 2 == 0:
        return "Evenish"
    else:
        return "Oddish"

print(oddish_or_evenish(42))
