cubes = set()
score = 0
dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
while True:
    row = input()
    if row == "": break
    new_cube = tuple(map(lambda x: int(x), row.split(",")))
    cubes.add(new_cube)
    for dx, dy, dz in dirs:
        adj_block = new_cube[0] + dx, new_cube[1] + dy, new_cube[2] + dz
        if adj_block in cubes:
            score -= 1
        else:
            score += 1
print(score)
