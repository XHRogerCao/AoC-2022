register = 1
score = 0
cycle_num = 0
cycles = [220, 180, 140, 100, 60, 20]
while True:
    inputval = input()
    if inputval == '': break
    inputvals = inputval.split()
    if inputvals[0] == 'noop':
        cycle_num += 1
        if cycles and cycle_num >= cycles[-1]:
            score += cycles[-1] * register
            print(cycles[-1] * register)
            cycles.pop()
    else:
        cycle_num += 2
        if cycles and cycle_num >= cycles[-1]:
            score += cycles[-1] * register
            print(cycles[-1] * register)
            cycles.pop()
        register += int(inputvals[1])
print(score)
