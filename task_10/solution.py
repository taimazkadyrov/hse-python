# Задание 10: Множества
# Реализуйте функции для работы с множествами


def create_set_from_list(lst):
    """
    Создает множество из списка, удаляя дубликаты
    """
    lf = set(lst)
    return lf


def is_subset(set1, set2):
    """
    Проверяет, является ли set1 подмножеством set2
    """
    return set1.issubset(set2)


def union_sets(set1, set2):
    """
    Возвращает объединение двух множеств
    """
    set3 = set1.union(set2)
    return set3


def intersection_sets(set1, set2):
    """
    Возвращает пересечение двух множеств
    """
    set3 = set1.intersection(set2)
    return set3


def difference_sets(set1, set2):
    """
    Возвращает разность множеств (элементы, которые есть в set1, но отсутствуют в set2)
    """
    set3 = set1.difference(set2)
    return set3


def symmetric_difference_sets(set1, set2):
    """
    Возвращает симметричную разность множеств
    (элементы, которые есть в одном из множеств, но не в обоих одновременно)
    """
    set3 = set1.symmetric_difference(set2)
    return set3


def remove_duplicates_preserve_order(lst):
    """
    Удаляет дубликаты из списка, сохраняя порядок первого появления элементов
    Используйте множество для отслеживания уже встреченных элементов
    """
    set1 = set()
    lst1 = list()
    for item in lst:
        if item not in set1:
            lst1.append(item)
            set1.add(item)
    return lst1
