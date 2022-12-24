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
elves_moved = 1
iters = 0
while elves_moved:
    iters += 1
    new_elves = {}
    elves_moved = 0
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
            elves_moved -= 1
        else:
            new_elves[new_pos] = elf
            if new_pos != elf:
                elves_moved += 1
    elves = new_elves
    check_dirs = check_dirs[:1] + check_dirs[2:] + check_dirs[1:2]
print(iters)
