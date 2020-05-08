def dice_game(inputs):
    total = 0
    for a,b in inputs:
        if a == b:
            return 0
        else:
            total += a + b
    return total
        

print(dice_game([(3, 2), (1, 1), (1, 3)]))
