# 1: open file, read each line into separate list, close file
page_pairs = []
updates = []
with open("input", 'r') as file:
    ## Read first section of file xx|yy into tuple ( xx, yy )
    for line in file:
        if line.strip() == "":
            break
        page_pairs.append((line[0:line.index('|')].strip(), line[line.index('|')+1:].strip()))
    ## Read second section of file into list of strings
    for line in file:
        if line.strip() == "":
            break
        updates.append(line)


# part 1
# Find correct updates -- where the update is in order. Order defined as
# if a page appears as a the first half of a page pair tuple, then the second
# half of that tuple must appear later in the update string or not at all
correct_updates = []
for update in updates:
    is_correct = True
    for pair in page_pairs:
        first_index = update.find(pair[0])
        if first_index != -1:
            second_index = update[0:first_index].find(pair[1])
            if second_index != -1:
                is_correct = False
                break
    if is_correct:
        correct_updates.append(update.strip())
    middles = []
    for update in correct_updates:
        length = len(update)
        middles.append(update[length//2-1:length//2+1])
print(sum(list(map(int, middles)))) 