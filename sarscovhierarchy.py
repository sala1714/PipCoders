import csv
with open('sequences.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile, delimiter=";")
    for row in data:
        print(row)