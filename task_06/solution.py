def sum_of_digits(n):
    pass


def count_digits(n):
    pass


def reverse_number(n):
    pass


def is_prime(n):
    pass


def gcd(a, b):
    pass


def binary_search(arr, target):
    pass


# Задание 6: Циклы (while)
# Реализуйте функции с использованием цикла while


def sum_of_digits(number):
    """
    Возвращает сумму цифр числа
    Например, для 123 результат должен быть 1 + 2 + 3 = 6
    """
    digit = [int(i) for i in str(number)]
    return sum(digit)


def count_digits(number):
    """
    Возвращает количество цифр в числе
    Например, для 123 результат должен быть 3
    """
    return len(str(number))


def reverse_number(number):
    """
    Возвращает число, записанное в обратном порядке
    Например, для 123 результат должен быть 321
    """
    return (int(str(number)[::-1]))


def is_prime(number):
    """
    Проверяет, является ли число простым
    Простое число - это число больше 1, которое делится только на 1 и на само себя
    """
    if number <= 1:
        return False
    for i in range(2, number + 1):
        if number % i == 0:
            break
    return i == number


def gcd(a, b):
    """
    Находит наибольший общий делитель (НОД) двух чисел
    Используйте алгоритм Евклида
    """
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def binary_search(sorted_list, target):
    """
    Реализует бинарный поиск элемента в отсортированном списке
    Возвращает индекс элемента, если он найден, иначе -1
    """
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
