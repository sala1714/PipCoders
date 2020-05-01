import csv
import pandas as pd


def main():
    with open('sequences_desordenado.csv', newline='') as csvfile:
        data = csv.DictReader(csvfile, delimiter=",")
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
            pais = row["Geo_Location"].split(":")[0]
            if pais in list(countries.keys()):
                countries[pais]["Accession"].append(str(row["Accession"]))
                countries[pais]["Length"].append(int(row["Length"]))
            else:
                countries[pais] = dict()
                list_len = list()
                list_len.append(int(row["Length"]))
                list_accession = list()
                list_accession.append(str(row["Accession"]))

                countries[pais].update({"Accession": list_accession})
                countries[pais].update({"Length": list_len})

        median_countries = dict()
        for x in list(countries.keys()):
            median_countries[x] = median(sorted(countries[x]["Length"]))
        final_median_dict(countries, median_countries)


def median(l):
    return l[len(l) // 2]


def final_median_dict(countries, median_countries):
    result = dict()
    for x in list(countries.keys()):
        medianIn = countries[x]["Length"].index(median_countries[x])
        result[x] = dict()
        result[x].update({"Accession": countries[x]["Accession"][medianIn]})
    print(pd.DataFrame(result).T)


main()
