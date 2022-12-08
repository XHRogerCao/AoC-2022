count = 0
while True:
    inval = input()
    if inval == "": break
    first_range, second_range = inval.split(",")
    first_start, first_end = first_range.split("-")
    second_start, second_end = second_range.split("-")
    first_start = int(first_start)
    first_end = int(first_end)
    second_start = int(second_start)
    second_end = int(second_end)
    if (first_start >= second_start and first_end <= second_end) or (first_start <= second_start and first_end >= second_end):
        count += 1
print(count)
