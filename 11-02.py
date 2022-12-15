class Monkey:
    def __init__(self, items = None, transition = None, test = None, ifTrue = None, ifFalse = None) -> None:
        self.items = items
        self.transition = transition
        self.test = test
        self.ifTrue = ifTrue
        self.ifFalse = ifFalse

monkeys = []

def make_lambda(op, val):
    if op == "+":
        return lambda old: old + (old if val == "old" else int(val))
    else:
        return lambda old: old * (old if val == "old" else int(val))

while True:
    inputval = input()
    if inputval == "": break
    monkey = Monkey()
    monkey.items = list(map(lambda x: int(x), input()[18:].split(", ")))
    newFunc = input()[23:].split()
    monkey.transition = make_lambda(*newFunc)
    monkey.test = int(input()[21:])
    monkey.ifTrue = int(input()[29:])
    monkey.ifFalse = int(input()[30:])
    monkeys.append(monkey)
    input()

inspections = [0] * len(monkeys)

lcmVal = 1

# Manually check that the monkeys have prime test values
for monkey in monkeys:
    lcmVal = lcmVal * monkey.test

for i in range(10000):
    for j in range(len(monkeys)):
        monkey = monkeys[j]
        for item in monkey.items:
            item = monkey.transition(item) % lcmVal
            inspections[j] += 1
            if item % monkey.test == 0:
                monkeys[monkey.ifTrue].items.append(item)
            else:
                monkeys[monkey.ifFalse].items.append(item)
        monkey.items.clear()
print(inspections)
inspections.sort()
print(inspections[-1] * inspections[-2])
