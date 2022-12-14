def findUnique(noOfUniqueNeeded):
    f = open("input.txt", "r")
    input = f.readline()

    index = 0
    lastRepeat = 0

    for letter in input:
        # if index less than no. needed then only go back to zero
        # if repeat_found and if it is higher than previous repeat_found, then update repeat_found

        # if index > no. needed then go back no needed and update repeat_found
        # if no repeat found then we're done!

        if index < noOfUniqueNeeded:
            # less than no_needed so only go back to start of input
            backTo = -1
        elif index >= noOfUniqueNeeded:
            backTo = index-noOfUniqueNeeded

        for x in range(index, backTo, -1):
            if index != x and lastRepeat < x:
                # if matched then update lastRepeat found
                if letter == input[x]:
                    # print(f"last repeat: {lastRepeat}. Current index: {index}. Latest run: {index - lastRepeat}")
                    if lastRepeat < x: lastRepeat = x

        # if lastRepeat > no._needed then we're done!
        if (index - lastRepeat) >= noOfUniqueNeeded:
            return index + 1

        index += 1


def main():
    part1 = findUnique(4)
    part2 = findUnique(14)

    print(part1)
    print(part2)


if __name__ == '__main__':
    main()
