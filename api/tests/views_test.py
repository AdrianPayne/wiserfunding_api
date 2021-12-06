import json
import unittest
from api.v1.app import app


# Integrity test suit
class TestViews(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

        self.test_data = {
            'data_ok': {
                'country_iso_code': 'gb', 'company_id': 10149809,
                'payload_request': {'financials': [
                    {"year": 2020, "ebit": 123.45, "equity": 234.56, "retained_earnings": 345.67, "sales": 1234.56,
                     "total_assets": 345.67, "total_liabilities": 456.78, "working_capital": 23.45},
                    {"year": 2019, "ebit": 122.63, "equity": 224.56, "retained_earnings": 325.33, "sales": 1214.99,
                     "total_assets": 325.04, "total_liabilities": 426.78, "working_capital": 23.45},
                    {"year": 2018, "ebit": 120.17, "equity": 214.06, "retained_earnings": 225.00, "sales": 1204.01,
                     "total_assets": 305.11, "total_liabilities": 426.78, "working_capital": 23.45},
                    {"year": 2017, "ebit": 118.23, "equity": 204.96, "retained_earnings": 125.97, "sales": 1200.00,
                     "total_assets": 290.75, "total_liabilities": 426.78, "working_capital": 23.45},
                    {"year": 2016, "ebit": 116.05, "equity": 234.56, "retained_earnings": 105.11, "sales": 1010.82,
                     "total_assets": 250.13, "total_liabilities": 426.78, "working_capital": 23.45}
                ]}
            },
            'data_incorrect': {
                'country_iso_code': 12, 'company_id': 'hola',
                'payload_request': {'financials': [
                    {"year": 2020, "ebit": 123.45, "equity": 234.56, "retained_earnings": 345.67, "sales": 1234.56,
                     "total_assets": 345.67, "total_liabilities": 456.78, "working_capital": 23.45},
                    {"year": 2019, "ebit": 122.63, "equity": 224.56, "retained_earnings": 325.33, "sales": 1214.99,
                     "total_assets": 325.04, "total_liabilities": 426.78, "working_capital": 23.45}
                ]}
            }
        }

    def test_health_check(self):
        response = self.client.get('/healthcheck')

        self.assertEqual(200, response.status_code)
        self.assertEqual(b"Everything ok!", response.data)

    def test_z_score_view_ok(self):
        test_data = self.test_data['data_ok']
        expected_response = {"scores": [
            {"year": 2020, "zscore": 0}, {"year": 2019, "zscore": 0},
            {"year": 2018, "zscore": 0}, {"year": 2017, "zscore": 0},
            {"year": 2016, "zscore": 0}
        ]}

        response = self.client.put(f'/company/{test_data["country_iso_code"]}/{test_data["company_id"]}',
                                   data=json.dumps(test_data["payload_request"]),
                                   content_type='application/json')

        self.assertEqual(expected_response, response.data)

    def test_z_score_view_incorrect_input(self):
        test_data_incorrect = self.test_data['data_incorrect']
        test_data_ok = self.test_data['data_ok']

        data_cases = [
            {'country_iso_code': test_data_incorrect["country_iso_code"], 'company_id':test_data_ok["company_id"],
             'payload_request': test_data_ok["payload_request"]},
            {'country_iso_code': test_data_ok["country_iso_code"], 'company_id': test_data_incorrect["company_id"],
             'payload_request': test_data_ok["payload_request"]},
            {'country_iso_code': test_data_ok["country_iso_code"], 'company_id': test_data_ok["company_id"],
             'payload_request': test_data_incorrect["payload_request"]},
            {'country_iso_code': test_data_incorrect["country_iso_code"], 'company_id': test_data_ok["company_id"],
             'payload_request': test_data_incorrect["payload_request"]},
            {'country_iso_code': test_data_ok["country_iso_code"], 'company_id': test_data_ok["company_id"],
             'payload_request': test_data_ok["payload_request"]}
        ]

        for case in data_cases:
            response = self.client.put(f'/company/{case["country_iso_code"]}/{case["company_id"]}',
                                       data=json.dumps(case["payload_request"]),
                                       content_type='application/json')
            self.assertEqual(400, response.status_code)


if __name__ == '__main__':
    unittest.main()
