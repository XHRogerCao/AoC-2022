import re
ranges = {}
row = int(input())
included_beacons = set()
def add_range(start, end):
    global ranges
    for key in ranges:
        if end + 1 >= key and start <= ranges[key] + 1:
            # Overlap
            old_start, old_end = key, ranges[key]
            del ranges[key]
            add_range(min(start, old_start), max(end, old_end))
            return
    ranges[start] = end
while True:
    inputval = input()
    if inputval == "": break
    match = re.match(r"Sensor at x=(\-?[0-9]+), y=(\-?[0-9]+): closest beacon is at x=(\-?[0-9]+), y=(\-?[0-9]+)", inputval)
    sx, sy, bx, by = int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))
    dist = abs(sx - bx) + abs(sy - by)
    xdist = dist - abs(sy - row)
    if xdist >= 0:
        add_range(sx - xdist, sx + xdist)
    if by == row:
        included_beacons.add(bx)
score = 0
for start in ranges:
    score += ranges[start] - start + 1
    for beacon in included_beacons:
        if beacon >= start and beacon <= ranges[start]:
            score -= 1
print(score)
