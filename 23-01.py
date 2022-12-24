elves = {}
i = 0
elves_count = 0
while True:
    inputval = input()
    if inputval == "": break
    for j in range(len(inputval)):
        if inputval[j] == "#":
            elves[(i, j)] = (i, j)
            elves_count += 1
    i += 1
check_dirs = [
    [[(-1, 0), (-1, 1), (-1, -1), (1, 0), (1, 1), (1, -1), (0, 1), (0, -1)], (0, 0)],
    [[(-1, 0), (-1, 1), (-1, -1)], (-1, 0)],
    [[(1, 0), (1, 1), (1, -1)], (1, 0)],
    [[(0, -1), (-1, -1), (1, -1)], (0, -1)],
    [[(0, 1), (-1, 1), (1, 1)], (0, 1)],
]
for _ in range(10):
    new_elves = {}
    for elf in elves:
        new_pos = elf
        for check_deltas, move in check_dirs:
            no_elves = True
            for drow, dcol in check_deltas:
                if (elf[0] + drow, elf[1] + dcol) in elves:
                    no_elves = False
                    break
            if no_elves:
                new_pos = (elf[0] + move[0], elf[1] + move[1])
                break
        if new_pos in new_elves:
            # Collision, kick both out
            collided_elf = new_elves[new_pos]
            del new_elves[new_pos]
            new_elves[elf] = elf
            new_elves[collided_elf] = collided_elf
        else:
            new_elves[new_pos] = elf
    elves = new_elves
    check_dirs = check_dirs[:1] + check_dirs[2:] + check_dirs[1:2]

min_row = min(row for row, col in elves)
max_row = max(row for row, col in elves)
min_col = min(col for row, col in elves)
max_col = max(col for row, col in elves)
print((max_row - min_row + 1) * (max_col - min_col + 1) - elves_count)
