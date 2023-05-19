import pytest
from calc import Calculator


class TestCalculator:

    def setup(self):
        self.calc = Calculator

    def test_multiply_success(self):
        """Выполняем позитивный тест для проверки корректной работы метода multiply, для чего передаем функции
        необходимые числовые аргументы для умножения. Полученный результат произведения чисел сравниваем с ожидаемым
        посредством инструкции assert."""
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_success(self):
        assert self.calc.division(self, 8, 8) == 1.0

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 5, 5) == 0

    def test_adding_success(self):
        assert self.calc.adding(self, 10, 10) == 20

    def test_adding_unsuccess(self):  # добавим тест-кейс негативного тестирования метода adding.
        assert self.calc.adding(self, 1, 1) == 2

    def test_zero_division(self):   # добавим позитивный тест проверки срабатывания ZeroDivisionError при делении на 0.
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 100, 0)

    def teardown(self):
        print('Выполнение метода Teardown')
