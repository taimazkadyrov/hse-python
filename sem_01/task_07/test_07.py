import pytest
from .solution import (
    create_list,
    find_element_index,
    remove_duplicates,
    merge_lists,
    list_intersection,
    list_difference,
    flatten_list,
)


def test_create_list():
    assert create_list(1, 5) == [
        1,
        2,
        3,
        4,
        5,
    ], "Список от 1 до 5 должен быть [1, 2, 3, 4, 5]"
    assert create_list(1, 5, 2) == [
        1,
        3,
        5,
    ], "Список от 1 до 5 с шагом 2 должен быть [1, 3, 5]"
    assert create_list(5, 1, -1) == [
        5,
        4,
        3,
        2,
        1,
    ], "Список от 5 до 1 с шагом -1 должен быть [5, 4, 3, 2, 1]"
    assert create_list(1, 1) == [1], "Список от 1 до 1 должен быть [1]"
    assert create_list(1, 0) == [], "Список от 1 до 0 должен быть пустым"


def test_find_element_index():
    assert (
        find_element_index([1, 2, 3, 4, 5], 3) == 2
    ), "Индекс элемента 3 в [1, 2, 3, 4, 5] должен быть 2"
    assert (
        find_element_index([1, 2, 3, 4, 5], 6) == -1
    ), "Индекс отсутствующего элемента должен быть -1"
    assert (
        find_element_index([1, 2, 3, 3, 4], 3) == 2
    ), "Должен вернуть индекс первого вхождения"
    assert (
        find_element_index([], 1) == -1
    ), "Индекс элемента в пустом списке должен быть -1"


def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 3, 4, 5, 5]) == [
        1,
        2,
        3,
        4,
        5,
    ], "Должен удалить дубликаты"
    assert remove_duplicates([1, 1, 1, 1]) == [1], "Должен оставить только один элемент"
    assert remove_duplicates([1, 2, 3]) == [
        1,
        2,
        3,
    ], "Не должен изменять список без дубликатов"
    assert remove_duplicates([]) == [], "Не должен изменять пустой список"


def test_merge_lists():
    assert sorted(merge_lists([1, 2, 3], [3, 4, 5])) == [
        1,
        2,
        3,
        4,
        5,
    ], "Объединение [1, 2, 3] и [3, 4, 5] должно быть [1, 2, 3, 4, 5]"
    assert sorted(merge_lists([1, 2], [3, 4])) == [
        1,
        2,
        3,
        4,
    ], "Объединение [1, 2] и [3, 4] должно быть [1, 2, 3, 4]"
    assert sorted(merge_lists([1, 2], [1, 2])) == [
        1,
        2,
    ], "Объединение [1, 2] и [1, 2] должно быть [1, 2]"
    assert (
        merge_lists([], []) == []
    ), "Объединение пустых списков должно быть пустым списком"


def test_list_intersection():
    assert sorted(list_intersection([1, 2, 3], [3, 4, 5])) == [
        3
    ], "Пересечение [1, 2, 3] и [3, 4, 5] должно быть [3]"
    assert (
        sorted(list_intersection([1, 2, 3], [4, 5, 6])) == []
    ), "Пересечение [1, 2, 3] и [4, 5, 6] должно быть пустым"
    assert sorted(list_intersection([1, 2, 3], [1, 2, 3])) == [
        1,
        2,
        3,
    ], "Пересечение [1, 2, 3] и [1, 2, 3] должно быть [1, 2, 3]"
    assert (
        list_intersection([], [1, 2, 3]) == []
    ), "Пересечение пустого списка с любым должно быть пустым"


def test_list_difference():
    assert sorted(list_difference([1, 2, 3], [3, 4, 5])) == [
        1,
        2,
    ], "Разность [1, 2, 3] и [3, 4, 5] должна быть [1, 2]"
    assert sorted(list_difference([1, 2, 3], [4, 5, 6])) == [
        1,
        2,
        3,
    ], "Разность [1, 2, 3] и [4, 5, 6] должна быть [1, 2, 3]"
    assert (
        list_difference([1, 2, 3], [1, 2, 3]) == []
    ), "Разность [1, 2, 3] и [1, 2, 3] должна быть пустой"
    assert (
        list_difference([], [1, 2, 3]) == []
    ), "Разность пустого списка и любого должна быть пустой"


def test_flatten_list():
    assert flatten_list([1, [2, 3], [4, [5, 6]]]) == [
        1,
        2,
        3,
        4,
        5,
        6,
    ], "Неправильное преобразование вложенного списка"
    assert flatten_list([1, 2, 3]) == [1, 2, 3], "Не должен изменять плоский список"
    assert flatten_list([]) == [], "Не должен изменять пустой список"
    assert flatten_list([[1, 2], [3, 4]]) == [
        1,
        2,
        3,
        4,
    ], "Неправильное преобразование списка списков"


if __name__ == "__main__":
    pytest.main()
