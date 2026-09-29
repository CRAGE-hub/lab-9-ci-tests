import pytest

from calculator import Calculator


@pytest.fixture
def calculator() -> Calculator:
    return Calculator()


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (2, 3, 5),
        (0, 0, 0),
        (-2, 5, 3),
        (1.25, 2.5, 3.75),
    ],
)
def test_add(calculator: Calculator, left: int | float, right: int | float, expected: int | float) -> None:
    assert calculator.add(left, right) == expected


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (8, 3, 5),
        (0, 7, -7),
        (-4, -6, 2),
        (1.5, 2.25, -0.75),
    ],
)
def test_subtract(calculator: Calculator, left: int | float, right: int | float, expected: int | float) -> None:
    assert calculator.subtract(left, right) == expected


@pytest.mark.parametrize(
    ("numerator", "denominator", "expected"),
    [
        (8, 2, 4.0),
        (7, 2, 3.5),
        (-9, 3, -3.0),
        (0, 5, 0.0),
    ],
)
def test_divide(calculator: Calculator, numerator: int | float, denominator: int | float, expected: float) -> None:
    assert calculator.divide(numerator, denominator) == expected


@pytest.mark.parametrize("denominator", [0, 0.0, -0.0])
def test_divide_by_zero_raises_error(calculator: Calculator, denominator: int | float) -> None:
    with pytest.raises(ZeroDivisionError, match="Деление на ноль невозможно"):
        calculator.divide(10, denominator)


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (2, True),
        (3, True),
        (4, False),
        (1, False),
        (0, False),
        (-7, False),
        (97, True),
        (100, False),
        (7919, True),
        (49, False),
    ],
)
def test_is_prime_number(calculator: Calculator, number: int, expected: bool) -> None:
    assert calculator.is_prime_number(number) is expected


@pytest.mark.parametrize("value", [2.5, "7", True, None])
def test_is_prime_number_rejects_non_integers(calculator: Calculator, value: object) -> None:
    with pytest.raises(TypeError, match="целым числом"):
        calculator.is_prime_number(value)
