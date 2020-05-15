"""
    csv: Biblioteca usada para la carga de datos desde archivos csv.
"""
import csv


def select_accessions():
    """
        Rellena un diccionario con la muestra Accession mediana de cada país
        de una lista de muestras csv.

        :return: Devuelve un diccionario que contiene los paises con sus muestras Accession.
    """
    with open('data/sequences.csv', newline='') as csvfile:
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
        for country in list(countries.keys()):
            median_countries[country] = median(countries[country]["Length"], len(countries[country]["Length"]) // 2)
        return final_median_dict(countries, median_countries)


def median(values, middle_position):
    """
        Devuelve la longituda mediana de entre todas las muestras.
        :param values: Lista con las longitudes de las distintas muestras asociadas a cada país.
        :type values: list
        :param middle_position: Representa la posición media de la lista.
        :type middle_position: int
        :return: Devuelve la longituda mediana de entre todas las muestras.
    """
    pivot = values[0]
    below = [x for x in values if x < pivot]
    above = [x for x in values if x > pivot]

    num_less = len(below)
    num_less_or_eq = len(values) - len(above)

    if middle_position < num_less:
        return median(below, middle_position)
    elif middle_position >= num_less_or_eq:
        return median(above, middle_position - num_less_or_eq)
    else:
        return pivot


def final_median_dict(countries, median_countries):
    """
        Devuelve un diccionario con la muestra asociada a la longitud mediana para cada país.

        :param countries: Diccionario que contiene los paises con la lista de accessions-longitudes.
        :type countries: dict
        :param median_countries: Diccionario que contiene los paises con la longitud mediana.
        :type median_countries: dict
        :return: Devuelve un diccionario con los paises y su muestra Accession asociada
        a la longitud mediana.
    """
    result = dict()
    for country in list(countries.keys()):
        median_index = countries[country]["Length"].index(median_countries[country])
        result[country] = dict()
        result[country].update({"Accession": countries[country]["Accession"][median_index]})
    return result
