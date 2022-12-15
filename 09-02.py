rope = []
for i in range(10):
    rope.append((0, 0))
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
        rope[0] = (deltas[dir][0] + rope[0][0], deltas[dir][1] + rope[0][1])
        for j in range(9):
            diff = (rope[j][0] - rope[j + 1][0], rope[j][1] - rope[j + 1][1])
            if abs(diff[0]) >= 2 or abs(diff[1]) >= 2:
                rope[j + 1] = (rope[j + 1][0] + sign(diff[0]), rope[j + 1][1] + sign(diff[1]))
        visited.add(rope[-1])
print(len(visited))
