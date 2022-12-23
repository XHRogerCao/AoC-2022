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
for i in range(2022):
    current_block = blocks[i % len(blocks)]
    col, row = 2, max_block_height + 4
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
print(max_block_height + 1)
