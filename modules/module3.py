"""
    random: Se utiliza para calcular los primeros centros de manera aleatoria.
"""
import random


def clustering(distances, k, defined_centers=()):
    """
        Calcula el clustering de los paises pasados como parámetros.
        Aplica el algoritmo de k-medoids.

        :param distances: Diccionario sobre el que se quieren calcular los clusters.
        :type distances: dict
        :param k: Número de clusters a calcular.
        :type k: int
        :param defined_centers: Contiene los primeros centros sobre los que se ejecuta el clustering.
        :type defined_centers: tuple
        :return: Devulve un diccionario que contiene los clusters en forma de pais-lista.
    """
    countries = list(distances.keys())
    if not defined_centers:
        centers = random.sample(countries, k)
    else:
        centers = list(defined_centers)
    last_centers = list()
    clusters = dict()
    while centers != last_centers:
        clusters = dict()
        for center in centers:
            clusters[center] = dict()
            clusters[center]["Cluster"] = list()
        for country in countries:
            center = get_center(country, centers, distances)
            cluster_list = clusters[center]["Cluster"]
            cluster_list.append(country)
            clusters[center]["Cluster"] = cluster_list
        sum_distances = dict()
        for center in centers:
            sum_distances[center] = list()
            for country in clusters[center]["Cluster"]:
                sum_result = 0
                for country2 in clusters[center]["Cluster"]:
                    sum_result += distances[country][country2]
                sum_distances[center].append(sum_result)
        last_centers = centers
        centers = new_centers(sum_distances, clusters)
    return clusters


def new_centers(sum_distances, clusters):
    """
        Calcula los nuevos centros de cada vuelta del clustering.

        :param sum_distances: Diccionario que contiene listas de sumas asociadas a cada país.
        :type sum_distances: dict
        :param clusters: Diccionario que contiene los clusters de la vuelta actual.
        :type clusters: dict
        :return: Devuelve una lista con los nuevos centros.
    """
    centers = list()
    for center in list(sum_distances.keys()):
        mini = sum_distances[center].index(min(sum_distances[center]))
        centers.append(clusters[center]["Cluster"][mini])
    return centers


def get_center(country, centers, distances):
    """
        Calcula el pais de la lista centers con menos distancia al pais country.

        :param country: Pais sobre el que se calculará el centro.
        :type country: str
        :param centers: Lista que contiene los centros.
        :type centers: list
        :param distances: Diccionario que contiene las distancias entre paises.
        :type distances: dict
        :return: Devuleve el pais de la lista de centros mas cercano a country.
    """
    distances_of_center = list()
    for center in centers:
        distances_of_center.append(distances[center][country])
    return centers[distances_of_center.index(min(distances_of_center))]
