import pytest
from calculator import Calculator
from conftest import *

calculator = Calculator()


class TestCalculator:
    """Комплект тестов для модульного(unit) тестирования класса Calculator."""

    @time_of_test
    def test_multiply_success(self):
        """Выполняем позитивный тест для проверки корректной работы метода multiply, для чего передаем
        необходимые числовые аргументы для умножения. Полученный результат произведения чисел сравниваем
        с ожидаемым посредством инструкции assert."""

        result = calculator.multiply(2, 2)
        assert result == 4

    @time_of_test
    def test_division_success(self):
        """Выполняем позитивный тест для проверки корректной работы метода division, для чего передаем
        необходимые числовые аргументы для деления. Полученный результат частного сравниваем с ожидаемым
        посредством инструкции assert."""

        result = calculator.division(8, 8)
        assert result == 1

    @time_of_test
    def test_subtraction_success(self):
        """Выполняем позитивный тест для проверки корректной работы метода subtraction, для чего передаем
        необходимые числовые аргументы для вычитания. Полученный результат разности чисел сравниваем
        с ожидаемым посредством инструкции assert."""

        result = calculator.subtraction(5, 5)
        assert result == 0

    @time_of_test
    def test_adding_success(self):
        """Выполняем позитивный тест для проверки корректной работы метода adding, для чего передаем
        необходимые числовые аргументы для сложения. Полученный результат суммы чисел сравниваем
        с ожидаемым посредством инструкции assert."""

        result = calculator.adding(10, 10)
        assert result == 20

    def test_adding_unsuccessful(self):
        """Выполняем негативный тест для проверки корректной работы метода adding, для чего передаем необходимые
        числовые аргументы для сложения, а также для сравнения намеренно указываем некорректный ожидаемый результат."""

        assert calculator.adding(1, 1) == 3, (f"\nНегативный тест успешно пройден, ожидаемый результат != "
                                              f"фактическому.")

    @time_of_test
    def test_zero_division(self):
        """Добавим позитивный тест проверки срабатывания исключения ZeroDivisionError при делении на 0."""

        with pytest.raises(ZeroDivisionError):
            result = calculator.division(1, 0)
