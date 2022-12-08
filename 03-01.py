def get_priority(c):
    if c >= 'a' and c <= 'z':
        return ord(c) - ord('a') + 1
    return ord(c) - ord('A') + 27
score = 0
while True:
    inputval = input()
    if inputval == "": break
    first = {}
    second = {}
    sack_length = len(inputval)
    for i in range(sack_length // 2):
        first[inputval[i]] = 1
        second[inputval[i + sack_length // 2]] = 1
    for c in first:
        if c in second:
            score += get_priority(c)
print(score)
