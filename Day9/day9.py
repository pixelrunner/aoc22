DEBUG = True

if DEBUG:
    ARRAYSIZE = 5
else:
    ARRAYSIZE = 99

START_POS = [0, 0]


def setup_array():
    empty_array = []
    for i in range(0, ARRAYSIZE):
        empty_array.append([])

    for row in empty_array:
        for x in range(0, ARRAYSIZE):
            row.append(".")

    return empty_array


def follow_instructions(main_array):

    head_loc = [START_POS[0]], [START_POS[1]]
    tail_loc = [START_POS[0]], [START_POS[1]]

    main_array[tail_loc[0]][tail_loc[1]] = "#"

    if DEBUG:
        f = open("sample_input.txt", "r")
    else:
        f = open("input.txt", "r")

    instruction = f.readline().replace("/n", "").strip().split()

    for x in range(0,int(instruction[1])):



def main():
    main_array = setup_array()
    if DEBUG: print(main_array)

    follow_instructions(main_array)



if __name__ == '__main__':
    main()
