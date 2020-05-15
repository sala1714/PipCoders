import csv
import random
import pandas as pd
from Bio import SeqIO
import urllib.request
import glob
import needleman_wunsch as nw

def fasta_RNA(dictionary):
    for country in list(dictionary.keys()):
        path = glob.glob("./data/FASTA_files/" + dictionary[country]["Accession"] + ".fasta", recursive=False)
        if not path:
            path = download_FASTA(dictionary[country]["Accession"])
        else:
            path = str(path[0])
        for file in SeqIO.parse(path, "fasta"):
            dictionary[country].update({"RNA": str(file.seq)[0:1000]})
    return dictionary


def download_FASTA(accession):
    url = 'http://www.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&rettype=fasta&id=' + accession
    path = './data/FASTA_files/' + accession + '.fasta'
    urllib.request.urlretrieve(url, path)
    return path


def createDictionary(dictionary):
    result = dict()
    countries = list(dictionary.keys())
    for country in countries:
        result[country] = dict()
        A = dictionary[country]["RNA"]
        for country2 in countries:
            B = dictionary[country2]["RNA"]
            print(country)
            print(country2)
            result[country].update({country2: nw.maximum_score(A, B)})
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


def maximum_score(A, B):
    d = -1
    F = [[0 for x in range(len(A) + 1)] for y in range(len(B) + 1)]
    for i in range(len(B) + 1):
        F[i][0] = i * d
    for j in range(len(A) + 1):
        F[0][j] = j * d
    for i in range(1, (len(B) + 1)):
        for j in range(1, (len(A) + 1)):
            a_char = A[j - 1]
            if a_char == "N":
                a_char = "A"
            if a_char == "K":
                a_char = "G"
            b_char = B[i - 1]
            if b_char == "N":
                b_char = "A"
            if b_char == "K":
                b_char = "G"
            if a_char == b_char:
                match = F[i - 1][j - 1] + 1
            else:
                match = F[i - 1][j - 1] - 1
            delete = F[i - 1][j] + d
            insert = F[i][j - 1] + d
            F[i][j] = max(delete, insert, match)
    return F[-1][-1]


# Debido al tiempo que se tarda en comparar dos secuencias fasta, esta función se utiliza para cargar un csv con los resultados de una ejecución anterior.

def load_aligments(country_list):
    with open('data/aligment.csv', newline='') as csvfile:
        data = csv.DictReader(csvfile, delimiter=",")
        result = dict()
        i = 0
        for row in data:
            result[country_list[i]] = dict()
            for country2 in country_list:
                result[country_list[i]].update({country2: row[country2]})
            i += 1
    return result


# Devuelve un diccionario con el valor de la distancia de todos los paises con respecto a la muestra del pais

def distances(dictionary):
    result = dict()
    for i in list(dictionary.keys()):
        result[i] = dict()
    for i in list(dictionary.keys()):
        valor = dictionary[i][i]
        lista = list(dictionary.keys())
        for j in lista[lista.index(i):]:
            result[i].update({j: int(valor) - int(dictionary[i][j])})
            result[j].update({i: int(valor) - int(dictionary[j][i])})

    pd.DataFrame(result).to_csv('data/out.csv', index=False)
