import re

# 1: open file, read each report into separate arrays, close file
with open("Day3/input") as file:
    input = file.read()

#part1
total = 0
pattern = r"mul\(\d{1,3},\d{1,3}\)"
validFunctions = re.findall(pattern, input)
for function in validFunctions:
    value = [int(s) for s in re.findall(r'\d+', function)]
    total += value[0] * value[1]
print('part1: ' + str(total))

#part2
total = 0
do = True
pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
validFunctions = re.findall(pattern, input)
for function in validFunctions:
    if function == "do()":
        do = True
    elif function == "don't()":
        do = False
    else: 
        if do:
            value = [int(s) for s in re.findall(r'\d+', function)]
            total += value[0] * value[1]
print('part2: ' + str(total))