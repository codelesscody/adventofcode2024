# --- Day 6: Guard Gallivant ---

# The input is a map. Each line is a row of the map. Each character is a position in that row.
#A '.' means open ground, a '#' means an obstacle. The guard is marked with an arrow pointing
# in the direction the guard is facing -- '^', 'v', '<', or '>'.

# The guard follows a very strict patrol protocol which involves repeatedly following these steps:

#    If there is something in the square directly in front of you, turn right 90 degrees.
#    Otherwise, take a step forward.

# Start counting positions from the position the guard starts in, including that position.
# How many unique positions does the guard visit at least once on his patrol before leaving
# the map? (The guard leaves the map when he steps off of the edge of the map.)
map_data = []
with open("input", 'r') as file:
    for line in file:
        map_data.append(line.strip())
# find the guard
guard_row = -1
guard_col = -1
guard_dir = ''
for r in range(len(map_data)):
    for c in range(len(map_data[r])):
        if map_data[r][c] in ['^', 'v', '<', '>']:
            guard_row = r
            guard_col = c
            guard_dir = map_data[r][c]
# directions are in order: up, right, down, left
directions = ['^', '>', 'v', '<']
# movement deltas for each direction
deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# set of visited positions
visited = set()
# add starting position
visited.add((guard_row, guard_col))
# patrol until the guard leaves the map
while True:
    # find the index of the current direction
    dir_index = directions.index(guard_dir)
    # calculate the position in front of the guard
    delta = deltas[dir_index]
    new_row = guard_row + delta[0]
    new_col = guard_col + delta[1]
    # check if the position in front of the guard is out of bounds
    if new_row < 0 or new_row >= len(map_data) or new_col < 0 or new_col >= len(map_data[0]):
        break
    # check if the position in front of the guard is an obstacle
    if map_data[new_row][new_col] == '#':
        # turn right 90 degrees
        dir_index = (dir_index + 1) % 4
        guard_dir = directions[dir_index]
    else:
        # move forward
        guard_row = new_row
        guard_col = new_col
        visited.add((guard_row, guard_col))
# print the number of unique positions visited
print(len(visited))
