import pytest
from solution import (
    create_set_from_list,
    is_subset,
    union_sets,
    intersection_sets,
    difference_sets,
    symmetric_difference_sets,
    remove_duplicates_preserve_order,
)


def test_create_set_from_list():
    assert create_set_from_list([1, 2, 3, 3, 2, 1]) == {
        1,
        2,
        3,
    }, "Множество из [1, 2, 3, 3, 2, 1] должно быть {1, 2, 3}"
    assert create_set_from_list([1, 1, 1]) == {
        1
    }, "Множество из [1, 1, 1] должно быть {1}"
    assert (
        create_set_from_list([]) == set()
    ), "Множество из пустого списка должно быть пустым"


def test_is_subset():
    assert (
        is_subset({1, 2}, {1, 2, 3}) == True
    ), "{1, 2} должно быть подмножеством {1, 2, 3}"
    assert (
        is_subset({1, 2, 3}, {1, 2, 3}) == True
    ), "{1, 2, 3} должно быть подмножеством самого себя"
    assert (
        is_subset({1, 4}, {1, 2, 3}) == False
    ), "{1, 4} не должно быть подмножеством {1, 2, 3}"
    assert (
        is_subset(set(), {1, 2, 3}) == True
    ), "Пустое множество должно быть подмножеством любого множества"
    assert (
        is_subset({1, 2, 3}, set()) == False
    ), "Непустое множество не должно быть подмножеством пустого множества"


def test_union_sets():
    assert union_sets({1, 2}, {3, 4}) == {
        1,
        2,
        3,
        4,
    }, "Объединение {1, 2} и {3, 4} должно быть {1, 2, 3, 4}"
    assert union_sets({1, 2}, {2, 3}) == {
        1,
        2,
        3,
    }, "Объединение {1, 2} и {2, 3} должно быть {1, 2, 3}"
    assert union_sets({1, 2}, set()) == {
        1,
        2,
    }, "Объединение {1, 2} и пустого множества должно быть {1, 2}"
    assert (
        union_sets(set(), set()) == set()
    ), "Объединение пустых множеств должно быть пустым"


def test_intersection_sets():
    assert intersection_sets({1, 2, 3}, {2, 3, 4}) == {
        2,
        3,
    }, "Пересечение {1, 2, 3} и {2, 3, 4} должно быть {2, 3}"
    assert (
        intersection_sets({1, 2}, {3, 4}) == set()
    ), "Пересечение {1, 2} и {3, 4} должно быть пустым"
    assert intersection_sets({1, 2}, {1, 2}) == {
        1,
        2,
    }, "Пересечение {1, 2} и {1, 2} должно быть {1, 2}"
    assert (
        intersection_sets({1, 2}, set()) == set()
    ), "Пересечение {1, 2} и пустого множества должно быть пустым"


def test_difference_sets():
    assert difference_sets({1, 2, 3}, {2, 3, 4}) == {
        1
    }, "Разность {1, 2, 3} и {2, 3, 4} должна быть {1}"
    assert difference_sets({1, 2}, {3, 4}) == {
        1,
        2,
    }, "Разность {1, 2} и {3, 4} должна быть {1, 2}"
    assert (
        difference_sets({1, 2}, {1, 2}) == set()
    ), "Разность {1, 2} и {1, 2} должна быть пустой"
    assert difference_sets({1, 2}, set()) == {
        1,
        2,
    }, "Разность {1, 2} и пустого множества должна быть {1, 2}"
    assert (
        difference_sets(set(), {1, 2}) == set()
    ), "Разность пустого множества и {1, 2} должна быть пустой"


def test_symmetric_difference_sets():
    assert symmetric_difference_sets({1, 2, 3}, {2, 3, 4}) == {
        1,
        4,
    }, "Симметричная разность {1, 2, 3} и {2, 3, 4} должна быть {1, 4}"
    assert symmetric_difference_sets({1, 2}, {3, 4}) == {
        1,
        2,
        3,
        4,
    }, "Симметричная разность {1, 2} и {3, 4} должна быть {1, 2, 3, 4}"
    assert (
        symmetric_difference_sets({1, 2}, {1, 2}) == set()
    ), "Симметричная разность {1, 2} и {1, 2} должна быть пустой"
    assert symmetric_difference_sets({1, 2}, set()) == {
        1,
        2,
    }, "Симметричная разность {1, 2} и пустого множества должна быть {1, 2}"
    assert symmetric_difference_sets(set(), {1, 2}) == {
        1,
        2,
    }, "Симметричная разность пустого множества и {1, 2} должна быть {1, 2}"


def test_remove_duplicates_preserve_order():
    assert remove_duplicates_preserve_order([1, 2, 3, 3, 2, 1]) == [
        1,
        2,
        3,
    ], "Список [1, 2, 3, 3, 2, 1] без дубликатов должен быть [1, 2, 3]"
    assert remove_duplicates_preserve_order([1, 1, 1]) == [
        1
    ], "Список [1, 1, 1] без дубликатов должен быть [1]"
    assert (
        remove_duplicates_preserve_order([]) == []
    ), "Пустой список без дубликатов должен остаться пустым"
    assert remove_duplicates_preserve_order([3, 2, 1, 2, 3]) == [
        3,
        2,
        1,
    ], "Список [3, 2, 1, 2, 3] без дубликатов должен быть [3, 2, 1]"


if __name__ == "__main__":
    pytest.main()
