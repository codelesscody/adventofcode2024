def find_xmases(lines, x, y):
    xmas_count = 0
    if lines[y][x] == 'X':
        if y > 2 and x > 2 and lines[y-1][x-1] == 'M' and lines[y-2][x-2] == 'A' and lines[y-3][x-3] == 'S':
            xmas_count += 1
        if x > 2 and lines[y][x-1] == 'M' and lines[y][x-2] == 'A' and lines[y][x-3] == 'S':
            xmas_count += 1
        if x > 2 and y < len(lines) - 3 and lines[y+1][x-1] == 'M' and lines[y+2][x-2] == 'A' and lines[y+3][x-3] == 'S':
            xmas_count += 1
        if x < len(lines[y]) - 3 and y > 2 and lines[y-1][x+1] == 'M' and lines[y-2][x+2] == 'A' and lines[y-3][x+3] == 'S':
            xmas_count += 1
        if x < len(lines[y]) - 3 and lines[y][x+1] == 'M' and lines[y][x+2] == 'A' and lines[y][x+3] == 'S':
            xmas_count += 1
        if x < len(lines[y]) - 3 and y < len(lines) - 3 and lines[y+1][x+1] == 'M' and lines[y+2][x+2] == 'A' and lines[y+3][x+3] == 'S':
            xmas_count += 1
        if y > 2 and lines[y-1][x] == 'M' and lines[y-2][x] == 'A' and lines[y-3][x] == 'S':
            xmas_count += 1
        if y < len(lines) - 3 and lines[y+1][x] == 'M' and lines[y+2][x] == 'A' and lines[y+3][x] == 'S':
            xmas_count += 1
    return xmas_count

def find_crossmases(lines, x, y):
    if lines[y][x] == 'A':
        if y > 0 and y < len(lines) - 1 and x > 0 and x < len(lines[y]) - 1 and lines[y-1][x-1] == 'M' and lines[y+1][x-1] == 'M' and lines[y-1][x+1] == 'S' and lines[y+1][x+1] == 'S':
            return 1
        if y > 0 and y < len(lines) - 1 and x > 0 and x < len(lines[y]) - 1 and lines[y-1][x-1] == 'M' and lines[y+1][x-1] == 'S' and lines[y-1][x+1] == 'M' and lines[y+1][x+1] == 'S':
            return 1
        if y > 0 and y < len(lines) - 1 and x > 0 and x < len(lines[y]) - 1 and lines[y-1][x-1] == 'S' and lines[y+1][x-1] == 'M' and lines[y-1][x+1] == 'S' and lines[y+1][x+1] == 'M':
            return 1
        if y > 0 and y < len(lines) - 1 and x > 0 and x < len(lines[y]) - 1 and lines[y-1][x-1] == 'S' and lines[y+1][x-1] == 'S' and lines[y-1][x+1] == 'M' and lines[y+1][x+1] == 'M':
            return 1
    return 0


# 1: open file, read each line into separate list, close file
lines = []
total_xmases = 0
total_crossmases = 0
with open("Day4/input") as file:
    for line in file:
        lines.append(line)
for y in range(len(lines)):
    for x in range(len(lines[y])):
        total_xmases += find_xmases(lines, x, y)
        total_crossmases += find_crossmases(lines, x, y)


print("part1: " + str(total_xmases))
print("part2: " + str(total_crossmases))
