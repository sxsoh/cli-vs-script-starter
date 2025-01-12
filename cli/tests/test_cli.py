"""Test suite to ensure that each function words correctly."""

from cli import __version__
from cli import main

# TODO: Add comments to explain the steps in these test cases

def test_version():
    """Confirm that the version of the program is correct."""
    assert __version__ == "0.1.0"


def test_compute_one_by_addition():
    """Confirm addition in a loop does not add to 1.0"""
    one = 1.0
    one_by_addition = main.compute_one_by_addition()
    assert one != one_by_addition

def test_compute_one_by_multiplication():
    """Confirm multiplication does result in 1.0"""
    one = 1.0
    one_by_multiplication = main.compute_one_by_multiplication()
    assert one == one_by_multiplication

def test_determine_even_odd():
    """Confirm if the number 1 is odd"""
    number = 1
    expected_result = "odd"
    actual_result = main.determine_even_odd(number)
    assert expected_result == actual_result



