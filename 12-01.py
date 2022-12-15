from collections import deque

height_map = []
min_dist = []
bfs_queue = deque()
target_location = None
while True:
    inputval = input()
    if inputval == "": break
    height_map.append([])
    min_dist.append([])
    for i in range(len(inputval)):
        if inputval[i] == 'S':
            height_map[-1].append(1)
            min_dist[-1].append(0)
            bfs_queue.append((len(height_map) - 1, i))
        elif inputval[i] == 'E':
            height_map[-1].append(26)
            min_dist[-1].append(-1)
            target_location = (len(height_map) - 1, i)
        else:
            height_map[-1].append(ord(inputval[i]) - ord('a') + 1)
            min_dist[-1].append(-1)
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while min_dist[target_location[0]][target_location[1]] == -1:
    row, col = bfs_queue.popleft()
    for rowDelta, colDelta in dirs:
        newRow, newCol = row + rowDelta, col + colDelta
        if newRow >= 0 and newRow < len(height_map) and newCol >= 0 and newCol < len(height_map[newRow]):
            if min_dist[newRow][newCol] == -1 and height_map[newRow][newCol] - height_map[row][col] <= 1:
                min_dist[newRow][newCol] = min_dist[row][col] + 1
                bfs_queue.append((newRow, newCol))
print(min_dist[target_location[0]][target_location[1]])
