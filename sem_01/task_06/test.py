import pytest
from solution import (
    sum_of_digits,
    count_digits,
    reverse_number,
    is_prime,
    gcd,
    binary_search,
)


def test_sum_of_digits():
    assert sum_of_digits(123) == 6, "Сумма цифр 123 должна быть 6"
    assert sum_of_digits(9) == 9, "Сумма цифр 9 должна быть 9"
    assert sum_of_digits(0) == 0, "Сумма цифр 0 должна быть 0"
    assert sum_of_digits(10) == 1, "Сумма цифр 10 должна быть 1"
    assert sum_of_digits(999) == 27, "Сумма цифр 999 должна быть 27"


def test_count_digits():
    assert count_digits(123) == 3, "Количество цифр в 123 должно быть 3"
    assert count_digits(9) == 1, "Количество цифр в 9 должно быть 1"
    assert count_digits(0) == 1, "Количество цифр в 0 должно быть 1"
    assert count_digits(10) == 2, "Количество цифр в 10 должно быть 2"
    assert count_digits(999) == 3, "Количество цифр в 999 должно быть 3"


def test_reverse_number():
    assert reverse_number(123) == 321, "Обратное число для 123 должно быть 321"
    assert reverse_number(9) == 9, "Обратное число для 9 должно быть 9"
    assert reverse_number(0) == 0, "Обратное число для 0 должно быть 0"
    assert reverse_number(10) == 1, "Обратное число для 10 должно быть 1"
    assert reverse_number(100) == 1, "Обратное число для 100 должно быть 1"
    assert reverse_number(999) == 999, "Обратное число для 999 должно быть 999"


def test_is_prime():
    assert is_prime(2) == True, "2 должно быть простым числом"
    assert is_prime(3) == True, "3 должно быть простым числом"
    assert is_prime(7) == True, "7 должно быть простым числом"
    assert is_prime(11) == True, "11 должно быть простым числом"
    assert is_prime(1) == False, "1 не должно быть простым числом"
    assert is_prime(4) == False, "4 не должно быть простым числом"
    assert is_prime(6) == False, "6 не должно быть простым числом"
    assert is_prime(9) == False, "9 не должно быть простым числом"
    assert is_prime(0) == False, "0 не должно быть простым числом"
    assert is_prime(-7) == False, "Отрицательные числа не должны быть простыми"


def test_gcd():
    assert gcd(12, 8) == 4, "НОД 12 и 8 должен быть 4"
    assert gcd(17, 5) == 1, "НОД 17 и 5 должен быть 1"
    assert gcd(0, 5) == 5, "НОД 0 и 5 должен быть 5"
    assert gcd(5, 0) == 5, "НОД 5 и 0 должен быть 5"
    assert gcd(0, 0) == 0, "НОД 0 и 0 должен быть 0"
    assert gcd(48, 18) == 6, "НОД 48 и 18 должен быть 6"


def test_binary_search():
    assert (
        binary_search([1, 2, 3, 4, 5], 3) == 2
    ), "Индекс элемента 3 в [1, 2, 3, 4, 5] должен быть 2"
    assert (
        binary_search([1, 2, 3, 4, 5], 1) == 0
    ), "Индекс элемента 1 в [1, 2, 3, 4, 5] должен быть 0"
    assert (
        binary_search([1, 2, 3, 4, 5], 5) == 4
    ), "Индекс элемента 5 в [1, 2, 3, 4, 5] должен быть 4"
    assert (
        binary_search([1, 2, 3, 4, 5], 6) == -1
    ), "Элемент 6 отсутствует в [1, 2, 3, 4, 5]"
    assert (
        binary_search([1, 2, 3, 4, 5], 0) == -1
    ), "Элемент 0 отсутствует в [1, 2, 3, 4, 5]"
    assert binary_search([], 5) == -1, "Поиск в пустом списке должен вернуть -1"
    assert binary_search([1], 1) == 0, "Индекс элемента 1 в [1] должен быть 0"
    assert binary_search([1], 2) == -1, "Элемент 2 отсутствует в [1]"


if __name__ == "__main__":
    pytest.main()
