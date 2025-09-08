# Задание 2: Арифметические операции
# Реализуйте функции для выполнения основных арифметических операций


def add(a, b):
    """
    Сложение двух чисел
    """
    return a + b


def subtract(a, b):
    """
    Вычитание b из a
    """
    return a - b


def multiply(a, b):
    """
    Умножение двух чисел
    """
    return a * b


def divide(a, b):
    """
    Деление a на b
    Должно вызывать исключение ZeroDivisionError при делении на ноль
    """
    return a / b


def power(a, b):
    """
    Возведение числа a в степень b
    """
    return a ** b


def modulo(a, b):
    """
    Остаток от деления a на b
    """
    return a % b


def floor_division(a, b):
    """
    Целочисленное деление a на b
    """
    return a // b
