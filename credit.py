
def calculate_risk(income, debt, age):
    """
    Calculate the financial risk based on the debt-to-income ratio.

    Returns:
        -1: Invalid income
        HIGH: High financial risk
        MEDIUM: Medium financial risk
        LOW: Low financial risk
    """

    if income <= 0:
        return -1

    ratio = debt / income

    if ratio > 0.6:
        return "HIGH"
    elif ratio > 0.3:
        return "MEDIUM"
    else:
        return "LOW"
