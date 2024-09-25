# content of test_sample.py
def inc(x):  # noqa: ANN001, ANN201, D103
    return x + 1


def test_answer() -> None:  # noqa: D103
    assert inc(5) == 6  # noqa: PLR2004, S101
