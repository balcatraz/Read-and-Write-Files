import csv
from typing import Counter


def main():
    infile = open("customers.csv", "r")
    outfile = open("customer_country.csv", "w")

    reader = csv.reader(infile, delimiter=",")

    count = 0
    for rec in reader:
        outfile.write(rec[1] + "," + rec[2] + "," + rec[4] + "\n")
        count += 1

    print("Number of Records:", count - 1)
    outfile.close()


main()
