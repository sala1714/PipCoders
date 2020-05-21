def median(values, middle_position):
    from modules import module1 as m1
    return m1.median(values, middle_position)


def random_list(length):
    """ Random integer list generator """
    import random
    new_list = list(range(length))
    random.shuffle(new_list)
    return new_list


def calcular_temps():
    import timeit
    temps = []
    for x in range(1, 500, 10):
        temps.append((x, timeit.timeit("median(random_list(" + str(x) + "),len(random_list(" + str(x) + "))//2 )",
                                       setup="from __main__ import median, random_list", number=100)))
    return temps


def crear_grafica(x_list, y_list):
    import matplotlib.pyplot as plt
    plt.scatter(x_list, y_list)
    plt.show()


if __name__ == '__main__':
    temps = calcular_temps()
    crear_grafica(*map(list, zip(*temps)))
