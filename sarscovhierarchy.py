import csv
import random
import pandas as pd
from Bio import SeqIO
import urllib.request
import glob
import matplotlib.pyplot as plot


def main():
    print(pd.DataFrame(select_accessions()).T)  # First the program obtains the median sample for each country.
    # dictionary_with_fasta = fasta_RNA(
    # dictionary_median_accessions)   In second place, the program associates the RNA sequence with the sample.
    # createDictionary(dictionary_with_fasta)
    # distances(load_aligments(list(dictionary_with_fasta.keys())))


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
            median_countries[x] = median(countries[x]["Length"], len(countries[x]["Length"]) // 2)
        return final_median_dict(countries, median_countries)


def median(values, n):
    pivot = values[0]
    below = [x for x in values if x < pivot]
    above = [x for x in values if x > pivot]

    num_less = len(below)
    num_lessoreq = len(values) - len(above)

    if n < num_less:
        return median(below, n)
    elif n >= num_lessoreq:
        return median(above, n - num_lessoreq)
    else:
        return pivot


arr = random.sample(range(10), 10)


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
    return dictionary


def download_FASTA(accession):
    url = 'http://www.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&rettype=fasta&id=' + accession
    path = './FASTA_files/' + accession + '.fasta'
    urllib.request.urlretrieve(url, path)
    return path


def createDictionary(dictionary):
    result = dict()
    S = similarity_matrix()
    countries = list(dictionary.keys())
    for country in countries:
        result[country] = dict()
        A = dictionary[country]["RNA"]
        for country2 in countries:
            B = dictionary[country2]["RNA"]
            result[country].update({country2: maximum_score(S, A, B)})
    return result


def load_aligments(country_list):
    with open('aligment.csv', newline='') as csvfile:
        data = csv.DictReader(csvfile, delimiter=",")
        result = dict()
        i = 0
        for row in data:
            result[country_list[i]] = dict()
            for country2 in country_list:
                result[country_list[i]].update({country2: row[country2]})
            i += 1
    return result


def similarity_matrix():
    matrix = dict()
    for i in ["A", "G", "C", "T"]:
        matrix[i] = dict()

    matrix["A"].update({"A": 10})
    matrix["A"].update({"G": -1})
    matrix["A"].update({"C": -3})
    matrix["A"].update({"T": -4})
    matrix["G"].update({"A": -1})
    matrix["G"].update({"G": 7})
    matrix["G"].update({"C": -5})
    matrix["G"].update({"T": -3})
    matrix["C"].update({"A": -3})
    matrix["C"].update({"G": -5})
    matrix["C"].update({"C": 9})
    matrix["C"].update({"T": 0})
    matrix["T"].update({"A": -4})
    matrix["T"].update({"G": -3})
    matrix["T"].update({"C": 0})
    matrix["T"].update({"T": 8})
    return matrix


def maximum_score(S, A, B):
    d = -5
    F = [[0 for x in range(len(A) + 1)] for y in range(len(B) + 1)]
    for i in range(len(B) + 1):
        F[i][0] = i * d
    for j in range(len(A) + 1):
        F[0][j] = j * d
    for i in range(1, (len(B) + 1)):
        for j in range(1, (len(A) + 1)):
            if A[j - 1] == "N" and B[j - 1] == "N":
                match = F[i - 1][j - 1] + S[random.choice(list(S.keys()))][random.choice(list(S.keys()))]
            elif A[j - 1] == "N":
                match = F[i - 1][j - 1] + S[random.choice(list(S.keys()))][B[i - 1]]
            elif B[i - 1] == "N":
                match = F[i - 1][j - 1] + S[A[j - 1]][random.choice(list(S.keys()))]
            elif A[j - 1] == "K" and B[j - 1] == "K":
                match = F[i - 1][j - 1] + S[random.choice(["G", "C"])][random.choice(["G", "C"])]
            elif A[j - 1] == "K":
                match = F[i - 1][j - 1] + S[random.choice(["G", "C"])][B[i - 1]]
            elif B[i - 1] == "K":
                match = F[i - 1][j - 1] + S[A[j - 1]][random.choice(["G", "C"])]
            else:
                match = F[i - 1][j - 1] + S[A[j - 1]][B[i - 1]]
            delete = F[i - 1][j] + d
            insert = F[i][j - 1] + d
            F[i][j] = max(delete, insert, match)
    return F[-1][-1]


def distances(dictionary):
    result = dict()
    for i in list(dictionary.keys()):
        result[i] = dict()
        valor = dictionary[i][i]
        for j in list(dictionary.keys()):
            result[i].update({j: abs(int(valor) - int(dictionary[i][j]))})
    pd.DataFrame(result).to_csv('out.csv', index=False)


main()
