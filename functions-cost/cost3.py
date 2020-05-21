def local_execution():
    country_list = [0, 1, 2, 3, 4, 5]
    list_distances = [
        [0, 1, 4, 7, 6, 3],
        [1, 0, 3, 6, 5, 2],
        [4, 3, 0, 3, 4, 3],
        [7, 6, 3, 0, 5, 4],
        [6, 5, 4, 5, 0, 3],
        [3, 2, 3, 4, 3, 0],
    ]
    data_distances = dict()
    for country in country_list:
        data_distances[country] = dict()
        for country1 in country_list:
            data_distances[country][country1] = list_distances[country][country_list.index(country1)]
    return data_distances


def clustering(distances):
    from modules import module3 as m3
    import random

    return m3.clustering(distances, random.choice(range(5)))


def calcular_temps():
    import timeit
    time = []
    for x in range(1, 500, 10):
        time.append((x, timeit.timeit("clustering(local_execution())",
                                      setup="from __main__ import clustering, local_execution", number=100)))
    return time


def crear_grafica(x_list, y_list):
    import matplotlib.pyplot as plt
    plt.scatter(x_list, y_list)
    plt.show()


if __name__ == '__main__':
    temps = calcular_temps()
    crear_grafica(*map(list, zip(*temps)))
