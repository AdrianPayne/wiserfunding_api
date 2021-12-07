
def z_score(year_data: dict) -> float:
    ebit = year_data['ebit']
    equity = year_data['equity']
    retained_earnings = year_data['retained_earnings']
    sales = year_data['sales']
    total_assets = year_data['total_assets']
    total_liabilities = year_data['total_liabilities']
    working_capital = year_data['working_capital']

    x1 = working_capital / total_assets
    x2 = retained_earnings / total_assets
    x3 = ebit / total_assets
    x4 = equity / total_liabilities
    x5 = sales / total_assets

    return round(1.2*x1 + 1.4*x2 + 3.3*x3 + 0.6*x4 + 1.0*x5, 2)


def process_financials_data(financials: list) -> dict:
    scores = []
    for year_data in financials:
        scores.append({'year': year_data['year'], 'zscore': z_score(year_data)})

    return {'scores': scores}
