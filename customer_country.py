import csv


def main():
    infile = open("customers.csv", "r")
    outfile = open("customer_country.csv", "w")

    reader = csv.reader(infile, delimiter=",")
    next(reader)

    for rec in reader:
        outfile.write(rec[1] + "," + rec[2] + "," + rec[4] + "\n")

    outfile.close()


main()
