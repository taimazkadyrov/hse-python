# Задание 11: Кортежи
# Реализуйте функции для работы с кортежами


def create_point(x, y):
    """
    Создает кортеж, представляющий точку в двумерном пространстве
    """
    return (x, y)


def get_coordinates(point):
    """
    Возвращает координаты x и y из кортежа-точки
    """
    x, y = point
    return x, y


def calculate_distance(point1, point2):
    """
    Вычисляет евклидово расстояние между двумя точками
    """
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def create_rectangle(top_left, bottom_right):
    """
    Создает кортеж, представляющий прямоугольник
    по координатам верхнего левого и нижнего правого углов
    """
    return (top_left, bottom_right)


def calculate_area(rectangle):
    """
    Вычисляет площадь прямоугольника
    """
    (x1, y1), (x2, y2) = rectangle
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    return width * height


def is_point_inside(rectangle, point):
    """
    Проверяет, находится ли точка внутри прямоугольника
    """
    (x1, y1), (x2, y2) = rectangle
    x3, y3 = point
    return min(x2, x1) <= x3 <= max(x2, x1) and min(y1, y2) <= y3 <= max(y2, y1)


def swap_coordinates(point):
    """
    Меняет местами координаты x и y в точке
    """
    x, y = point
    return (y, x)
