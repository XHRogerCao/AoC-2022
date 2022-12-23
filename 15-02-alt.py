import re
# (1,0) on original grid rotates to (1,1) on square grid, while (0,1) on original grid rotates to (-1,1)
# As such, newX = oldX - oldY, newY = oldX + oldY
# Also, for the squares, after rotation, the radius doesn't change
# Square events stores these: (triggeredX, event type(0 for insert, 1 for delete), minY, maxY)
square_events = []
row = int(input())
idx = 0
while True:
    inputval = input()
    if inputval == "": break
    match = re.match(r"Sensor at x=(\-?[0-9]+), y=(\-?[0-9]+): closest beacon is at x=(\-?[0-9]+), y=(\-?[0-9]+)", inputval)
    sx, sy, bx, by = int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))
    dist = abs(sx - bx) + abs(sy - by)
    rsx, rsy = sx - sy, sx + sy
    # print(rsx, rsy)
    square_events.append((rsx - dist, 0, rsy - dist, rsy + dist, idx))
    square_events.append((rsx + dist + 1, 1, rsy - dist, rsy + dist, idx))
    idx += 1
square_events.sort()
edge_set = []
def calc_gap(minY, maxY, parity):
    ranges = {}
    def add_range(start, end):
        nonlocal ranges
        start = max(minY, start)
        end = min(maxY, end)
        if start > end: return
        for key in ranges:
            if end + 1 >= key and start <= ranges[key] + 1:
                # Overlap
                old_start, old_end = key, ranges[key]
                del ranges[key]
                add_range(min(start, old_start), max(end, old_end))
                return
        ranges[start] = end
    for edge_start, edge_end in edge_set:
        add_range(edge_start, edge_end)
    current_pos = minY
    # print(ranges)
    while current_pos in ranges and current_pos % 2 == parity:
        current_pos = ranges[current_pos] + 2
    if current_pos % 2 != parity:
        current_pos -= 1
    if current_pos > maxY:
        return None
    return current_pos
for i in range(len(square_events)):
    rx, eType, minY, maxY, idx = square_events[i]
    # print(rx, eType, minY, maxY, idx)
    if eType == 0:
        edge_set.append((minY, maxY))
        # print(edge_set)
        if rx >= -row and rx <= row and (i == len(square_events) - 1 or rx != square_events[i + 1][0]):
            # print(rx, abs(rx), row * 2 - abs(rx))
            gap = calc_gap(abs(rx), row * 2 - abs(rx), abs(rx) % 2)
            if gap:
                # Found correct gap. Now actually need to unrotate
                print("Found gap")
                x, y = (rx + gap) // 2, (gap - rx) // 2
                print(x, y)
                print(x * 4000000 + y)
                break
    else:
        edge_set.remove((minY, maxY))
        # print(edge_set)
        if rx >= -row and rx <= row and (i == len(square_events) - 1 or rx != square_events[i + 1][0]):
            # print(rx, abs(rx), row * 2 - abs(rx))
            gap = calc_gap(abs(rx), row * 2 - abs(rx), abs(rx) % 2)
            if gap:
                # Found correct gap. Now actually need to unrotate
                print("Found gap")
                print(rx, gap)
                x, y = (rx + gap) // 2, (gap - rx) // 2
                print(x, y)
                print(x * 4000000 + y)
                break
