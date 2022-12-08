max_cal = []
elf_total = 0
while True:
    inputval = input()
    if inputval and inputval != "" and inputval != "END":
        elf_total += int(inputval)
    else:
        max_cal.append(elf_total)
        max_cal.sort(reverse=True)
        if len(max_cal) > 3:
            max_cal.pop()
        elf_total = 0
        if inputval == "END":
            break
print(max_cal)
print(sum(max_cal))
