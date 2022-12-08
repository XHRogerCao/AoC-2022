stacks: list[list] = []
stack_count = int(input())
for i in range(stack_count):
    stacks.append([])
while True:
    inputval = input()
    if inputval[1] == "1":
        break
    for i in range(stack_count):
        cargo = inputval[1 + 4 * i]
        if cargo != " ":
            stacks[i].insert(0, cargo)
input()
while True:
    inst = input()
    if inst == "": break
    words = inst.split(" ")
    count = int(words[1])
    start = int(words[3]) - 1
    end = int(words[5]) - 1
    for i in range(count):
        stacks[end].append(stacks[start].pop())

for stack in stacks:
    print(stack[-1], end="")
print("")
