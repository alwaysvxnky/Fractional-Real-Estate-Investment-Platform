def calculate_dividend(investments):
    total = 0
    for rent, shares, total_shares in investments:
        total += rent * (shares / total_shares)
    return total