from unittest import TestCase
import needleman_wunsch as nw


class Test(TestCase):
    def test_maximum_score(self):
        sample1 = "AGCCTAGTCG"
        sample2 = "AAGTCGATAGCCAG"
        self.assertEqual(2, nw.maximum_score(sample1,sample2))

    def test_maximum_score_empty(self):
        sample1 = ""
        sample2 = ""
        self.assertEqual(0, nw.maximum_score(sample1,sample2))

    def test_maximum_score_only_empty(self):
        sample1 = "AGCCTAGTCG"
        self.assertEqual(-10, nw.maximum_score(sample1,""))

    def test_maximum_score_equals(self):
        sample1 = "AGCCTAGTCG"
        self.assertEqual(len(sample1), nw.maximum_score(sample1, sample1))

