# Задание 8: Функции
# Реализуйте различные функции согласно их описанию


def greet(name):
    """
    Возвращает приветствие для имени
    Например, "Привет, Иван!"
    """
    return f"Привет, {name}!"


def absolute_value(number):
    """
    Возвращает абсолютное значение числа
    """
    if number < 0:
        return -number
    return number


def calculate_area(shape, *args):
    """
    Вычисляет площадь фигуры

    Параметры:
    - shape: строка, тип фигуры ("circle", "rectangle", "triangle")
    - *args: аргументы для вычисления площади
        - для "circle": радиус
        - для "rectangle": длина и ширина
        - для "triangle": основание и высота

    Возвращает:
    - площадь фигуры или None, если тип фигуры неизвестен
    """
    import math
    if shape == "circle":
        return math.pi * args[0] * args[0]
    elif shape == "rectangle":
        return args[0] * args[1]
    elif shape == "triangle":
        return 0.5 * args[0] * args[1]
    else:
        return None


def apply_operation(operation, a, b):
    """
    Применяет операцию к двум числам

    Параметры:
    - operation: строка, операция ("add", "subtract", "multiply", "divide")
    - a, b: числа

    Возвращает:
    - результат операции или None, если операция неизвестна
    """
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return None
        return a / b
    else:
        return None


def create_multiplier(factor):
    """
    Создает и возвращает функцию, которая умножает свой аргумент на factor

    Пример использования:
    double = create_multiplier(2)
    result = double(5)  # result = 10
    """

    def bla(x):
        return x * factor

    return bla


def apply_to_each(func, items):
    """
    Применяет функцию func к каждому элементу списка items
    и возвращает список результатов

    Пример использования:
    result = apply_to_each(lambda x: x*2, [1, 2, 3])  # result = [2, 4, 6]
    """
    lok = list()
    for item in items:
        lok.append(func(item))
    return lok
