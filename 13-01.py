left_signals = []
right_signals = []
while True:
    inputval = input()
    if inputval == "": break
    left_signals.append(eval(inputval))
    right_signals.append(eval(input()))
    input()
score = 0
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
for i in range(len(left_signals)):
    if compare_values(left_signals[i], right_signals[i]) < 0:
        score += i + 1
print(score)
