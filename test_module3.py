from unittest import TestCase
from modules.module3 import clustering


class Test(TestCase):
    def test_clustering(self):
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
        expected_result = dict()
        expected_result.update({1: {"Cluster": [0, 1, 2, 4, 5]}})
        expected_result.update({3: {"Cluster": [3]}})

        self.assertEqual(expected_result, clustering(data_distances, 2, (1, 4)))
