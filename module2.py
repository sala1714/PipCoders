"""
    csv: Biblioteca usada para la carga de datos desde archivos csv.
    urllib: Biblioteca usada para descargar los archivos FASTA desde la web.
    glob: Biblioteca usada para listar el directorio de archivos FASTA.
    Bio: Biblioteca usada para localizar el RNA de la muestra dentro de un archivo FASTA.
    needleman_wunsch: El algoritmo para calcular los aligment en lenguajes RUST.
"""
import csv
import urllib.request
import glob
from Bio import SeqIO
import needleman_wunsch as nw


def fasta_rna(dictionary):
    """
        Rellena un diccionario con la muestra FASTA asociada a cada país.

        :param dictionary: Diccionario que contiene los paises a rellenar con su muestra FASTA.
        :type dictionary: dict
        :return: Devuelve un diccionario que contiene los paises con sus muestras FASTA.
    """
    for country in list(dictionary.keys()):
        path = glob.glob("./data/FASTA_files/" + dictionary[country]["Accession"] + ".fasta", recursive=False)
        if not path:
            path = download_fasta(dictionary[country]["Accession"])
        else:
            path = str(path[0])
        for file in SeqIO.parse(path, "fasta"):
            dictionary[country].update({"RNA": str(file.seq)})
    return dictionary


def download_fasta(accession):
    """
        Descarga una muestra fasta desde la web del ncbi.

        :param accession: Identificador Accession.
        :type accession: str
        :return: Devuelve la ruta donde se ha almacenado el archivo FASTA que contiene la muestra.
    """
    url = 'http://www.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&rettype=fasta&id=' + accession
    path = './data/FASTA_files/' + accession + '.fasta'
    urllib.request.urlretrieve(url, path)
    return path


def create_dictionary(dictionary):
    """
        Crea un diccionario con los datos de aligmentes desde un diccionario que contiene los FASTA.

        :param dictionary: Diccionario que contiene las muestras fasta.
        :type dictionary: dict
        :return: Diccionario que contiene los datos de aligment.
    """
    result = dict()
    countries = list(dictionary.keys())
    for country in countries:
        result[country] = dict()
    for country in countries:
        country_a = dictionary[country]["RNA"]
        for country2 in countries[countries.index(country):]:
            country_b = dictionary[country2]["RNA"]
            if country != country2:
                score = nw.maximum_score(country_a, country_b)
                result[country].update({country2: score})
                result[country2].update({country: score})

            else:
                result[country].update({country2: len(country_a)})
    return result


def load_alignments(country_list):
    """
        Crea un diccionario con los datos de alignments desde un csv.

        :param country_list: Lista de países presentes en el diccionario result.
        :type country_list: list
        :return: Diccionario con las datos del csv.
    """
    with open('data/alignments.csv', newline='') as csvfile:
        data = csv.DictReader(csvfile, delimiter=",")
        result = dict()
        i = 0
        for row in data:
            result[country_list[i]] = dict()
            for country2 in country_list:
                result[country_list[i]].update({country2: row[country2]})
            i += 1
    return result


def distances(dictionary):
    """
        Devuelve las distancias de datos entre países de un diccionario pasado como parámetro.

        :param dictionary: Diccionario sobre el que se quieren calcular las distancias.
        :type dictionary: dict
        :return: Diccionario con las distancias calculadas.
    """
    result = dict()
    for i in list(dictionary.keys()):
        result[i] = dict()
    for i in list(dictionary.keys()):
        valor = dictionary[i][i]
        lista = list(dictionary.keys())
        for j in lista[lista.index(i):]:
            result[i].update({j: int(valor) - int(dictionary[i][j])})
            result[j].update({i: int(valor) - int(dictionary[j][i])})
    return result
