inputval = input()
charSet = {}
diffChars = 0
for i in range(4):
    if inputval[i] not in charSet:
        charSet[inputval[i]] = 0
    charSet[inputval[i]] = charSet[inputval[i]] + 1
    if charSet[inputval[i]] == 1:
        diffChars += 1
i = 0
while diffChars < 4:
    if inputval[i + 4] not in charSet:
        charSet[inputval[i + 4]] = 0
    charSet[inputval[i + 4]] = charSet[inputval[i + 4]] + 1
    if charSet[inputval[i + 4]] == 1:
        diffChars += 1
    charSet[inputval[i]] = charSet[inputval[i]] - 1
    if charSet[inputval[i]] == 0:
        diffChars -= 1
    i += 1
print(i + 4)
