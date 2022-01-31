def main():
    infile = open("customers.csv", "r")
    outfile = open("customer_country.csv", "w")

    infile.reader()

    for reader in infile:
        outfile.write(reader[1] + "," + reader[2] + "\n")

    infile.close()
    outfile.close()


main()
