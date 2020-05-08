def concat(*lists):
    new_list = []
    for i in lists:
        new_list.extend(i)
    return new_list

print(concat([1,2], [3,4], [5, 6, 7]))
