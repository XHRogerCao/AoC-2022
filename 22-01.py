import re
from bisect import bisect_left
raw_rows = []
max_row_size = 0
while True:
    inputval = input()
    if inputval == "": break
    raw_rows.append(inputval)
    max_row_size = max(max_row_size, len(inputval))
row_bounds = []
col_bounds = []
row_obs = []
col_obs = []
row, col = None, None
for i in range(max_row_size):
    col_bounds.append([])
    col_obs.append([])
for i in range(len(raw_rows)):
    row_obs.append([])
    for j in range(len(raw_rows[i])):
        if raw_rows[i][j] == "." and row is None:
            row, col = i, j
        if raw_rows[i][j] != " " and len(row_bounds) == i:
            row_bounds.append([j, len(raw_rows[i]) - 1])
        if raw_rows[i][j] != " " and len(col_bounds[j]) == 0:
            col_bounds[j].append(i)
        if raw_rows[i][j] == " " and len(col_bounds[j]) == 1:
            col_bounds[j].append(i - 1)
        if raw_rows[i][j] == "#":
            row_obs[i].append(j)
            col_obs[j].append(i)
    for j in range(len(raw_rows[i]), max_row_size):
        if len(col_bounds[j]) == 1:
            col_bounds[j].append(i - 1)
for j in range(max_row_size):
    if len(col_bounds[j]) == 1:
        col_bounds[j].append(len(raw_rows) - 1)
direction = 0
raw_moves = input()
moves = list(map(lambda x: int(x), re.findall(r"\d+", raw_moves)))
rotations = re.findall(r"L|R", raw_moves)
for i in range(len(moves)):
    if direction == 0:
        # Right
        left_bound, right_bound = row_bounds[row]
        if len(row_obs[row]) > 0:
            newCol = bisect_left(row_obs[row], col)
            if len(row_obs[row]) == newCol:
                newCol = 0
            move_pos = row_obs[row][newCol] - 1
            rel_move_pos = move_pos
            if move_pos < col:
                rel_move_pos += right_bound - left_bound + 1
            actual_moves = min(moves[i], rel_move_pos - col)
            col += actual_moves
            if col > right_bound:
                col -= right_bound - left_bound + 1
        else:
            col += moves[i]
            while col > right_bound:
                col -= right_bound - left_bound + 1
    elif direction == 1:
        # down
        top_bound, bottom_bound = col_bounds[col]
        if len(col_obs[col]) > 0:
            newRow = bisect_left(col_obs[col], row)
            if len(col_obs[col]) == newRow:
                newRow = 0
            move_pos = col_obs[col][newRow] - 1
            rel_move_pos = move_pos
            if move_pos < row:
                rel_move_pos += bottom_bound - top_bound + 1
            actual_moves = min(moves[i], rel_move_pos - row)
            row += actual_moves
            if row > bottom_bound:
                row -= bottom_bound - top_bound + 1
        else:
            row += moves[i]
            while row > bottom_bound:
                row -= bottom_bound - top_bound + 1
    elif direction == 2:
        # left
        left_bound, right_bound = row_bounds[row]
        if len(row_obs[row]) > 0:
            newCol = bisect_left(row_obs[row], col)
            if newCol == 0:
                newCol = len(row_obs[row])
            move_pos = row_obs[row][newCol - 1] + 1
            rel_move_pos = move_pos
            if move_pos > col:
                rel_move_pos -= right_bound - left_bound + 1
            actual_moves = min(moves[i], col - rel_move_pos)
            col -= actual_moves
            if col < left_bound:
                col += right_bound - left_bound + 1
        else:
            col -= moves[i]
            while col < left_bound:
                col += right_bound - left_bound + 1
    elif direction == 3:
        # up
        top_bound, bottom_bound = col_bounds[col]
        if len(col_obs[col]) > 0:
            newRow = bisect_left(col_obs[col], row)
            if newRow == 0:
                newRow = len(col_obs[col])
            move_pos = col_obs[col][newRow - 1] + 1
            rel_move_pos = move_pos
            if move_pos > row:
                rel_move_pos -= bottom_bound - top_bound + 1
            actual_moves = min(moves[i], row - rel_move_pos)
            row -= actual_moves
            if row < top_bound:
                row += bottom_bound - top_bound + 1
        else:
            row += moves[i]
            while row < top_bound:
                row += bottom_bound - top_bound + 1

    if i < len(rotations):
        if rotations[i] == "R":
            direction = (direction + 1) % 4
        else:
            direction = (direction + 3) % 4
    # print(row, col, direction)

print((row + 1) * 1000 + (col + 1) * 4 + direction)
