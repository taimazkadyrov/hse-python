import pytest
from .solution import (
    sum_of_numbers,
    factorial,
    count_vowels,
    find_max,
    filter_even_numbers,
    generate_multiplication_table,
)


def test_sum_of_numbers():
    assert sum_of_numbers(1) == 1, "Сумма чисел от 1 до 1 должна быть 1"
    assert sum_of_numbers(5) == 15, "Сумма чисел от 1 до 5 должна быть 15"
    assert sum_of_numbers(10) == 55, "Сумма чисел от 1 до 10 должна быть 55"
    assert sum_of_numbers(0) == 0, "Сумма чисел от 1 до 0 должна быть 0"


def test_factorial():
    assert factorial(0) == 1, "Факториал 0 должен быть 1"
    assert factorial(1) == 1, "Факториал 1 должен быть 1"
    assert factorial(5) == 120, "Факториал 5 должен быть 120"
    assert factorial(10) == 3628800, "Факториал 10 должен быть 3628800"


def test_count_vowels():
    assert count_vowels("hello") == 2, "В строке 'hello' должно быть 2 гласные"
    assert count_vowels("PYTHON") == 1, "В строке 'PYTHON' должна быть 1 гласная"
    assert count_vowels("aeiou") == 5, "В строке 'aeiou' должно быть 5 гласных"
    assert count_vowels("bcdfg") == 0, "В строке 'bcdfg' не должно быть гласных"
    assert count_vowels("") == 0, "В пустой строке не должно быть гласных"


def test_find_max():
    assert find_max([1, 2, 3, 4, 5]) == 5, "Максимум в [1, 2, 3, 4, 5] должен быть 5"
    assert find_max([5, 4, 3, 2, 1]) == 5, "Максимум в [5, 4, 3, 2, 1] должен быть 5"
    assert find_max([-1, -2, -3]) == -1, "Максимум в [-1, -2, -3] должен быть -1"
    assert find_max([7]) == 7, "Максимум в [7] должен быть 7"
    assert find_max([]) == None, "Максимум в пустом списке должен быть None"


def test_filter_even_numbers():
    assert filter_even_numbers([1, 2, 3, 4, 5]) == [
        2,
        4,
    ], "Четные числа в [1, 2, 3, 4, 5] должны быть [2, 4]"
    assert filter_even_numbers([2, 4, 6, 8]) == [
        2,
        4,
        6,
        8,
    ], "Четные числа в [2, 4, 6, 8] должны быть [2, 4, 6, 8]"
    assert filter_even_numbers([1, 3, 5, 7]) == [], "Четных чисел в [1, 3, 5, 7] нет"
    assert filter_even_numbers([]) == [], "Четных чисел в пустом списке нет"


def test_generate_multiplication_table():
    assert generate_multiplication_table(1) == [
        [1]
    ], "Таблица умножения 1x1 должна быть [[1]]"

    expected_2x2 = [[1, 2], [2, 4]]
    assert (
        generate_multiplication_table(2) == expected_2x2
    ), "Таблица умножения 2x2 неверна"

    expected_3x3 = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    assert (
        generate_multiplication_table(3) == expected_3x3
    ), "Таблица умножения 3x3 неверна"

    assert (
        generate_multiplication_table(0) == []
    ), "Таблица умножения 0x0 должна быть пустым списком"


if __name__ == "__main__":
    pytest.main()
