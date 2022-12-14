# {directory_path: [[file, size],[file, size], [file, size]],
#  directory_path: [[file, size],[file, size]]}


def main():
    filesAndDirs = {}
    currentPath = ""
    f = open("input.txt", "r")
    cliLine = f.readline().strip().split()

    while cliLine != "":
        if cliLine[1] == "cd" and cliLine[2] != "..":
            currentPath = currentPath & cliLine[2]
            filesAndDirs[currentPath] = []
        elif cliLine[0].isalnum():
            filesAndDirs[currentPath].append([cliLine[1], cliLine[0]])
        elif cliLine[1] == "cd" and cliLine[2] == "..":
            currentPath = currentPath.rsplit("/", 1)[0]

        cliLine = f.readline().strip().split()

    print(filesAndDirs)

if __name__ == '__main__':
    main()