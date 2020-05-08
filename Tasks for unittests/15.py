def get_indices(l, item):
    ind = []
    for i in range(len(l)):
        if item == l[i]:
            ind.append(i)
    return ind

print(get_indices([1, 3, 3, 5], 3))
