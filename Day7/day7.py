# {directory_path: [[file, size],[file, size], [file, size]],
#  directory_path: [[file, size],[file, size]]}

TESTING = 0
HDSIZE = 70000000
SPACENEEDED = 30000000


def convertToTuple (itemToConvert):
    # convert lists of lists inside a dictionary to tuples of tuples inside a dictionary
    if type(itemToConvert) == dict:
        for dictKey in itemToConvert.keys():
            itemToConvert[dictKey] = tuple(tuple(x) for x in itemToConvert[dictKey])
    return itemToConvert


def buildTree():
    # loop through cli and build dictionary of directories and every file in each of them wth their sizes
    filesAndDirs = {}
    currentPath = ""
    if TESTING:
        f = open("sample_input.txt", "r")
    else:
        f = open("input.txt", "r")

    cliLine = f.readline().replace("/n", "").strip().split()

    while cliLine != []:
        if cliLine[1] == "ls":
            pass
        elif cliLine[0] == "dir":
            pass
        elif cliLine[1] == "cd" and cliLine[2] != "..":
            currentPath = (currentPath + "/" + cliLine[2]).replace("//", "/")
            filesAndDirs[currentPath] = []
        elif cliLine[0].isalnum():
            # check for duplicate and add to list if no duplicate
            if [cliLine[1], cliLine[0]] not in filesAndDirs[currentPath]:
                filesAndDirs[currentPath].append([cliLine[1], cliLine[0]])
        elif cliLine[1] == "cd" and cliLine[2] == "..":
            currentPath = currentPath.rsplit("/", 1)[0]

        cliLine = f.readline().replace("/n", "").strip().split()

    return convertToTuple(filesAndDirs)


def buildSummary(directoryTree):
    # take full tree and build a summary dictionary {directory: size}
    summaryDict = {}
    for dictKey in directoryTree:
        cumTotal = 0
        for file in directoryTree[dictKey]:
            cumTotal += int(file[1])
        summaryDict[dictKey] = cumTotal
    return summaryDict


def calculateCumTotals(directorySummary):
    cumDict = {}
    for pathOrigin in directorySummary.keys():
        cumTotal = 0
        for pathDest in directorySummary.keys():
            if pathDest.startswith(pathOrigin):
                cumTotal += directorySummary[pathDest]
        cumDict[pathOrigin] = cumTotal
    return cumDict


def part1answer(directorySummary):
    return sum(v for v in directorySummary.values() if v <= 100000)

def part2answer(directorySummary):
    # get minimum space needed to delete
    minimum_value = SPACENEEDED - (HDSIZE - directorySummary["/"])

    fileSizeOfNextSmallest = min(i for i in directorySummary.values() if i > minimum_value)

    return fileSizeOfNextSmallest

def main():
    filesAndDirs = buildTree()
    individualDirectorySummary = buildSummary(filesAndDirs)
    cumDirectorySummary = calculateCumTotals(individualDirectorySummary)

    if TESTING:
        print(filesAndDirs)
        print(individualDirectorySummary)
        print(cumDirectorySummary)

    print(part1answer(cumDirectorySummary))

    print(part2answer(cumDirectorySummary))






if __name__ == '__main__':
    main()