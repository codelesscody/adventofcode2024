# visiting locations
# after each location is checked, mark on list with a star
# historian must be in one of the first fifty places, so we must get fifty stars on our list before dec25

# historically significant locations are listed by location ID
# split into two lists, but there is a discrepancy between the twoo
# two lists of numbers here's how to check discrepancies:

# pair up smallest numbers on each list all the way up to largest with largest on each list
# find diistance between each pair, then add up all the distances
# find total distance between the lists

# 0: initiialize variables
distance = 0

# 1: open file, read each list into separate arrays, close file

# 2: sort each array

# 3: pop a pair from each list, compare difference (abs(val1-val2)), and add to distance

# 4. output result