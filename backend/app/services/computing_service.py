
class ComputingService:
    def __init__(self, decimal_places: int):
        self._decimal_places = decimal_places

    @property
    def decimal_places(self) -> int:
        return self._decimal_places

    def _round(self, v) -> float:
        return round(v, self._decimal_places)

    def add(self, a, b):
        return self._round(a + b)

    def subtract(self, a, b):
        return self._round(a - b)

    def multiply(self, a, b):
        return self._round(a * b)

    def divide(self, a, b):
        return self._round(a / b)

    def modulo(self, a, b) -> int:
        return a % b

    def integer_divide(self, a, b) -> int:
        return a // b