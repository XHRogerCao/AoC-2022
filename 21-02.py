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
    if monkeyId == "humn":
        ops[monkeyId] = monkeyId
        empty_queue.append(monkeyId)
    elif len(vals) == 2:
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
        if type(ops[ops[monkeyId][0]]) is int and type(ops[ops[monkeyId][2]]) is int:
            if ops[monkeyId][1] == "+":
                ops[monkeyId] = ops[ops[monkeyId][0]] + ops[ops[monkeyId][2]]
            elif ops[monkeyId][1] == "-":
                ops[monkeyId] = ops[ops[monkeyId][0]] - ops[ops[monkeyId][2]]
            elif ops[monkeyId][1] == "*":
                ops[monkeyId] = ops[ops[monkeyId][0]] * ops[ops[monkeyId][2]]
            elif ops[monkeyId][1] == "/":
                ops[monkeyId] = ops[ops[monkeyId][0]] // ops[ops[monkeyId][2]]
        else:
            ops[monkeyId][0] = ops[ops[monkeyId][0]]
            ops[monkeyId][2] = ops[ops[monkeyId][2]]
    if monkeyId == "root":
        target, op_left = None, None
        if type(ops[monkeyId][0]) is int:
            target, op_left = ops[monkeyId][0], ops[monkeyId][2]
        else:
            target, op_left = ops[monkeyId][2], ops[monkeyId][0]
        assert type(target) is int, "target must be int"
        # print(target)
        # print(op_left)
        while type(op_left) is list:
            if op_left[1] == "+":
                if type(op_left[0]) is int:
                    target, op_left = target - op_left[0], op_left[2]
                else:
                    target, op_left = target - op_left[2], op_left[0]
            elif op_left[1] == "-":
                if type(op_left[0]) is int:
                    target, op_left = op_left[0] - target, op_left[2]
                else:
                    target, op_left = target + op_left[2], op_left[0]
            elif op_left[1] == "*":
                if type(op_left[0]) is int:
                    target, op_left = target // op_left[0], op_left[2]
                else:
                    target, op_left = target // op_left[2], op_left[0]
            elif op_left[1] == "/":
                if type(op_left[0]) is int:
                    target, op_left = op_left[0] // target, op_left[2]
                else:
                    target, op_left = target * op_left[2], op_left[0]
        print(target)
        break
    if monkeyId in preds:
        for newMonkey in preds[monkeyId]:
            deps[newMonkey] -= 1
            if deps[newMonkey] == 0:
                empty_queue.append(newMonkey)
