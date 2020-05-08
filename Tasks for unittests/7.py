#Given two lines, determine whether or not they are parallel.
#Lines are represented by a list [a, b, c], which corresponds to the line ax+by=c.

def lines_are_parallel(line1, line2):
  return line1[0]/line1[1] == line2[0]/line2[1]

print(lines_are_parallel([1,2,3], [1,2,4]))
