def sum_fractions(list1):
    summ = 0
    for i in list1:
        summ += i[0]/i[1]
    return round(summ)

print(sum_fractions([[7,19], [1,4], [13, 8], [0,2], [15, 4]]))
