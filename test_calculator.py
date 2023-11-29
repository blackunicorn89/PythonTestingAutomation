import pytest
from calculator_test import add, multiply, power

@pytest.mark.parametrize("input1, input2, expected", [
    (3, 5, 8),
    (-1, 1, 0),
    (5, 5, 10),
])
def test_add(input1, input2, expected):
    result = add(input1, input2)
    assert result == expected

@pytest.mark.parametrize("input1, input2, expected", [
    (2, 4, 8),
    (-3, 6, -18),
    # Lisää tarvittaessa muita testejä
])
def test_multiply(input1, input2, expected):
    result = multiply(input1, input2)
    assert result == expected

@pytest.mark.parametrize("input1, input2, expected", [
    (2, 3, 8),
    (5, 0, 1),
    (2, 2, 4),
    # Lisää tarvittaessa muita testejä
])
def test_power(input1, input2, expected):
    result = power(input1, input2)
    assert result == expected
