register = 1
cycle_num = 0
cycles = 40
crtOutput = ""
def outputPixel():
    global crtOutput
    if abs(register - cycle_num) <= 1:
        crtOutput += '#'
    else:
        crtOutput += '.'
while True:
    inputval = input()
    if inputval == '': break
    inputvals = inputval.split()
    if inputvals[0] == 'noop':
        outputPixel()
        cycle_num += 1
        if cycles and cycle_num >= cycles:
            cycle_num = 0
            crtOutput += '\n'
    else:
        for i in range(2):
            outputPixel()
            cycle_num += 1
            if cycles and cycle_num >= cycles:
                cycle_num = 0
                crtOutput += '\n'
        register += int(inputvals[1])
print(crtOutput)
