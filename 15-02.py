import re
ranges = []
row = int(input())
for i in range(row + 1):
    ranges.append({})
def add_range(y, start, end):
    global ranges
    if y < 0 or y > row: return
    start = max(0, start)
    end = min(row, end)
    for key in ranges[y]:
        if end + 1 >= key and start <= ranges[y][key] + 1:
            # Overlap
            old_start, old_end = key, ranges[y][key]
            del ranges[y][key]
            add_range(y, min(start, old_start), max(end, old_end))
            return
    ranges[y][start] = end
while True:
    inputval = input()
    if inputval == "": break
    match = re.match(r"Sensor at x=(\-?[0-9]+), y=(\-?[0-9]+): closest beacon is at x=(\-?[0-9]+), y=(\-?[0-9]+)", inputval)
    sx, sy, bx, by = int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))
    dist = abs(sx - bx) + abs(sy - by)
    for deltaY in range(-dist, dist + 1):
        xdist = dist - abs(deltaY)
        if xdist >= 0:
            add_range(sy + deltaY, sx - xdist, sx + xdist)
for y in range(row + 1):
    if 0 not in ranges[y]:
        # Special case.
        print(0, y)
        print(y)
        break
    if ranges[y][0] != row:
        print(ranges[y][0] + 1, y)
        print((ranges[y][0] + 1) * 4000000 + y)
        break
