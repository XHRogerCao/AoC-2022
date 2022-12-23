blocks_raw = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##"""

blocks = []
for block in blocks_raw.split("\n\n"):
    lines = block.split("\n")
    new_block = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "#":
                new_block.append((j, len(lines) - i - 1))
    blocks.append(new_block)
movement = input()
movement_length = len(movement)
field = []
columns = 7
for i in range(columns):
    field.append({})
max_block_height = -1
current_move = 0
i = 0
max_point_intervals = []
target_number = 1000000000000
height_offset = 0
while i < target_number:
    current_block = blocks[i % len(blocks)]
    col, row = 2, max_block_height + 4
    old_current_move = current_move
    while True:
        # CAlculate horizontal move
        col_delta = -1 if movement[current_move] == "<" else 1
        valid = True
        for block_col, block_row in current_block:
            new_col = col + col_delta + block_col
            new_row = row + block_row
            if new_col < 0 or new_col >= columns or new_row in field[new_col]:
                valid = False
                break
        if valid:
            col += col_delta
        current_move = (current_move + 1) % movement_length
        # Calculate vertical move using the same logic
        valid = True
        for block_col, block_row in current_block:
            new_col = col + block_col
            new_row = row - 1 + block_row
            if new_row < 0 or new_row in field[new_col]:
                valid = False
                break
        if not valid:
            for block_col, block_row in current_block:
                field[col + block_col][row + block_row] = 1
                max_block_height = max(max_block_height, row + block_row)
            break
        else:
            row = row - 1
    # print(i, current_move, old_current_move)
    if current_move < old_current_move:
        # print(i, current_move)
        max_point_intervals.append((i, max_block_height, current_move))
        good_intervals = []
        for entry in reversed(max_point_intervals):
            if not good_intervals:
                good_intervals.append(entry)
            elif (i - entry[0]) % len(blocks) == 0 and current_move == entry[2]:
                good_intervals.insert(0, entry)
                if len(good_intervals) >= 3:
                    break
        if len(good_intervals) >= 3:
            if good_intervals[-1][0] - good_intervals[-2][0] == good_intervals[-2][0] - good_intervals[-3][0] and good_intervals[-1][1] - good_intervals[-2][1] == good_intervals[-2][1] - good_intervals[-3][1]:
                print("Found pattern")
                print(max_point_intervals)
                print(good_intervals)
                interval_delta = good_intervals[-1][0] - good_intervals[-2][0]
                repetitions = (target_number - i - 1) // interval_delta
                i += interval_delta * repetitions
                height_offset = (good_intervals[-1][1] - good_intervals[-2][1]) * repetitions
    i += 1
print(max_block_height + height_offset + 1)
