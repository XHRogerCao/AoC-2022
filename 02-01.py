score = 0
while True:
    inputval = input()
    if inputval == "END":
        break
    op, you = inputval.split()
    opval = ord(op) - ord('A')
    youval = ord(you) - ord('X')
    score += youval + 1
    result = (youval + 3 - opval) % 3
    if result == 0:
        score += 3
    elif result == 1:
        score += 6
print(score)
