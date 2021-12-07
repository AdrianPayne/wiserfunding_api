import unittest

from v1 import z_score


# Unit tests
class TestZScore(unittest.TestCase):

    def test_z_score_function(self):
        test_data = {"year": 2016, "ebit": 116.05, "equity": 234.56, "retained_earnings": 105.11, "sales": 1010.82,
                     "total_assets": 250.13, "total_liabilities": 426.78, "working_capital": 23.45}

        self.assertEqual(6.60, z_score.z_score(test_data))



