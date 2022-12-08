from bisect import bisect_left
directories = {}
currentDir = []
currentMaps = [directories]

isLs = False

while True:
    inputval = input()
    if inputval == "":
        break
    if isLs and inputval[0] == '$':
        isLs = False
    if not isLs:
        inputvals = inputval.split()
        if inputvals[1] == 'cd':
            if inputvals[2] == '..':
                currentDir.pop()
                currentMaps.pop()
            elif inputvals[2] == '/':
                currentDir.clear()
                currentMaps.clear()
                currentMaps.append(directories)
            else:
                currentDir.append(inputvals[2])
                if inputvals[2] not in currentMaps[-1]:
                    currentMaps[-1][inputvals[2]] = {}
                currentMaps.append(currentMaps[-1][inputvals[2]])
        else:
            isLs = True
    else:
        inputvals = inputval.split()
        if inputvals[0] == "dir":
            # Is a directory
            if inputvals[1] not in currentMaps[-1]:
                currentMaps[-1][inputvals[1]] = {}
        else:
            filesize = int(inputvals[0])
            currentMaps[-1][inputvals[1]] = filesize

directorySizes = []
def getDirectorySize(dir):
    size = 0
    for index in dir:
        if type(dir[index]) is dict:
            size += getDirectorySize(dir[index])
        else:
            size += dir[index]
    directorySizes.append(size)
    return size
rootSize = getDirectorySize(directories)

freeSpace = 70000000 - rootSize
spaceRequired = 30000000 - freeSpace

directorySizes.sort()
idx = bisect_left(directorySizes, spaceRequired)
print(directorySizes[idx])
