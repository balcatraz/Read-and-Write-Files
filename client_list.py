def main():

    infile = open("clients.txt", "r")
    lineNum = 0

    for line in infile:
        lineNum += 1
        print(str(lineNum) + ". " + line.rstrip())

    infile.close()


main()
