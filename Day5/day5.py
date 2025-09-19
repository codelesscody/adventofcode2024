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
incorrect_updates = []
for update in updates:
    is_correct = True
    for pair in page_pairs:
        first_index = update.find(pair[0])
        if first_index != -1:
            second_index = update[0:first_index].find(pair[1])
            if second_index != -1:
                is_correct = False
    if is_correct:
        correct_updates.append(update.strip())
    else:
        incorrect_updates.append(update.strip())
middles = []
for update in correct_updates:
        length = len(update)
        middles.append(update[length//2-1:length//2+1])
print(sum(list(map(int, middles)))) 


# part 2
# Now look at incorrect_updates. If a set of page pairs both appear in the list
# but in the wrong order, then we need to swap them. We need to keep doing this
# until no more swaps are needed.
def fix_update(update, page_pairs):
    made_a_swap = True
    while made_a_swap:
        made_a_swap = False
        for pair in page_pairs:
            first_index = update.find(pair[0])
            if first_index != -1:
                second_index = update.find(pair[1])
                if second_index != -1 and second_index < first_index:
                    # need to swap
                    made_a_swap = True
                    # swap by replacing the first instance of pair[0] with a temp string
                    # then replacing the first instance of pair[1] with pair[0]
                    # then replacing the temp string with pair[1]
                    temp_str = "TEMPSTRING"
                    update = update.replace(pair[0], temp_str, 1)
                    update = update.replace(pair[1], pair[0], 1)
                    update = update.replace(temp_str, pair[1], 1)
    return update

fixed_middles = []
for update in incorrect_updates:
    fixed_update = fix_update(update, page_pairs)
    length = len(fixed_update)
    fixed_middles.append(fixed_update[length//2-1:length//2+1])
print(sum(list(map(int, fixed_middles))))