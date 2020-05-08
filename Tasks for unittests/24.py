def count_uppercase(l1):
    count = 0
    for word in l1:
        for let in word:
            if let.isupper():
                count += 1
    return count

print(count_uppercase(['cAT', 'SUn', 'suMmER']))

