import pytest
from calc import Calculator


class TestCalculator:

    def setup(self):
        self.calc = Calculator


    def test_multiply_success(self):
        """Выполняем позитивный тест для проверки корректной работы метода multiply, для чего передаем
        необходимые числовые аргументы для умножения. Полученный результат произведения чисел сравниваем
        с ожидаемым посредством инструкции assert."""
        assert self.calc.multiply(self, 2, 2) == 4


    def test_division_success(self):
        """Выполняем позитивный тест для проверки корректной работы метода division, для чего передаем
        необходимые числовые аргументы для деления. Полученный результат частного сравниваем с ожидаемым
        посредством инструкции assert."""
        assert self.calc.division(self, 8, 8) == 1.0


    def test_subtraction_success(self):
        """Выполняем позитивный тест для проверки корректной работы метода subtraction, для чего передаем
        необходимые числовые аргументы для вычитания. Полученный результат разности чисел сравниваем
        с ожидаемым посредством инструкции assert."""
        assert self.calc.subtraction(self, 5, 5) == 0


    def test_adding_success(self):
        """Выполняем позитивный тест для проверки корректной работы метода adding, для чего передаем
        необходимые числовые аргументы для сложения. Полученный результат суммы чисел сравниваем
        с ожидаемым посредством инструкции assert."""
        assert self.calc.adding(self, 10, 10) == 20


    def test_adding_unsuccess(self):
        """Выполняем негативный тест для проверки корректной работы метода adding, для чего передаем необходимые
        числовые аргументы для сложения, а также для сравнения намеренно указываем некорректный ожидаемый результат."""
        assert self.calc.adding(self, 1, 1) == 2


    def test_zero_division(self):
        """Добавим позитивный тест проверки срабатывания исключения ZeroDivisionError при делении на 0."""
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)


    def teardown(self):
        print('Выполнение метода Teardown')



