import csv
import pandas as pd
def main():
    with open('sequences.csv', newline='') as csvfile:
        data = csv.DictReader(csvfile, delimiter=";")
        first_row = next(data)
        location = first_row["Geo_Location"]
        countries = {}
        countries[location] = list()
        countries[location].append(int(first_row["Length"]))
        for row in data:
            if location in row["Geo_Location"]:
                countries[location].append(int(row["Length"]))
            else:
                location = row["Geo_Location"]
                countries[location] = list()
                countries[location].append(int(row["Length"]))
        median_countries = {}
        for x in list(countries.keys()):
            median_countries[x] = median(sorted(countries[x]))
def median(l):
    if len(l) % 2 == 0:
        n = len(l)
        mediana = (l[n // 2 - 1] + l[n // 2]) // 2
        if l[n//2]-mediana < mediana-l[n//2-1]:
            return l[n//2]
        else:
            return l[n//2-1]
    else:
        return l[len(l) // 2]
main()