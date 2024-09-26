"""Test Calculator Class."""
import pytest

from example1.calculator import Calculator


@pytest.fixture
def calculator():
    """Fixture to create a Calculator instance."""
    return Calculator()


# Positive test cases
def test_add_positive(calculator):
    """Test add method with positive numbers."""
    assert calculator.add(10, 5) == 15


def test_divide_positive(calculator):
    """Test divide method with valid input values."""
    assert calculator.divide(10, 2) == 5.0


# Negative test cases
def test_add_negative(calculator):
    """Test add method with negative numbers."""
    assert calculator.add(-3, -7) == -10


def test_divide_by_zero(calculator):
    """Test divide method raises ValueError for division by zero."""
    with pytest.raises(ValueError):
        calculator.divide(10, 0)


# Boundary test cases
def test_add_boundary_zero(calculator):
    """Test add method when one value is zero."""
    assert calculator.add(0, 5) == 5


def test_divide_boundary_zero(calculator):
    """Test divide method when numerator is zero."""
    assert calculator.divide(0, 5) == 0.0


def test_divide_boundary_near_zero(calculator):
    """Test divide method with very small non-zero denominator."""
    assert pytest.approx(calculator.divide(10, 1e-7), rel=1e-9) == 100000000.0


# Edge cases
def test_add_large_numbers(calculator):
    """Test add method with large floating-point numbers."""
    assert calculator.add(1e18, 1e18) == 2e18


def test_divide_large_numbers(calculator):
    """Test divide method with large floating-point numbers."""
    assert calculator.divide(1e18, 1e6) == 1e12


def test_add_float_precision(calculator):
    """Test add method with floating-point precision."""
    assert pytest.approx(calculator.add(0.1, 0.2), rel=1e-9) == 0.3


def test_divide_float_precision(calculator):
    """Test divide method with floating-point precision."""
    assert pytest.approx(calculator.divide(1.0, 3.0), rel=1e-9) == 0.3333333
