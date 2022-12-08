def get_priority(c):
    if c >= 'a' and c <= 'z':
        return ord(c) - ord('a') + 1
    return ord(c) - ord('A') + 27
score = 0
while True:
    str1 = input()
    if str1 == "": break
    str2 = input()
    str3 = input()
    first = {}
    second = {}
    third = {}
    for c in str1:
        first[c] = 1
    for c in str2:
        second[c] = 1
    for c in str3:
        third[c] = 1
    for c in first:
        if c in second and c in third:
            score += get_priority(c)
print(score)
