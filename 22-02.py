import re
from math import sqrt
from collections import deque
raw_rows = []
max_row_size = 0
total_grid_size = 0
while True:
    inputval = input()
    if inputval == "": break
    raw_rows.append(inputval)
    max_row_size = max(max_row_size, len(inputval))
    total_grid_size += len(inputval.strip())
direction = 0
raw_moves = input()
moves = list(map(lambda x: int(x), re.findall(r"\d+", raw_moves)))
rotations = re.findall(r"L|R", raw_moves)
grid_length = int(sqrt(total_grid_size // 6))
# Stores edge coloring for cubes
# Two cubes are adjacent in a certain way if their color matches
cube_edge_match = [
    [2, 3, 4, 1],
    [5, 1, 7, 6],
    [4, 10, 9, 7],
    [8, 11, 2, 5],
    [9, 12, 8, 6],
    [11, 12, 10, 3]
]
edge_color = {}
row, col = None, None
bfs_queue = deque()
for i in range(0, len(raw_rows), grid_length):
    for j in range(0, len(raw_rows[i]), grid_length):
        if raw_rows[i][j] != " ":
            if row is None:
                row, col = i, j
                edge_color[(i // grid_length, j // grid_length)] = cube_edge_match[0]
                cube_edge_match.pop(0)
                bfs_queue.append((i // grid_length, j // grid_length))
                break
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
while bfs_queue:
    cube_row, cube_col = bfs_queue.popleft()
    for i in range(len(dirs)):
        drow, dcol = dirs[i]
        newrow, newcol = cube_row + drow, cube_col + dcol
        # print(cube_row, cube_col, i, newrow, newcol)
        if newrow >= 0 and newrow * grid_length < len(raw_rows) and newcol >= 0 and newcol * grid_length < len(raw_rows[newrow * grid_length]):
            if raw_rows[newrow * grid_length][newcol * grid_length] != " " and (newrow, newcol) not in edge_color:
                # There is a square
                color_edge = edge_color[(cube_row, cube_col)][i]
                for j in range(len(cube_edge_match)):
                    if color_edge in cube_edge_match[j]:
                        idx = cube_edge_match[j].index(color_edge)
                        offset = (idx - i + 2) % 4
                        edge_color[(newrow, newcol)] = cube_edge_match[j][offset:] + cube_edge_match[j][:offset]
                        bfs_queue.append((newrow, newcol))
                        cube_edge_match.pop(j)
                        break
print(edge_color)
for move in range(len(moves)):
    for _ in range(moves[move]):
        blockrow, blockcol = row // grid_length, col // grid_length
        drow, dcol = dirs[direction]
        nrow, ncol = row + drow, col + dcol
        ndir = direction
        nbrow, nbcol = nrow // grid_length, ncol // grid_length
        if blockrow != nbrow or blockcol != nbcol:
            # Wrap around occurs.
            dbrow, dbcol = nbrow - blockrow, nbcol - blockcol
            wrap_dir = direction
            color_edge = edge_color[(blockrow, blockcol)][wrap_dir]
            for destrow, destcol in edge_color:
                if destrow != blockrow or destcol != blockcol:
                    if color_edge in edge_color[(destrow, destcol)]:
                        dest_dir = edge_color[(destrow, destcol)].index(color_edge)
                        nrow += (destrow - nbrow) * grid_length
                        ncol += (destcol - nbcol) * grid_length
                        # Rotate within grid
                        if (dest_dir - wrap_dir) % 4 == 3:
                            nrow, ncol = destrow * grid_length + (ncol % grid_length), destcol * grid_length + grid_length - 1 - (nrow % grid_length)
                        elif (dest_dir - wrap_dir) % 4 == 0:
                            nrow, ncol = destrow * grid_length + grid_length - 1 - (nrow % grid_length), destcol * grid_length + grid_length - 1 - (ncol % grid_length)
                        elif (dest_dir - wrap_dir) % 4 == 1:
                            nrow, ncol = destrow * grid_length + grid_length - 1 - (ncol % grid_length), destcol * grid_length + (nrow % grid_length)
                        ndir = (ndir + dest_dir + 2 - wrap_dir) % 4
                        break
        # print(nrow, ncol, ndir, end="")
        if raw_rows[nrow][ncol] == ".":
            row, col, direction = nrow, ncol, ndir
            # print(" moved")
        else:
            # print(" stopped")
            break

    if move < len(rotations):
        if rotations[move] == "R":
            direction = (direction + 1) % 4
        else:
            direction = (direction + 3) % 4
print(row, col, direction)
print((row + 1) * 1000 + (col + 1) * 4 + direction)
