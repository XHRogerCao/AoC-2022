import functools
signals = [[[2]], [[6]]]
while True:
    inputval = input()
    if inputval == "": break
    signals.append(eval(inputval))
    signals.append(eval(input()))
    input()
def compare_values(a, b):
    if type(a) is int:
        if type(b) is int:
            return a - b
        else:
            return compare_values([a], b)
    else:
        if type(b) is int:
            return compare_values(a, [b])
        else:
            for i in range(min(len(a), len(b))):
                val = compare_values(a[i], b[i])
                if val != 0:
                    return val
            return len(a) - len(b)
signals.sort(key=functools.cmp_to_key(compare_values))

score = 1

for i in range(len(signals)):
    if compare_values(signals[i], [[2]]) == 0 or compare_values(signals[i], [[6]]) == 0:
        score = score * (i + 1)
print(score)
