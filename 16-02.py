import re
from collections import deque

valves = {}
important_valves = {"AA"}
while True:
    inputval = input()
    if inputval == "": break
    match = re.match(r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ([\w, ]+)", inputval)
    valve, rate, edges = match.group(1), int(match.group(2)), match.group(3).split(", ")
    valves[valve] = (rate, edges)
    if rate != 0:
        important_valves.add(valve)
compressed_valves = {}
for valve in important_valves:
    dist = {valve: 0}
    bfsQueue = deque()
    bfsQueue.append(valve)
    while bfsQueue:
        currentValve = bfsQueue.popleft()
        for adjacentValve in valves[currentValve][1]:
            if adjacentValve not in dist:
                dist[adjacentValve] = dist[currentValve] + 1
                bfsQueue.append(adjacentValve)
    compressed_valves[valve] = {}
    for calcValve in important_valves:
        if valves[calcValve][0] != 0 and calcValve in dist and dist[calcValve] != 0:
            compressed_valves[valve][calcValve] = dist[calcValve]

all_scores = {}
def calc_score(current_score, current_loc, opened_valves, time_left):
    global all_scores
    unique_key = tuple(sorted(opened_valves))
    if unique_key in all_scores:
        all_scores[unique_key] = max(all_scores[unique_key], current_score)
    else:
        all_scores[unique_key] = current_score
    for connectedValve in compressed_valves[current_loc]:
        if connectedValve not in opened_valves and compressed_valves[current_loc][connectedValve] + 1 < time_left:
            new_opened_valves = opened_valves.copy()
            new_opened_valves.add(connectedValve)
            new_time_left = time_left - (compressed_valves[current_loc][connectedValve] + 1)
            calc_score(current_score + valves[connectedValve][0] * new_time_left, connectedValve, new_opened_valves, new_time_left)
calc_score(0, "AA", set(), 26)
print(len(all_scores))
max_score = 0
for set1 in all_scores:
    for set2 in all_scores:
        if set1 < set2:
            if not set(set1).intersection(set(set2)):
                # Intersection is empty, good for max score
                max_score = max(all_scores[set1] + all_scores[set2], max_score)
print(max_score)
