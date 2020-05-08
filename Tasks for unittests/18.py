def square_patch(n):
    if n == 0:
        return []
    square = [0] * n
    for i in range(n):
        square[i] = [0] * n
        for j in range(n):
            square[i][j] = n
    return square

print(square_patch(4))
