class Calculator:
    """Простые арифметические операции и проверка простых чисел."""

    def add(self, left: int | float, right: int | float) -> int | float:
        return left + right

    def subtract(self, left: int | float, right: int | float) -> int | float:
        return left - right

    def divide(self, numerator: int | float, denominator: int | float) -> float:
        if denominator == 0:
            raise ZeroDivisionError("Деление на ноль невозможно.")
        return numerator / denominator

    def is_prime_number(self, number: int) -> bool:
        if isinstance(number, bool) or not isinstance(number, int):
            raise TypeError("Проверяемое значение должно быть целым числом.")
        if number < 2:
            return False

        divisor = 2
        while divisor * divisor <= number:
            if number % divisor == 0:
                return False
            divisor += 1
        return True
