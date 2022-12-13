# build lists (1 list for each stack)
# go through instructions one line at a time
#       loop x times (x = how many you need to move)
#           take one from origin
#           add to destination
# read off top values to ge answer


def buildStacks(f):
    stacks = {}
    tempLines = []

    # store all crate lines in temporary list
    # store final line (crate numbers) in a list

    fileLine = f.readline().replace("\n", "")
    while "[" in fileLine:
        tempLines.append(fileLine)
        fileLine = f.readline().replace("\n", "")
    else:
        for box in fileLine.replace("  "," ").strip().split():
            stacks[int(box)] = []

    for line in tempLines:
        letternumber = 0
        foundCrate = False

        for letter in line:
            if letter == "]": foundCrate = False
            if foundCrate == True:
                cratenumber = int(((letternumber-1)/4)+1)
                stacks[cratenumber].insert(0, letter)

            if letter == "[": foundCrate = True


            letternumber += 1
    return stacks


def getFirstInstruction(f):
    fileLine = f.readline().replace("\n", "").strip()
    while fileLine == "":
        fileLine = f.readline().replace("\n", "").strip()
    else:
        return fileLine

def createInstructionsList(f):
    instructions = []
    fileLine = getFirstInstruction(f)
    while fileLine != "":
        instructions.append(fileLine.split())
        fileLine = f.readline().replace("\n", "").strip()
    else:
        return instructions

def moveCrates(stacks, amount, origin, destination, partNo):
    if partNo == "P1":
        for x in range(0, amount):
            crate = stacks[origin].pop()
            stacks[destination].append(crate)
    elif partNo == "P2":
        cratesMoving = []
        for x in range(0, amount):
            cratesMoving.append(stacks[origin].pop())

        for crate in cratesMoving:
            stacks[destination].append(crate)

    return stacks


def followInstructions(instructions, stacks, partNo):
    for instruction in instructions:
        if instruction[0] == "move":
            stacks = moveCrates(stacks, int(instruction[1]), int(instruction[3]), int(instruction[5]), partNo)

    return stacks


def topCrates(stacks):
    lastItems = ""
    for stack in stacks.values():

        lastItems = lastItems + stack[-1]

    return lastItems


def main():
    f = open("input.txt", "r")

    stacks = buildStacks(f)
    instructions = createInstructionsList(f)

    print(stacks)

    stacksP1 = followInstructions(instructions, stacks, "P1")
    # print(topCrates(stacksP1))

    print(stacks)

    # stacksP2 = followInstructions(instructions, stacks, "P2")
    # print(topCrates(stacksP2))




if __name__ == '__main__':
    main()