import csv

DELIM = ','

def main():
    infile = open('student_scores.csv', 'r')
    outfile = open('student_avg.csv', 'w')

    record = csv.reader(infile, delimiter=DELIM)

    for rec in record:
        average = (float(rec[1]) + float(rec[2]) + float(rec[3]))/3.0
        outfile.write(rec[0] + DELIM + str(round(average,2)) + '\n')

    outfile.close()

main()
