rocks = []
while True:
    inputval = input()
    if inputval == "": break
    rocks.append([tuple(int(x) for x in oneCoord.split(",")) for oneCoord in inputval.split(" -> ")])
min_x = min(min(coord[0] for coord in line) for line in rocks)
max_x = max(max(coord[0] for coord in line) for line in rocks)
max_y = max(max(coord[1] for coord in line) for line in rocks)

print(min_x, max_x, max_y)

# 0 for air, 1 for stone, 2 for sand
caveMap = [[0] * (max_y + 1) for i in range(min_x, max_x + 1)]

for line in rocks:
    for start, end in zip(line[:-1], line[1:]):
        if start[0] < end[0]:
            for i in range(start[0], end[0] + 1):
                caveMap[i - min_x][start[1]] = 1
        else:
            for i in range(end[0], start[0] + 1):
                caveMap[i - min_x][start[1]] = 1
        if start[1] < end[1]:
            for i in range(start[1], end[1] + 1):
                caveMap[start[0] - min_x][i] = 1
        else:
            for i in range(end[1], start[1] + 1):
                caveMap[start[0] - min_x][i] = 1

score = 0
while True:
    sandX, sandY = 500, 0
    while sandY < max_y and sandX > min_x and sandX < max_x:
        if caveMap[sandX - min_x][sandY + 1] == 0:
            sandY += 1
        elif caveMap[sandX - min_x - 1][sandY + 1] == 0:
            sandY += 1
            sandX += -1
        elif caveMap[sandX - min_x + 1][sandY + 1] == 0:
            sandY += 1
            sandX += 1
        else:
            caveMap[sandX - min_x][sandY] = 2
            score += 1
            break
    if not (sandY < max_y and sandX > min_x and sandX < max_x):
        # Reached the edge. Break
        break
print(score)
