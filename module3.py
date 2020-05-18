import random


def clustering(distances, k):
    countries = list(distances.keys())
    centers = random.sample(countries, k)
    last_centers = list()
    clusters = dict()
    while (centers!=last_centers):
        clusters = dict()
        for center in centers:
            clusters[center] = dict()
            clusters[center]["Cluster"]=list()
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
    centers = list()
    for center in list(sum_distances.keys()):
        mini = sum_distances[center].index(min(sum_distances[center]))
        centers.append(clusters[center]["Cluster"][mini])
    return centers


def get_center(country, centers, distances):
    distances_of_center = list()
    for center in centers:
        distances_of_center.append(distances[center][country])
    return centers[distances_of_center.index(min(distances_of_center))]