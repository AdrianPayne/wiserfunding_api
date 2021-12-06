# WiserFunding API
## Basic goals

Implement basic API:
- One resource: 
  ```
  company/<country_iso_code>/<id>
  ```
- One method: `PUT`
- JSON payload: financials for 5 years
- Response: `Z-Score formula` (explained later)

Complete example:
```
INPUT:
PUT /company/gb/10149809
{“financials”: [
{“year”: 2020, “ebit”: 123.45, “equity”: 234.56, “retained_earnings”: 345.67, “sales”:
1234.56, “total_assets”: 345.67, “total_liabilities”: 456.78, “working_capital”: 23.45},
{“year”: 2019, “ebit”: 122.63, “equity”: 224.56, “retained_earnings”: 325.33, “sales”:
1214.99, “total_assets”: 325.04, “total_liabilities”: 426.78, “working_capital”: 23.45},
{“year”: 2018, “ebit”: 120.17, “equity”: 214.06, “retained_earnings”: 225.00, “sales”:
1204.01, “total_assets”: 305.11, “total_liabilities”: 426.78, “working_capital”: 23.45},
{“year”: 2017, “ebit”: 118.23, “equity”: 204.96, “retained_earnings”: 125.97, “sales”:
1200.00, “total_assets”: 290.75, “total_liabilities”: 426.78, “working_capital”: 23.45},
{“year”: 2016, “ebit”: 116.05, “equity”: 234.56, “retained_earnings”: 105.11, “sales”:
1010.82, “total_assets”: 250.13, “total_liabilities”: 426.78, “working_capital”: 23.45}]}

OUTPUT:
{“scores”: [{“year”: 2020, “zscore”: xxx}, {“year”: 2019, “zscore”: xxx}, {“year”: 2018,
“zscore”: xxx}, {“year”: 2017, “zscore”: xxx}, {“year”: 2016, “zscore”: xxx}]}
```

### Z-Score formula
```
Z = 1.2X1 + 1.4X2 + 3.3X3 + 0.6X4 + 1.0X5
X1 = working_capital / total_assets
X2 = retained_earnings / total_assets
X3 = ebit / total_assets
X4 = equity / total_liabilities
X5 = sales / total_assets
```

## Plus goals
Additional endpoints to return previously generated reports:

- [ ] Database models in postgres or sqlite, mysql etc.
- [ ] Build and deploy to free cloud tier on AWS, GCP, Azure etc.
- [ ] docker compose up to run locally
- [ ] API documentation and examples
- [ ] Use of pre-commit, black, mypy, isort etc.
- [ ] Test coverage of 100%
- [ ] CI/CD with Travis or similar
