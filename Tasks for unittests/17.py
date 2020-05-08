def progress_days(miles):
    total = 0
    for i in range(len(miles)-1):
        if miles[i] < miles[i+1]:
            total += 1
    return total

print(progress_days([2, 5, 4, 7, 8]))
