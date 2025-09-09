# Задание 7: Списки и операции со списками
# Реализуйте функции для работы со списками


def create_list(start, end, step=1):
    """
    Создает список чисел от start до end (включительно) с шагом step
    """
    if step > 0:
        return [i for i in range(start, end + 1, step)]
    else:
        return [i for i in range(start, end - 1, step)]

def find_element_index(lst, element):
    """
    Находит индекс первого вхождения элемента в список
    Если элемент не найден, возвращает -1
    """
    try:
        return lst.index(element)
    except ValueError:
        return -1


def remove_duplicates(lst):
    """
    Удаляет дубликаты из списка, сохраняя порядок элементов
    """
    ls = set()
    lst_1 = list()
    for item in lst:
        if item not in ls:
            lst_1.append(item)
            ls.add(item)
    return lst_1


def merge_lists(list1, list2):
    """
    Объединяет два списка в один, удаляя дубликаты
    """
    ls = set()
    lst_1 = list()
    for item in list1:
        if item not in ls:
            lst_1.append(item)
            ls.add(item)
    for item in list2:
        if item not in ls:
            lst_1.append(item)
            ls.add(item)
    return lst_1


def list_intersection(list1, list2):
    """
    Возвращает список элементов, которые есть в обоих списках
    """
    ls1, ls2 = set(list1), set(list2)
    return list(ls1.intersection(ls2))


def list_difference(list1, list2):
    """
    Возвращает список элементов, которые есть в list1, но отсутствуют в list2
    """
    ls1, ls2 = set(list1), set(list2)
    return list(ls1.difference(ls2))


def flatten_list(nested_list):
    """
    Преобразует вложенный список в плоский
    Например, [1, [2, 3], [4, [5, 6]]] -> [1, 2, 3, 4, 5, 6]
    """
    ls = list()
    for item in nested_list:
        if isinstance(item, list):
            ls.extend(flatten_list(item))
        else:
            ls.append(item)
    return ls
