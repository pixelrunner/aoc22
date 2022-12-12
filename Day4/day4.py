
def isContained(fileLine):
    bothElves = fileLine.split(",")
    elf1 = bothElves[0].split("-")
    elf2 = bothElves[1].split("-")

    if int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]): return True
    if int(elf2[0]) >= int(elf1[0]) and int(elf2[1]) <= int(elf1[1]): return True

    return False

def isOverlapping(fileLine):
    bothElves = fileLine.split(",")
    elf1 = bothElves[0].split("-")
    elf2 = bothElves[1].split("-")

    if int(elf1[0]) <= int(elf2[1]) and int(elf1[1]) >= int(elf2[0]): return True
    if int(elf2[0]) <= int(elf1[1]) and int(elf2[1]) >= int(elf1[0]): return True

    return False

def main():
    f = open("input.txt", "r")
    fileLine = f.readline().replace(" ","").replace("\n", "")
    p1CumulativeTotal = 0
    p2CumulativeTotal = 0

    while fileLine != "":
        if isContained(fileLine):
            p1CumulativeTotal += 1

        if isOverlapping(fileLine):
            p2CumulativeTotal += 1

        fileLine = f.readline().replace(" ", "").replace("\n", "")

    print(f"Total number of elf pairs where one contains the other: {p1CumulativeTotal}")
    print(f"Total number of overlapping elf pairs: {p2CumulativeTotal}")

if __name__ == '__main__':
    main()