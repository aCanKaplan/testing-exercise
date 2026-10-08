# Your testing code
from src.my_math import add_numbers, subtract_numbers, multiply_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5

def test_subtract_numbers():
    assert subtract_numbers(5, 2) == 3

def test_multiply_numbers():
    assert multiply_numbers(2, 3) == 6
    