trees = []
while True:
    inputval = input()
    if inputval == "": break
    trees.append(inputval)
tree_score = []
count = 0
for row in trees:
    tree_score.append([1] * len(row))
for i in range(len(trees)):
    height_stack = []
    for j in range(len(trees[0])):
        height = int(trees[i][j])
        max_dist = 0
        for tree_height, idx in reversed(height_stack):
            if tree_height >= height:
                max_dist = idx
                break
        tree_score[i][j] = tree_score[i][j] * (j - max_dist)
        while height_stack and height >= height_stack[-1][0]:
            height_stack.pop()
        height_stack.append((height, j))
    height_stack = []
    for j in reversed(range(len(trees[0]))):
        height = int(trees[i][j])
        max_dist = len(trees[0]) - 1
        for tree_height, idx in reversed(height_stack):
            if tree_height >= height:
                max_dist = idx
                break
        tree_score[i][j] = tree_score[i][j] * (max_dist - j)
        while height_stack and height >= height_stack[-1][0]:
            height_stack.pop()
        height_stack.append((height, j))
for j in range(len(trees[0])):
    height_stack = []
    for i in range(len(trees)):
        height = int(trees[i][j])
        max_dist = 0
        for tree_height, idx in reversed(height_stack):
            if tree_height >= height:
                max_dist = idx
                break
        tree_score[i][j] = tree_score[i][j] * (i - max_dist)
        while height_stack and height >= height_stack[-1][0]:
            height_stack.pop()
        height_stack.append((height, i))
    height_stack = []
    for i in reversed(range(len(trees))):
        height = int(trees[i][j])
        max_dist = len(trees) - 1
        for tree_height, idx in reversed(height_stack):
            if tree_height >= height:
                max_dist = idx
                break
        tree_score[i][j] = tree_score[i][j] * (max_dist - i)
        while height_stack and height >= height_stack[-1][0]:
            height_stack.pop()
        height_stack.append((height, i))
print(tree_score)
print(max(max(row) for row in tree_score))
