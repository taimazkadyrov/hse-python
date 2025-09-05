import pytest
import math
from solution import (
    greet,
    absolute_value,
    calculate_area,
    apply_operation,
    create_multiplier,
    apply_to_each,
)


def test_greet():
    assert greet("Иван") == "Привет, Иван!", "Приветствие должно быть 'Привет, Иван!'"
    assert (
        greet("Мария") == "Привет, Мария!"
    ), "Приветствие должно быть 'Привет, Мария!'"
    assert (
        greet("") == "Привет, !"
    ), "Приветствие для пустой строки должно быть 'Привет, !'"


def test_absolute_value():
    assert absolute_value(5) == 5, "Абсолютное значение 5 должно быть 5"
    assert absolute_value(-5) == 5, "Абсолютное значение -5 должно быть 5"
    assert absolute_value(0) == 0, "Абсолютное значение 0 должно быть 0"
    assert absolute_value(-0.5) == 0.5, "Абсолютное значение -0.5 должно быть 0.5"


def test_calculate_area():
    # Проверка площади круга
    assert calculate_area("circle", 1) == pytest.approx(
        math.pi
    ), "Площадь круга с радиусом 1 должна быть примерно равна π"
    assert calculate_area("circle", 2) == pytest.approx(
        4 * math.pi
    ), "Площадь круга с радиусом 2 должна быть примерно равна 4π"

    # Проверка площади прямоугольника
    assert (
        calculate_area("rectangle", 2, 3) == 6
    ), "Площадь прямоугольника 2x3 должна быть 6"
    assert (
        calculate_area("rectangle", 0, 5) == 0
    ), "Площадь прямоугольника 0x5 должна быть 0"

    # Проверка площади треугольника
    assert (
        calculate_area("triangle", 4, 3) == 6
    ), "Площадь треугольника с основанием 4 и высотой 3 должна быть 6"
    assert (
        calculate_area("triangle", 0, 5) == 0
    ), "Площадь треугольника с основанием 0 должна быть 0"

    # Проверка неизвестной фигуры
    assert (
        calculate_area("unknown", 1, 2) is None
    ), "Для неизвестной фигуры должно возвращаться None"


def test_apply_operation():
    assert apply_operation("add", 2, 3) == 5, "2 + 3 должно быть 5"
    assert apply_operation("subtract", 5, 3) == 2, "5 - 3 должно быть 2"
    assert apply_operation("multiply", 2, 3) == 6, "2 * 3 должно быть 6"
    assert apply_operation("divide", 6, 3) == 2, "6 / 3 должно быть 2"
    assert (
        apply_operation("divide", 5, 0) is None
    ), "Деление на ноль должно возвращать None"
    assert (
        apply_operation("unknown", 2, 3) is None
    ), "Неизвестная операция должна возвращать None"


def test_create_multiplier():
    double = create_multiplier(2)
    triple = create_multiplier(3)

    assert double(5) == 10, "Умножение 5 на 2 должно быть 10"
    assert double(0) == 0, "Умножение 0 на 2 должно быть 0"
    assert double(-3) == -6, "Умножение -3 на 2 должно быть -6"

    assert triple(5) == 15, "Умножение 5 на 3 должно быть 15"
    assert triple(0) == 0, "Умножение 0 на 3 должно быть 0"
    assert triple(-3) == -9, "Умножение -3 на 3 должно быть -9"


def test_apply_to_each():
    assert apply_to_each(lambda x: x * 2, [1, 2, 3]) == [
        2,
        4,
        6,
    ], "Удвоение каждого элемента [1, 2, 3] должно дать [2, 4, 6]"
    assert apply_to_each(lambda x: x + 1, [1, 2, 3]) == [
        2,
        3,
        4,
    ], "Увеличение на 1 каждого элемента [1, 2, 3] должно дать [2, 3, 4]"
    assert apply_to_each(lambda x: x**2, [1, 2, 3]) == [
        1,
        4,
        9,
    ], "Возведение в квадрат каждого элемента [1, 2, 3] должно дать [1, 4, 9]"
    assert (
        apply_to_each(lambda x: x, []) == []
    ), "Применение функции к пустому списку должно дать пустой список"


if __name__ == "__main__":
    pytest.main()
