import csv


def main():
    infile = open("EmployeePay.csv", "r")

    record = csv.reader(infile, delimiter=",")
    next(record)

    for rec in record:
        print("First Name:  ", rec[1])
        print("Last Name:   ", rec[2])
        print("Salary:      ", "${:,.2f}".format(float(rec[3])))
        print("Bonus:       ", rec[4])
        totalpay = float(rec[3]) + (float(rec[3]) * float(rec[4]))
        print("Total Pay:   ", "${:,.2f}".format(totalpay))
        print()


main()
