def day1():
    elfNumber = 1
    calorieTotal = 0
    elfTotals = {}

    f = open("input.txt", "r")
    fileLine = f.readline()

    while fileLine:
        fileLine = fileLine.replace("/n", "").strip()
        if fileLine != '':
            calorieTotal = calorieTotal + int(fileLine)
        else:
            elfTotals.update({elfNumber: calorieTotal})
            calorieTotal = 0
            elfNumber += 1

        fileLine = f.readline()

    maxElf = max(elfTotals, key=elfTotals.get)
    print(maxElf)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day1()
