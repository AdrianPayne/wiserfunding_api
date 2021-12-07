import unittest
from api.v1 import validators


class TestValidators(unittest.TestCase):

    def setUp(self):
        self.country_iso_code = 'es'
        self.id_company = 54
        self.request_data = [{"year": 2016, "ebit": 116.05, "equity": 234.56, "retained_earnings": 105.11,
                             "sales": 1010.82,"total_assets": 250.13, "total_liabilities": 426.78,
                             "working_capital": 23.45}]

    def test_validate_z_score_view_ok(self):
        self.assertTrue(validators.validate_z_score_view(self.country_iso_code, self.id_company, self.request_data))

    def test_validate_z_score_view_ko(self):
        self.request_data[0].pop("equity")
        self.assertFalse(validators.validate_z_score_view(self.country_iso_code, self.id_company, self.request_data))
