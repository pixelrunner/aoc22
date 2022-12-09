def buildPriorityList(priorityDict):
    n = 1
    for letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        priorityDict.update({letter: n})
        n += 1

    return priorityDict


def buildlist(packList, partNo):
    f = open("input.txt", "r")
    fileLine = f.readline().replace(" ","").replace("\n", "")

    if partNo == 1:
        while fileLine != "":
            n = len(fileLine)

            if n % 2 == 0:
                half1 = fileLine[0:n // 2]
                half2 = fileLine[n // 2:]
            else:
                half1 = fileLine[0:(n // 2 + 1)]
                half2 = fileLine[(n // 2 + 1):]

            packList.append([half1, half2])
            fileLine = f.readline().replace(" ", "").replace("\n", "")

    elif partNo == 2:
        while fileLine != "":
            trioPacks = []
            for x in range(3):
                trioPacks.append(fileLine)
                fileLine = f.readline().replace(" ", "").replace("\n", "")
            packList.append(trioPacks)


    return packList


def workOutDuplicate(packList, partNo):
    n = 0
    # iterate through each backpack
    for packItem in packList:

        # iterate through letters in first half and see if letter in both
        for letter in packItem[0]:
            if letter in packItem[1]:
                if partNo == 2:
                    if letter in packItem[2]:
                        # letter found - add it to the list
                        packList[n].append(letter)
                        break
                else:
                    # letter found - add it to the list
                    packList[n].append(letter)
                    break
        n += 1
    return packList


def workOutSum(priorityDict, packList, partNo):
    sum = 0
    for packItem in packList:
        if partNo == 1:
            sum += priorityDict[packItem[2]]
        elif partNo == 2:
            sum += priorityDict[packItem[3]]
    return sum


def main ():
    priorityDict = {}
    priorityDict = buildPriorityList(priorityDict)

    for partNo in range(1, 3):
        packList = []
        packList = buildlist(packList, partNo)
        packList = workOutDuplicate(packList, partNo)

        sumOfPriorities = workOutSum(priorityDict, packList, partNo)

        print(f"Part {partNo}: Sum of priorities = {sumOfPriorities}")

if __name__ == '__main__':
    main()