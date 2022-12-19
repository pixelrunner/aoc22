# create tuple of tuple of all trees
'''
eg.
((3,0,3,7,3),
(2,5,5,1,2),
(6,5,3,3,2),
(3,3,5,4,9),
(3,5,3,9,0))
'''
# start at (1(1)) - second row, second tree
# four for loops that look in each direction for each tree
# as soon as a tree is found to be visible skip the other for loops and add one to the tree count

# CONSTANTS
DEBUG = False

def createTreeArray():
    if DEBUG:
        f = open("sample_input.txt", "r")
    else:
        f = open("input.txt", "r")

    treeArray = []
    treeLine = tuple([int(x) for x in f.readline().replace("/n", "").strip()])

    while treeLine != ():
        treeArray.append(treeLine)
        treeLine = tuple([int(x) for x in f.readline().replace("/n", "").strip()])

    return tuple(treeArray)


def countVisibleTrees(treeArray, partNo):
    rowNumber = 0
    count = 0
    if partNo == 1:
        for row in treeArray:
            if rowNumber == 0 or rowNumber == (len(treeArray) - 1):
                # automatically count the top and bottom trees
                for tree in row:
                    count += 1
            else:
                columnNumber = 0
                for tree in row:
                    if columnNumber == 0 or columnNumber == (len(row) - 1):
                        # automatically count the trees on the sides
                        count += 1
                    elif checkVisible(rowNumber, columnNumber, treeArray):
                        count += 1
                    columnNumber += 1
            rowNumber += 1

        return count
    elif partNo == 2:
        currentHighest = 0
        for row in treeArray:
            columnNumber = 0
            for tree in row:
                treesVisibleScore = checkTreesVisibleScore(rowNumber, columnNumber, treeArray)
                if treesVisibleScore > currentHighest: currentHighest = treesVisibleScore
                columnNumber += 1
            rowNumber += 1

        return currentHighest

def checkVisible(rowNumber, columnNumber, treeArray):
    visibleSeen = False
    origTreeHeight = treeArray[rowNumber][columnNumber]
    arrayWidth = len(treeArray[0])
    arrayHeight = len(treeArray)

    # check North
    # -1 on row number until 0 (including 0)
    if not visibleSeen:
        for newRow in range(rowNumber - 1, -1, -1):
            if treeArray[newRow][columnNumber] >= origTreeHeight:
                break
            if newRow == 0:
                visibleSeen = True
    # check East
    # +1 on column number to length of list (including final one)
    if not visibleSeen:
        for newCol in range(columnNumber + 1, arrayWidth):
            if treeArray[rowNumber][newCol] >= origTreeHeight:
                break
            if newCol + 1 == arrayWidth:
                visibleSeen = True

    # check South
    # +1 on row number until length of list (including final one)
    if not visibleSeen:
        for newRow in range(rowNumber + 1, arrayHeight):
            if treeArray[newRow][columnNumber] >= origTreeHeight:
                break
            if newRow + 1 == arrayHeight:
                visibleSeen = True

    # check West
    # -1 on column number until 0 (including 0)
    if not visibleSeen:
        for newCol in range(columnNumber - 1, -1, -1):
            if treeArray[rowNumber][newCol] >= origTreeHeight:
                break
            if newCol == 0:
                visibleSeen = True

    return visibleSeen


def checkTreesVisibleScore(rowNumber, columnNumber, treeArray):
    origTreeHeight = treeArray[rowNumber][columnNumber]
    arrayWidth = len(treeArray[0])
    arrayHeight = len(treeArray)

    northTrees = 0
    eastTrees = 0
    southTrees = 0
    westTrees = 0

    # check north
    # if at the top of the array then northTrees = 0
    # else go up each row counting how many trees you can see
    if rowNumber == 0:
        northTrees = 0
    else:
        for newRow in range(rowNumber - 1, -1, -1):
            if treeArray[newRow][columnNumber] < origTreeHeight:
                northTrees += 1
            elif treeArray[newRow][columnNumber] >= origTreeHeight:
                northTrees += 1
                break

    # check east
    # if at the right side of the array then eastTrees = 0
    # else go up each column counting how many trees you can see
    if columnNumber == (len(treeArray[0]) - 1):
        eastTrees = 0
    else:
        for newCol in range(columnNumber + 1, arrayWidth):
            if treeArray[rowNumber][newCol] < origTreeHeight:
                eastTrees += 1
            elif treeArray[rowNumber][newCol] >= origTreeHeight:
                eastTrees += 1
                break

    # check south
    # if at the bottom of the array then southTrees = 0
    # else go down each row counting how many trees you can see
    if rowNumber == (len(treeArray) - 1):
        southTrees = 0
    else:
        for newRow in range(rowNumber + 1, arrayHeight):
            if treeArray[newRow][columnNumber] < origTreeHeight:
                southTrees += 1
            elif treeArray[newRow][columnNumber] >= origTreeHeight:
                southTrees += 1
                break

    # check west
    # if at the left side of the array then westTrees = 0
    # else go down each column counting how many trees you can see
    if columnNumber == 0:
        westTrees = 0
    else:
        for newCol in range(columnNumber - 1, -1, -1):
            if treeArray[rowNumber][newCol] < origTreeHeight:
                westTrees += 1
            elif treeArray[rowNumber][newCol] >= origTreeHeight:
                westTrees += 1
                break

    score = northTrees * eastTrees * southTrees * westTrees
    return score


def main():
    treeArray = createTreeArray()
    print(treeArray)
    part1 = countVisibleTrees(treeArray, 1)
    print (part1)
    part2 = countVisibleTrees(treeArray, 2)
    print(part2)


if __name__ == '__main__':
    main()