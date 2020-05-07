import csv
import random
import pandas as pd
from Bio import SeqIO
import urllib.request
import glob


def main():
    dictionary_median_accessions = select_accessions()  # First the program obtains the median sample for each country.
    fasta_RNA(dictionary_median_accessions)  # In second place, the program associates the RNA sequence with the sample.
    # createDictionary(dictionary_median_accessions)


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


def median(values):
    values = sort(values)
    return values[len(values) // 2]


def sort(values):
    less = []
    equal = []
    greater = []

    if len(values) > 1:
        pivot = random.choice(values)
        for x in values:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sort(less) + equal + sort(greater)
    else:
        return values


# This function, once we get the median value of each country, it creates a dictionary that contains all the medians'
# Accessions related with their country.


def final_median_dict(countries, median_countries):
    result = dict()
    for x in list(countries.keys()):
        medianIn = countries[x]["Length"].index(median_countries[x])
        result[x] = dict()
        result[x].update({"Accession": countries[x]["Accession"][medianIn]})
    return result


def fasta_RNA(dictionary):
    for country in list(dictionary.keys()):
        path = glob.glob("./FASTA_files/" + dictionary[country]["Accession"] + ".fasta", recursive=False)
        if not path:
            path = download_FASTA(dictionary[country]["Accession"])
        else:
            path = str(path[0])
        for file in SeqIO.parse(path, "fasta"):
            dictionary[country].update({"RNA": str(file.seq)[0:1000]})
    print(pd.DataFrame(dictionary).T)


def download_FASTA(accession):
    url = 'http://www.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&rettype=fasta&id=' + accession
    path = './FASTA_files/' + accession + '.fasta'
    urllib.request.urlretrieve(url, path)
    return path


def createDictionary(dictionary):
    result = dict()
    countries = list(dictionary.keys())
    for country in countries:
        result[country] = dict()
        for country2 in countries:
            result[country].update({country2: ""})
    print(pd.DataFrame(result).T)


main()
