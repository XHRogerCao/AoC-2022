from numpy import lcm
rows, cols = 0, 0
inputval = input()
cols = len(inputval) - 2
blizzards = []
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]
while True:
    inputval = input()
    if inputval[1] == "#": break
    for j in range(0, len(inputval) - 2):
        if inputval[j + 1] == ">":
            blizzards.append([(rows, j), 0])
        elif inputval[j + 1] == "v":
            blizzards.append([(rows, j), 1])
        elif inputval[j + 1] == "<":
            blizzards.append([(rows, j), 2])
        elif inputval[j + 1] == "^":
            blizzards.append([(rows, j), 3])
    rows += 1
# Use a modded bfs, kind of
moves = 0
pos = [(-1, 0)]
has_result = False
while not has_result:
    moves += 1
    new_map = [0] * (rows * cols)
    for blizzard in blizzards:
        blizzard[0] = ((blizzard[0][0] + dirs[blizzard[1]][0]) % rows, (blizzard[0][1] + dirs[blizzard[1]][1]) % cols)
        new_map[blizzard[0][0] * cols + blizzard[0][1]] = 1
    new_pos = [(-1, 0)]
    for row, col in pos:
        if row == rows - 1 and col == cols - 1:
            print(moves)
            has_result = True
            break
        for drow, dcol in dirs:
            new_row, new_col = row + drow, col + dcol
            if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols:
                if new_map[new_row * cols + new_col] == 0:
                    new_map[new_row * cols + new_col] = 1
                    new_pos.append((new_row, new_col))
    pos = new_pos
