import csv


def student_list():
    file = open("/home/rane/ashu/carnot interview/student.csv")
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row)
    file.close()
    return rows
