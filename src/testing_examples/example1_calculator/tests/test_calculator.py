def my_function() -> int:
    """Always returns 42.

    Returns
    -------
        Always 42.
    """  # noqa: D401
    return 42

"""This module contains example tests."""


def test_my_function() -> None:  # noqa: D103
    expected_value = 42
    assert my_function() == expected_value  # noqa: S101
