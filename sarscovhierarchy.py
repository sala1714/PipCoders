import csv
import random
import pandas as pd
from Bio import SeqIO


def main():
    dictionary_median_accessions = select_accessions() #First the program obtains the median sample for each country.
    fasta_RNA(dictionary_median_accessions) #In second place, the program associates the RNA sequence with the sample.


'''def muestras(dict):
    for country in list(dict.keys()):
        print(dict[country]["Accession"])'''

def fasta_RNA(dict):
    for sequence in SeqIO.parse("sequences.fasta", "fasta"):
        dict[country_of(sequence.id, dict)].update({"RNA": str(sequence.seq)[0:1000]})
    print(pd.DataFrame(dict).T)


def select_accessions():
    with open('sequences.csv', newline='') as csvfile:
        data = csv.DictReader(csvfile, delimiter=",")
        row = next(data)
        countries = dict()
        countries[row["Geo_Location"]] = dict()
        countries[row["Geo_Location"]]["Length"] = [int(row["Length"])]
        countries[row["Geo_Location"]]["Accession"] = [str(row["Accession"])]

        for row in data:
            location = row["Geo_Location"].split(":")[0]
            if location in list(countries.keys()):
                countries[location]["Accession"].append(str(row["Accession"]))
                countries[location]["Length"].append(int(row["Length"]))
            else:
                countries[location] = dict()
                countries[location]["Length"] = [int(row["Length"])]
                countries[location]["Accession"] = [str(row["Accession"])]

        median_countries = dict()
        for x in list(countries.keys()):
            median_countries[x] = median(countries[x]["Length"])
        return final_median_dict(countries, median_countries)

def median(list):
    list = sort(list)
    return list[len(list) // 2]


def sort(list):
    less = []
    equal = []
    greater = []

    if len(list) > 1:
        pivot = random.choice(list)
        for x in list:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sort(less) + equal + sort(greater)
    else:
        return list


# This function, once we get the median value of each country, it creates a dictionary that contains all the medians'
# Accessions related with their country.


def final_median_dict(countries, median_countries):
    result = dict()
    for x in list(countries.keys()):
        medianIn = countries[x]["Length"].index(median_countries[x])
        result[x] = dict()
        result[x].update({"Accession": countries[x]["Accession"][medianIn]})
    return result


def country_of(accession, dictionary):
    for country in list(dictionary.keys()):
        if accession in dictionary[country]["Accession"]:
            return country


main()
