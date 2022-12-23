coords = []
origin_to_cur = []
cur_to_origin = []
zero_index = 0
def swap_coord(i, j):
    origin_to_cur[cur_to_origin[i]], origin_to_cur[cur_to_origin[j]] = origin_to_cur[cur_to_origin[j]], origin_to_cur[cur_to_origin[i]]
    cur_to_origin[i], cur_to_origin[j] = cur_to_origin[j], cur_to_origin[i]
while True:
    inputval = input()
    if inputval == "": break
    coords.append(int(inputval) * 811589153)
    if inputval == "0":
        zero_index = len(origin_to_cur)
    origin_to_cur.append(len(origin_to_cur))
    cur_to_origin.append(len(cur_to_origin))
for _ in range(10):
    for i in range(len(origin_to_cur)):
        val = coords[i]
        moves = val % (len(coords) - 1)
        cur_coord = origin_to_cur[i]
        if cur_coord + moves < len(coords):
            for j in range(moves):
                swap_coord(cur_coord + j, cur_coord + j + 1)
        else:
            for j in range(len(coords) - 1 - moves):
                swap_coord(cur_coord - j - 1, cur_coord - j)
cur_zero_index = origin_to_cur[zero_index]
x, y, z = coords[cur_to_origin[(cur_zero_index + 1000) % len(cur_to_origin)]], coords[cur_to_origin[(cur_zero_index + 2000) % len(cur_to_origin)]], coords[cur_to_origin[(cur_zero_index + 3000) % len(cur_to_origin)]]
print(x + y + z)
