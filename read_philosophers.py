from unicodedata import name


def main():
    infile = open("philosophers.txt", "r")

    name = infile.readline().rstrip()
    print(name)
    name = infile.readline().rstrip()
    print(name)
    name = infile.readline().rstrip()
    print(name)

    infile.close()


main()
