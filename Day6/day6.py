def main():
    f = open("input.txt", "r")
    input = f.readline()

    index = 0
    for letter in input:
        if index >= 3:
            if letter != input[index - 1] and letter != input[index - 2] and letter != input[index - 3]:
                print(index)
                break
        index += 1


if __name__ == '__main__':
    main()
