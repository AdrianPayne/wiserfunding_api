
def validate_z_score_view(country_iso_code: str, id_company: int, request_data: list) -> bool:
    # country_iso_code
    try:
        if not country_iso_code or not country_iso_code.isalpha() or len(country_iso_code) != 2:
            return False
        if not id_company or not int(id_company):
            return False
        if not request_data or len(request_data) == 0:
            return False

        financial_keywords = ['ebit', 'equity', 'retained_earnings', 'sales', 'total_assets',
                              'total_liabilities', 'working_capital']
        for row in request_data:
            for kword in financial_keywords:
                if kword not in row.keys():
                    return False
    except:
        return False

    return True
