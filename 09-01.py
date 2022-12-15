head = (0, 0)
tail = (0, 0)
visited = {(0, 0)}
deltas = {
    'U': [0, 1],
    'D': [0, -1],
    'L': [-1, 0],
    'R': [1, 0]
}
def sign(n):
    if n > 0:
        return 1
    if n < 0:
        return -1
    return 0
while True:
    inputval = input()
    if inputval == "": break
    dir, moves = inputval.split()
    moves = int(moves)
    for i in range(moves):
        head = (deltas[dir][0] + head[0], deltas[dir][1] + head[1])
        diff = (head[0] - tail[0], head[1] - tail[1])
        if abs(diff[0]) >= 2 or abs(diff[1]) >= 2:
            tail = (tail[0] + sign(diff[0]), tail[1] + sign(diff[1]))
        visited.add(tail)
print(len(visited))
