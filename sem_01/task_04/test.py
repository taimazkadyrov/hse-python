import pytest
from solution import (
    is_positive,
    is_even,
    is_in_range,
    max_of_three,
    fizz_buzz,
    grade_converter,
)


def test_is_positive():
    assert is_positive(5) == True, "5 должно быть положительным"
    assert is_positive(0) == False, "0 не должно считаться положительным"
    assert is_positive(-3) == False, "-3 не должно быть положительным"


def test_is_even():
    assert is_even(2) == True, "2 должно быть четным"
    assert is_even(0) == True, "0 должно быть четным"
    assert is_even(-4) == True, "-4 должно быть четным"
    assert is_even(3) == False, "3 не должно быть четным"
    assert is_even(-7) == False, "-7 не должно быть четным"


def test_is_in_range():
    assert is_in_range(5, 1, 10) == True, "5 должно быть в диапазоне [1, 10]"
    assert (
        is_in_range(1, 1, 10) == True
    ), "1 должно быть в диапазоне [1, 10] (включая границы)"
    assert (
        is_in_range(10, 1, 10) == True
    ), "10 должно быть в диапазоне [1, 10] (включая границы)"
    assert is_in_range(0, 1, 10) == False, "0 не должно быть в диапазоне [1, 10]"
    assert is_in_range(11, 1, 10) == False, "11 не должно быть в диапазоне [1, 10]"


def test_max_of_three():
    assert max_of_three(1, 2, 3) == 3, "Максимум из 1, 2, 3 должен быть 3"
    assert max_of_three(3, 2, 1) == 3, "Максимум из 3, 2, 1 должен быть 3"
    assert max_of_three(2, 3, 1) == 3, "Максимум из 2, 3, 1 должен быть 3"
    assert max_of_three(5, 5, 1) == 5, "Максимум из 5, 5, 1 должен быть 5"
    assert max_of_three(5, 5, 5) == 5, "Максимум из 5, 5, 5 должен быть 5"
    assert max_of_three(-1, -2, -3) == -1, "Максимум из -1, -2, -3 должен быть -1"


def test_fizz_buzz():
    assert fizz_buzz(3) == "Fizz", "Для числа 3 должно вернуться 'Fizz'"
    assert fizz_buzz(5) == "Buzz", "Для числа 5 должно вернуться 'Buzz'"
    assert fizz_buzz(15) == "FizzBuzz", "Для числа 15 должно вернуться 'FizzBuzz'"
    assert fizz_buzz(2) == "2", "Для числа 2 должно вернуться '2'"
    assert fizz_buzz(0) == "FizzBuzz", "Для числа 0 должно вернуться 'FizzBuzz'"


def test_grade_converter():
    assert grade_converter(95) == "A", "Оценка 95 должна быть 'A'"
    assert grade_converter(90) == "A", "Оценка 90 должна быть 'A'"
    assert grade_converter(85) == "B", "Оценка 85 должна быть 'B'"
    assert grade_converter(80) == "B", "Оценка 80 должна быть 'B'"
    assert grade_converter(75) == "C", "Оценка 75 должна быть 'C'"
    assert grade_converter(70) == "C", "Оценка 70 должна быть 'C'"
    assert grade_converter(65) == "D", "Оценка 65 должна быть 'D'"
    assert grade_converter(60) == "D", "Оценка 60 должна быть 'D'"
    assert grade_converter(55) == "F", "Оценка 55 должна быть 'F'"
    assert grade_converter(0) == "F", "Оценка 0 должна быть 'F'"
    assert (
        grade_converter(101) == "Invalid score"
    ), "Оценка 101 должна быть 'Invalid score'"
    assert (
        grade_converter(-1) == "Invalid score"
    ), "Оценка -1 должна быть 'Invalid score'"


if __name__ == "__main__":
    pytest.main()
