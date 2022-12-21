from math import sqrt


def walk_the_snake(puzzle: list, rope_size: int) -> int:
    snake = [(0, 0)] * rope_size
    dir_map = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
    tail_visited = set()
    tail_visited.add(snake[0])

    for command in puzzle:
        snake[-1] = (
            snake[-1][0] + command[1] * dir_map[command[0]][0], snake[-1][1] + command[1] * dir_map[command[0]][1])
        anything_moved = True
        while anything_moved:
            anything_moved = False
            for i in range(len(snake) - 1, 0, -1):
                head = snake[i]
                tail = snake[i - 1]
                dist_from_tail = sqrt((head[0] - tail[0]) ** 2 + (head[1] - tail[1]) ** 2)
                if dist_from_tail < 2.0: break
                # tail takes one step towards head
                tail = (tail[0] + just_one_step(head[0], tail[0]), tail[1] + just_one_step(head[1], tail[1]))
                anything_moved = True
                snake[i - 1] = tail
            tail_visited.add(snake[0])

    return len(tail_visited)


def code_gen(data: list):
    for l in data:
        t = l.split()
        yield t[0], int(t[1])


def just_one_step(a, b) -> int:
    return 0 if a == b else int(abs(a - b) / (a - b))


def cheating():
    with open(r"input.txt") as f:
        puzzle = [command for command in code_gen(f.read().splitlines())]

    print("Part 1: {}".format(walk_the_snake(puzzle, 2)))
    print("Part 2: {}".format(walk_the_snake(puzzle, 10)))

# ===========================================

DEBUG = False

if DEBUG:
    ARRAYSIZE = 400
else:
    ARRAYSIZE = 400

# START_POS = [int((ARRAYSIZE-1)/2), int((ARRAYSIZE-1)/2)]
# START_POS = [(ARRAYSIZE-1), 0]
START_POS = [99, 99]


def setup_array():
    empty_array = []
    for i in range(0, ARRAYSIZE):
        empty_array.append([])

    for row in empty_array:
        for x in range(0, ARRAYSIZE):
            row.append(".")

    return empty_array


def check_and_move_tail(head_loc, tail_loc, main_array):
    '''
      A B C
    D E F G H
    I J * K L
    M N O P Q
      U R S
    '''

    # if adjacent (F, J, K, O, or *) then do nothing
    if tail_loc in ([head_loc[0] - 1, head_loc[1]],[head_loc[0], head_loc[1] - 1],[head_loc[0] + 1, head_loc[1]],[head_loc[0], head_loc[1] + 1],head_loc):
        pass

    # if in B, L, R, or I then move 1 space towards head_loc
    elif tail_loc in ([head_loc[0] - 2, head_loc[1]],[head_loc[0], head_loc[1] - 2],[head_loc[0] + 2, head_loc[1]],[head_loc[0], head_loc[1] + 2]):
        # if I or L
        if head_loc[0] == tail_loc[0]:
            # if I
            if tail_loc[1] == (head_loc[1] - 2):
                tail_loc[1] = (head_loc[1] - 1)
            # else if L
            elif tail_loc[1] == (head_loc[1] + 2):
                tail_loc[1] = (head_loc[1] + 1)

        # if B or R
        if head_loc[1] == tail_loc[1]:
            # if B
            if tail_loc[0] == (head_loc[0] - 2):
                tail_loc[0] = (head_loc[0] - 1)
            # else if R
            elif tail_loc[0] == (head_loc[0] + 2):
                tail_loc[0] = (head_loc[0] + 1)

    # if in A, C, D, H, M, Q, U or S then move diagnally towards head_loc
    else:
        # if A or C then move to F
        if tail_loc[0] == (head_loc[0] - 2):
            tail_loc = [head_loc[0] - 1, head_loc[1]]

        # if D or M then move to J
        if tail_loc[1] == (head_loc[1] - 2):
            tail_loc = [head_loc[0], head_loc[1] - 1]

        # if H or Q  then move to K
        if tail_loc[1] == (head_loc[1] + 2):
            tail_loc = [head_loc[0], head_loc[1] + 1]

        # if U or S then move to O
        if tail_loc[0] == (head_loc[0] + 2):
            tail_loc = [head_loc[0] + 1, head_loc[1]]

    return tail_loc


def follow_instructions(main_array, part_no):
    head_loc = [START_POS[0], START_POS[1]]
    tail_loc = [START_POS[0], START_POS[1]]
    if part_no == 2:
        knot1 = [START_POS[0], START_POS[1]]
        knot2 = [START_POS[0], START_POS[1]]
        knot3 = [START_POS[0], START_POS[1]]
        knot4 = [START_POS[0], START_POS[1]]
        knot5 = [START_POS[0], START_POS[1]]
        knot6 = [START_POS[0], START_POS[1]]
        knot7 = [START_POS[0], START_POS[1]]
        knot8 = [START_POS[0], START_POS[1]]

    main_array[tail_loc[0]][tail_loc[1]] = "#"

    '''
    if DEBUG:
        f = open("sample_input.txt", "r")
    else:'''
    f = open("input.txt", "r")

    instruction = f.readline().replace("/n", "").strip().split()

    while instruction != []:
        if DEBUG: print(instruction)
        for x in range(0,int(instruction[1])):
            match instruction[0]:
                case "R":
                    head_loc = [head_loc[0], head_loc[1] + 1]
                case "U":
                    head_loc = [head_loc[0] - 1, head_loc[1]]
                case "L":
                    head_loc = [head_loc[0], head_loc[1] - 1]
                case "D":
                    head_loc = [head_loc[0] + 1, head_loc[1]]

            if DEBUG: print(f"Head: {head_loc}")
            if part_no == 1:
                tail_loc = check_and_move_tail(head_loc, tail_loc, main_array)
            if part_no == 2:
                knot1 = check_and_move_tail(head_loc, knot1, main_array)
                knot2 = check_and_move_tail(knot1, knot2, main_array)
                knot3 = check_and_move_tail(knot2, knot3, main_array)
                knot4 = check_and_move_tail(knot3, knot4, main_array)
                knot5 = check_and_move_tail(knot4, knot5, main_array)
                knot6 = check_and_move_tail(knot5, knot6, main_array)
                knot7 = check_and_move_tail(knot6, knot7, main_array)
                knot8 = check_and_move_tail(knot7, knot8, main_array)
                tail_loc = check_and_move_tail(knot8, tail_loc, main_array)


            if DEBUG: print(f"Tail: {tail_loc}")

            main_array[tail_loc[0]][tail_loc[1]] = "#"
        instruction = f.readline().replace("/n", "").strip().split()

    return main_array

def count_hashes(main_array):
    counter = 0
    for row in main_array:
        for spot in row:
            if spot == "#":
                counter += 1

    return counter


def main():
    main_array = setup_array()
    if DEBUG: print(main_array)

    main_array = follow_instructions(main_array, 1)
    if DEBUG: print(main_array)
    part_1_ans = count_hashes(main_array)
    print(part_1_ans)

    main_array = setup_array()
    main_array = follow_instructions(main_array, 2)
    part_2_ans = count_hashes(main_array)
    print(part_2_ans)

if __name__ == '__main__':
    main()
    cheating()

