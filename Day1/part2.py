# historically significant locations are listed by location ID
# split into two lists, but there is a discrepancy between the two

# look at location IDs in first list
# multiply each ID by how many times it occurs in second list
# add total similarity scores up

# 0: initiialize variables
similarity = 0
list1 = []
list2 = []

# 1: open file, read each list into separate arrays, close file
with open("Day1/input") as file:
    for line in file:
        list1.append(line.split(None)[0])
        list2.append(line.split(None)[1])

# 3: for each item in list1, multiply it by its occurrences in list2, then add to similarity score

for id in list1:
    similarity += int(id) * list2.count(id)

# 4. output result
print(similarity)