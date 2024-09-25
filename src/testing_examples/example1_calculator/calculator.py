"""Module contain only Calculator Class"""


class Calculator:
    """Calculator Class does simple calculations for you"""

    def add(self, a: float, b: float) -> float:
        """Return sum of two values."""
        return a + b

    def divide(self, a: float, b: float) -> float:
        """Return devision of two values"""
        if b == 0:
            msg = "'Some value' is incorrect"
            raise ValueError(msg)
        return a / b
