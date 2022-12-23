from collections import deque
deps = {}
ops = {}
preds = {}
empty_queue = deque()
while True:
    inputval = input()
    if inputval == "": break
    vals = inputval.split()
    monkeyId = vals[0][:-1]
    if len(vals) == 2:
        ops[monkeyId] = int(vals[1])
        empty_queue.append(monkeyId)
    else:
        if vals[1] not in preds:
            preds[vals[1]] = []
        preds[vals[1]].append(monkeyId)
        if vals[3] not in preds:
            preds[vals[3]] = []
        preds[vals[3]].append(monkeyId)
        deps[monkeyId] = 2
        ops[monkeyId] = vals[1:]
while empty_queue:
    monkeyId = empty_queue.popleft()
    if type(ops[monkeyId]) == list:
        if ops[monkeyId][1] == "+":
            ops[monkeyId] = ops[ops[monkeyId][0]] + ops[ops[monkeyId][2]]
        elif ops[monkeyId][1] == "-":
            ops[monkeyId] = ops[ops[monkeyId][0]] - ops[ops[monkeyId][2]]
        elif ops[monkeyId][1] == "*":
            ops[monkeyId] = ops[ops[monkeyId][0]] * ops[ops[monkeyId][2]]
        elif ops[monkeyId][1] == "/":
            ops[monkeyId] = ops[ops[monkeyId][0]] // ops[ops[monkeyId][2]]
    if monkeyId == "root":
        print(ops[monkeyId])
        break
    if monkeyId in preds:
        for newMonkey in preds[monkeyId]:
            deps[newMonkey] -= 1
            if deps[newMonkey] == 0:
                empty_queue.append(newMonkey)
