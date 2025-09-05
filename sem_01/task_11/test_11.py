import pytest
import math
from .solution import (
    create_point,
    get_coordinates,
    calculate_distance,
    create_rectangle,
    calculate_area,
    is_point_inside,
    swap_coordinates,
)


def test_create_point():
    point = create_point(3, 4)
    assert isinstance(point, tuple), "Точка должна быть кортежем"
    assert len(point) == 2, "Точка должна содержать 2 координаты"
    assert point[0] == 3, "Координата x должна быть 3"
    assert point[1] == 4, "Координата y должна быть 4"


def test_get_coordinates():
    point = (3, 4)
    x, y = get_coordinates(point)
    assert x == 3, "Координата x должна быть 3"
    assert y == 4, "Координата y должна быть 4"


def test_calculate_distance():
    point1 = (0, 0)
    point2 = (3, 4)
    distance = calculate_distance(point1, point2)
    assert distance == 5.0, "Расстояние между (0,0) и (3,4) должно быть 5.0"

    point1 = (1, 1)
    point2 = (1, 1)
    distance = calculate_distance(point1, point2)
    assert distance == 0.0, "Расстояние между одинаковыми точками должно быть 0.0"

    point1 = (1, 2)
    point2 = (4, 6)
    distance = calculate_distance(point1, point2)
    assert distance == 5.0, "Расстояние между (1,2) и (4,6) должно быть 5.0"


def test_create_rectangle():
    top_left = (1, 5)
    bottom_right = (5, 1)
    rectangle = create_rectangle(top_left, bottom_right)

    assert isinstance(rectangle, tuple), "Прямоугольник должен быть кортежем"
    assert len(rectangle) == 2, "Прямоугольник должен содержать 2 точки"
    assert rectangle[0] == top_left, "Первая точка должна быть верхним левым углом"
    assert rectangle[1] == bottom_right, "Вторая точка должна быть нижним правым углом"


def test_calculate_area():
    rectangle = ((1, 5), (5, 1))
    area = calculate_area(rectangle)
    assert (
        area == 16.0
    ), "Площадь прямоугольника с углами (1,5) и (5,1) должна быть 16.0"

    rectangle = ((0, 0), (3, 4))
    area = calculate_area(rectangle)
    assert (
        area == 12.0
    ), "Площадь прямоугольника с углами (0,0) и (3,4) должна быть 12.0"

    rectangle = ((2, 2), (2, 2))
    area = calculate_area(rectangle)
    assert area == 0.0, "Площадь прямоугольника с совпадающими углами должна быть 0.0"


def test_is_point_inside():
    rectangle = ((1, 5), (5, 1))

    assert (
        is_point_inside(rectangle, (3, 3)) == True
    ), "Точка (3,3) должна быть внутри прямоугольника"
    assert (
        is_point_inside(rectangle, (1, 5)) == True
    ), "Точка (1,5) должна быть внутри прямоугольника (включая границы)"
    assert (
        is_point_inside(rectangle, (5, 1)) == True
    ), "Точка (5,1) должна быть внутри прямоугольника (включая границы)"
    assert (
        is_point_inside(rectangle, (0, 0)) == False
    ), "Точка (0,0) должна быть вне прямоугольника"
    assert (
        is_point_inside(rectangle, (6, 6)) == False
    ), "Точка (6,6) должна быть вне прямоугольника"


def test_swap_coordinates():
    point = (3, 4)
    swapped = swap_coordinates(point)

    assert isinstance(swapped, tuple), "Результат должен быть кортежем"
    assert swapped == (4, 3), "Координаты должны быть поменяны местами"

    point = (0, 0)
    swapped = swap_coordinates(point)
    assert swapped == (0, 0), "Для точки (0,0) обмен координат не меняет точку"


if __name__ == "__main__":
    pytest.main()
