def getPlayedHands (f):
    fileLine = f.readline()
    hands = fileLine.replace(" ", "")

    if hands == "":
        return "", "", ""

    if hands[0] == "A":
        competitor = "R"
    elif hands[0] == "B":
        competitor = "P"
    elif hands[0] == "C":
        competitor = "S"

    if hands[1] == "X":
        p1OwnHand = "R"
        p2DesiredOutcome = -1
    elif hands[1] == "Y":
        p1OwnHand = "P"
        p2DesiredOutcome = 0
    elif hands[1] == "Z":
        p1OwnHand = "S"
        p2DesiredOutcome = 1

    return competitor, p1OwnHand, p2DesiredOutcome

def getOutcome(competitor, ownhand):
    if competitor == "R":
        if ownhand == "R":
            return 0
        elif ownhand == "P":
            return 1
        elif ownhand == "S":
            return -1
    elif competitor == "P":
        if ownhand == "R":
            return -1
        elif ownhand == "P":
            return 0
        elif ownhand == "S":
            return 1
    elif competitor == "S":
        if ownhand == "R":
            return 1
        elif ownhand == "P":
            return -1
        elif ownhand == "S":
            return 0

def getHand(competitor, p2DesiredOutcome):
    if competitor == "R":
        if p2DesiredOutcome == -1:
            return "S"
        elif p2DesiredOutcome == 0:
            return "R"
        elif p2DesiredOutcome == 1:
            return "P"
    elif competitor == "P":
        if p2DesiredOutcome == -1:
            return "R"
        elif p2DesiredOutcome == 0:
            return "P"
        elif p2DesiredOutcome == 1:
            return "S"
    elif competitor == "S":
        if p2DesiredOutcome == -1:
            return "P"
        elif p2DesiredOutcome == 0:
            return "S"
        elif p2DesiredOutcome == 1:
            return "R"

def roundPoints(outcome, played):
    pointsWin = 6
    pointsDraw = 3
    pointsLoss = 0
    pointsRock = 1
    pointsPaper = 2
    pointsScissors = 3

    if outcome == 1:
        points = pointsWin
    elif outcome == 0:
        points = pointsDraw
    elif outcome == -1:
        points = pointsLoss

    if played == "R":
        points += pointsRock
    elif played == "P":
        points += pointsPaper
    elif played == "S":
        points += pointsScissors

    return points

def day2():
    p1TotalPoints = 0
    p2TotalPoints = 0
    f = open("input.txt", "r")
    competitor, p1OwnHand, p2DesiredOutcome = getPlayedHands(f)
    while competitor != "":
        p1Outcome = getOutcome(competitor, p1OwnHand)
        p1TotalPoints += roundPoints(p1Outcome,p1OwnHand)
        p2OwnHand = getHand(competitor, p2DesiredOutcome)
        p2TotalPoints += roundPoints(p2DesiredOutcome, p2OwnHand)

        # get next hands from file
        competitor, p1OwnHand, p2DesiredOutcome = getPlayedHands(f)

    print(p1TotalPoints)
    print(p2TotalPoints)
if __name__ == '__main__':
    day2()