import pytest
from src.calculator import calculator


@pytest.mark.parametrize("n, expected", [
    (2, 8),
    (-3, -27),
    (4, 64),
])
def test_cubeNums(n, expected):
    assert calculator.cubeNums(n) == expected
    
@pytest.mark.parametrize("n, expected", [
    (2, 4),
    (-2, 4),
    (0, 0),
])
def test_squareNums(n, expected):
    assert calculator.squareNums(n) == expected
    
@pytest.mark.parametrize("n, expected", [
    (3, 7),
    (4, 11),
    (5, 16),
])
def test_lazyCaterer(n, expected):
    assert calculator.lazyCaterer(n) == expected
    
@pytest.mark.parametrize("n, expected", [
    (5, 15),
    (6, 21),
    (7, 28),
])
def test_triNums(n, expected):
    assert calculator.triNums(n) == expected
    
@pytest.mark.parametrize("n, expected", [
    (3, 15),
    (4, 34),
    (5, 65),
])
def test_magicSquares(n, expected):
    assert calculator.magicSquares(n) == expected
    
@pytest.mark.parametrize("n, expected", [
    (5, 120),
    (6, 720),
    (0, 1),
])
def test_factorial(n, expected):
    assert calculator.factorial(n) == expected
    
@pytest.mark.parametrize("n, expected", [
    (3, 3),
    (-3, 3),
    (-281, 281),
])
def test_absolute(n, expected):
    assert calculator.absolute(n) == expected