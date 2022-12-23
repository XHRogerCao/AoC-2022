from collections import deque
grid_size = 20
cubes = []
for i in range(grid_size + 2):
    cubes.append([])
    for j in range(grid_size + 2):
        cubes[-1].append([0] * (grid_size + 2))
score = 0
dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
while True:
    row = input()
    if row == "": break
    new_cube = tuple(map(lambda x: int(x), row.split(",")))
    cubes[new_cube[0] + 1][new_cube[1] + 1][new_cube[2] + 1] = 1

bfs_queue = deque()
bfs_queue.append((-1, -1, -1))
cubes[0][0][0] = -1
while bfs_queue:
    px, py, pz = bfs_queue.popleft()
    for dx, dy, dz in dirs:
        nx, ny, nz = px + dx, py + dy, pz + dz
        if nx < -1 or nx > grid_size or ny < -1 or ny > grid_size or nz < -1 or nz > grid_size:
            continue
        if cubes[nx + 1][ny + 1][nz + 1] == 1:
            score += 1
        elif cubes[nx + 1][ny + 1][nz + 1] == 0:
            cubes[nx + 1][ny + 1][nz + 1] = -1
            bfs_queue.append((nx, ny, nz))
print(score)
