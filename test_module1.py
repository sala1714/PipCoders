from unittest import TestCase
from Modules.module1 import median


class Test(TestCase):
    def test_median1(self):
        self.assertEqual(3, median([4, 3, 2, 1, 5], 2))
