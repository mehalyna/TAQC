def count_overlapping(intervals, point):
    overlap = 0
    for i in intervals:
        if point >= i[0] and point <= i[1]:
            overlap += 1
    return overlap

print(count_overlapping([[1, 3], [2, 5], [4, 8]], 3))
