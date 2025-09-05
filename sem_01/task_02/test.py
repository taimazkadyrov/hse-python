import pytest
from .solution import add, subtract, multiply, divide, power, modulo, floor_division


def test_add():
    assert add(5, 3) == 8, "5 + 3 должно быть равно 8"
    assert add(-1, 1) == 0, "-1 + 1 должно быть равно 0"
    assert add(0, 0) == 0, "0 + 0 должно быть равно 0"
    assert add(0.1, 0.2) == pytest.approx(
        0.3
    ), "0.1 + 0.2 должно быть примерно равно 0.3"


def test_subtract():
    assert subtract(5, 3) == 2, "5 - 3 должно быть равно 2"
    assert subtract(1, 1) == 0, "1 - 1 должно быть равно 0"
    assert subtract(0, 5) == -5, "0 - 5 должно быть равно -5"
    assert subtract(10, 0.5) == 9.5, "10 - 0.5 должно быть равно 9.5"


def test_multiply():
    assert multiply(5, 3) == 15, "5 * 3 должно быть равно 15"
    assert multiply(-1, 1) == -1, "-1 * 1 должно быть равно -1"
    assert multiply(0, 5) == 0, "0 * 5 должно быть равно 0"
    assert multiply(0.5, 2) == 1.0, "0.5 * 2 должно быть равно 1.0"


def test_divide():
    assert divide(6, 3) == 2, "6 / 3 должно быть равно 2"
    assert divide(5, 2) == 2.5, "5 / 2 должно быть равно 2.5"
    assert divide(0, 5) == 0, "0 / 5 должно быть равно 0"

    # Проверка деления на ноль
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)


def test_power():
    assert power(2, 3) == 8, "2 в степени 3 должно быть равно 8"
    assert power(5, 0) == 1, "5 в степени 0 должно быть равно 1"
    assert power(0, 5) == 0, "0 в степени 5 должно быть равно 0"
    assert power(2, -1) == 0.5, "2 в степени -1 должно быть равно 0.5"


def test_modulo():
    assert modulo(7, 3) == 1, "7 % 3 должно быть равно 1"
    assert modulo(10, 5) == 0, "10 % 5 должно быть равно 0"
    assert modulo(0, 5) == 0, "0 % 5 должно быть равно 0"

    # Проверка деления на ноль
    with pytest.raises(ZeroDivisionError):
        modulo(5, 0)


def test_floor_division():
    assert floor_division(7, 3) == 2, "7 // 3 должно быть равно 2"
    assert floor_division(10, 5) == 2, "10 // 5 должно быть равно 2"
    assert floor_division(0, 5) == 0, "0 // 5 должно быть равно 0"
    assert floor_division(-7, 3) == -3, "-7 // 3 должно быть равно -3"

    # Проверка деления на ноль
    with pytest.raises(ZeroDivisionError):
        floor_division(5, 0)


if __name__ == "__main__":
    pytest.main()
