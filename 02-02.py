score = 0
while True:
    inputval = input()
    if inputval == "END":
        break
    op, you = inputval.split()
    opval = ord(op) - ord('A')
    result = ord(you) - ord('X')
    youval = (opval + result + 2) % 3
    score += youval + 1
    # result = (youval + 3 - opval) % 3
    if result == 1:
        score += 3
    elif result == 2:
        score += 6
print(score)
