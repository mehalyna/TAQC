def replace(lists):
    new_list = []
    for i in lists:
        if type(i)== int:
            new_list.append(0)
        elif type(i) == float:
            new_list.append(0.0)
        elif type(i) == str:
            new_list.append('')
        elif type(i) == bool:
            new_list.append(False)
        elif type(i) == list:
            new_list.append([])
        elif type(i) == tuple:
            new_list.append(())
        elif type(i) == set:
            new_list.append(set())
        elif type(i) == dict:
            new_list.append(set())
        else:
            new_list.append(None)
    return new_list

print(replace([[1,2], 3.42, 'cat', {1,2}, True, {}]))
    
