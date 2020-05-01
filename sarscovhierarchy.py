import csv
import pandas as pd


def main():
    with open('sequences.csv', newline='') as csvfile:
        data = csv.DictReader(csvfile, delimiter=";")
        first_row = next(data)
        location = first_row["Geo_Location"]
        countries = dict()
        countries[location] = dict()
        list_len = list()
        list_len.append(int(first_row["Length"]))
        list_accession = list()
        list_accession.append(str(first_row["Accession"]))

        countries[location].update({"Accession": list_accession})
        countries[location].update({"Length": list_len})

        for row in data:
            if location in row["Geo_Location"]:
                list_len.append(int(row["Length"]))
                list_accession.append(str(row["Accession"]))

                countries[location].update({"Accession": list_accession})
                countries[location].update({"Length": list_len})
            else:
                location = row["Geo_Location"]

                countries[location] = dict()
                list_len = list()
                list_len.append(int(row["Length"]))
                list_accession = list()
                list_accession.append(str(row["Accession"]))

                countries[location].update({"Accession": list_accession})
                countries[location].update({"Length": list_len})

        median_countries = dict()
        for x in list(countries.keys()):
            median_countries[x] = median(sorted(countries[x]["Length"]))
        final_median_dict(countries, median_countries)


def median(l):
    if len(l) % 2 == 0:
        n = len(l)
        mediana = (l[n // 2 - 1] + l[n // 2]) // 2
        if l[n // 2] - mediana < mediana - l[n // 2 - 1]:
            return l[n // 2]
        else:
            return l[n // 2 - 1]
    else:
        return l[len(l) // 2]


def final_median_dict(countries, median_countries):
    result = dict()
    for x in list(countries.keys()):
        medianIn = countries[x]["Length"].index(median_countries[x])
        result[x] = countries[x]["Accession"][medianIn]
    print(result)


main()
