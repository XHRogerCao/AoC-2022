score = 0
snafu_map = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}
snafu_map_inverse = {v: k for k, v in snafu_map.items()}
while True:
    inputval = input()
    if inputval == "": break
    one_score = 0
    for digit in inputval:
        one_score *= 5
        one_score += snafu_map[digit]
    score += one_score
print(score)
digits = []
while score > 0:
    digits.append(score % 5)
    score = score // 5
i = 0
while i < len(digits):
    if digits[i] >= 3:
        digits[i] -= 5
        if i < len(digits) - 1:
            digits[i + 1] += 1
        else:
            digits.append(1)
    i += 1
for digit in reversed(digits):
    print(snafu_map_inverse[digit], end="")
print()
