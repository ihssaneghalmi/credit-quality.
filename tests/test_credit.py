
from credit import calculate_risk


def test_high_risk():
    result = calculate_risk(1000, 700, 30)
    assert result == "HIGH"


def test_medium_risk():
    result = calculate_risk(1000, 400, 30)
    assert result == "MEDIUM"


def test_low_risk():
    result = calculate_risk(1000, 100, 30)
    assert result == "LOW"

def test_zero_income():
    result = calculate_risk(0, 100, 30)
    assert result == -1


def test_negative_income():
    result = calculate_risk(-1000, 100, 30)
    assert result == -1


def test_zero_debt():
    result = calculate_risk(1000, 0, 30)
    assert result == "LOW"


def test_ratio_exactly_03():
    result = calculate_risk(1000, 300, 30)
    assert result == "LOW"


def test_ratio_exactly_06():
    result = calculate_risk(1000, 600, 30)
    assert result == "MEDIUM"
