def score(seq1, seq2):
    import needleman_wunsch as nw
    return nw.maximum_score(seq1, seq2)


def random_sequence(length):
    """ Random RNA string generator """
    import random
    letters = "ACGTNW"
    return ''.join(random.choice(letters) for i in range(length))


def calcular_temps():
    import timeit
    time = []
    for x in range(1, 500, 10):
        time.append((x, timeit.timeit("score(random_sequence(" + str(x) + "),random_sequence(" + str(x) + "))",
                                      setup="from __main__ import score, random_sequence", number=100)))
    return time


def crear_grafica(x_list, y_list):
    import matplotlib.pyplot as plt
    plt.scatter(x_list, y_list)
    plt.show()


if __name__ == '__main__':
    temps = calcular_temps()
    crear_grafica(*map(list, zip(*temps)))
