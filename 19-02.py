import re
score = 1
while True:
    inputval = input()
    if inputval == "": break
    match = re.match(r"Blueprint ([0-9]+): Each ore robot costs ([0-9]+) ore. Each clay robot costs ([0-9]+) ore. Each obsidian robot costs ([0-9]+) ore and ([0-9]+) clay. Each geode robot costs ([0-9]+) ore and ([0-9]+) obsidian.", inputval)
    bpid = int(match.group(1))
    ore_orecost, clay_orecost, obs_orecost, obs_claycost, geo_orecost, geo_obscost = int(match.group(2)), int(match.group(3)), int(match.group(4)), int(match.group(5)), int(match.group(6)), int(match.group(7))
    max_orecost = max(ore_orecost, clay_orecost, obs_orecost, geo_orecost)
    # max_score = 0
    current_sets = {(0, 0, 0, 1): [(0, 0, 0, 0)]}
    for i in reversed(range(1, 32 + 1)):
        next_sets = {}
        def add_resource_count(bs, rs):
            if bs not in next_sets:
                next_sets[bs] = []
            next_sets[bs].append(rs)
        for bs in current_sets:
            for rs in current_sets[bs]:
                add_resource_count(bs, (rs[0] + bs[0], rs[1] + bs[1], rs[2] + bs[2], rs[3] + bs[3]))
                if rs[3] >= ore_orecost and bs[3] < max_orecost:
                    add_resource_count((bs[0], bs[1], bs[2], bs[3] + 1), (rs[0] + bs[0], rs[1] + bs[1], rs[2] + bs[2], rs[3] + bs[3] - ore_orecost))
                if rs[3] >= clay_orecost and bs[2] < obs_claycost:
                    add_resource_count((bs[0], bs[1], bs[2] + 1, bs[3]), (rs[0] + bs[0], rs[1] + bs[1], rs[2] + bs[2], rs[3] + bs[3] - clay_orecost))
                if rs[3] >= obs_orecost and rs[2] >= obs_claycost and bs[1] < geo_obscost:
                    add_resource_count((bs[0], bs[1] + 1, bs[2], bs[3]), (rs[0] + bs[0], rs[1] + bs[1], rs[2] + bs[2] - obs_claycost, rs[3] + bs[3] - obs_orecost))
                if rs[3] >= geo_orecost and rs[1] >= geo_obscost:
                    add_resource_count((bs[0] + 1, bs[1], bs[2], bs[3]), (rs[0] + bs[0], rs[1] + bs[1] - geo_obscost, rs[2] + bs[2], rs[3] + bs[3] - geo_orecost))
        for bs in next_sets:
            compressed_sets = []
            for rs in sorted(next_sets[bs], reverse=True):
                if not compressed_sets:
                    compressed_sets.append(rs)
                    continue
                worse = False
                for better_res in compressed_sets:
                    if min(rs[1], 2 * geo_obscost) > min(better_res[1], 2 * geo_obscost):
                        continue
                    if min(rs[2], 2 * obs_claycost) > min(better_res[2], 2 * obs_claycost):
                        continue
                    if min(rs[3], 2 * max_orecost) > min(better_res[3], 2 * max_orecost):
                        continue
                    # if rs[1] > better_res[1]:
                    #     continue
                    # if rs[2] > better_res[2]:
                    #     continue
                    # if rs[3] > better_res[3]:
                    #     continue
                    worse = True
                if not worse:
                    compressed_sets.append(rs)
            next_sets[bs] = compressed_sets
        current_sets = next_sets
        # possibility_count = sum(len(rs) for rs in current_sets.values())
        # print(f"T-{i}, {possibility_count} possibilities")
    max_score = max(max(rs) for rs in current_sets.values())
    max_score = max_score[0]
    # print(max_score)
    score *= max_score
print(score)
