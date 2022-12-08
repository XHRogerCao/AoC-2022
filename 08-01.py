trees = []
while True:
    inputval = input()
    if inputval == "": break
    trees.append(inputval)
visible = []
count = 0
for row in trees:
    visible.append([False] * len(row))
for i in range(len(trees)):
    max_height = -1
    for j in range(len(trees[0])):
        if int(trees[i][j]) > max_height:
            if not visible[i][j]:
                count += 1
                visible[i][j] = True
            max_height = int(trees[i][j])
    max_height = -1
    for j in range(len(trees[0]) - 1, -1, -1):
        if int(trees[i][j]) > max_height:
            if not visible[i][j]:
                count += 1
                visible[i][j] = True
            max_height = int(trees[i][j])
for j in range(len(trees[0])):
    max_height = -1
    for i in range(len(trees)):
        if int(trees[i][j]) > max_height:
            if not visible[i][j]:
                count += 1
                visible[i][j] = True
            max_height = int(trees[i][j])
    max_height = -1
    for i in range(len(trees) - 1, -1, -1):
        if int(trees[i][j]) > max_height:
            if not visible[i][j]:
                count += 1
                visible[i][j] = True
            max_height = int(trees[i][j])

print(count)
