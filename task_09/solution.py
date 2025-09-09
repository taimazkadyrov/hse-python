# Задание 9: Словари
# Реализуйте функции для работы со словарями


def create_person(name, age, city):
    """
    Создает и возвращает словарь, представляющий человека
    с ключами 'name', 'age', 'city'
    """
    return {"name": name, "age": age, "city": city}


def get_value(dictionary, key, default=None):
    """
    Возвращает значение из словаря по ключу
    Если ключ отсутствует, возвращает default
    """
    if key not in dictionary:
        return default
    else:
        return dictionary[key]


def update_dict(dictionary, key, value):
    """
    Обновляет словарь, добавляя или изменяя пару ключ-значение
    Возвращает обновленный словарь
    """
    dictionary[key] = value
    return dictionary


def merge_dicts(dict1, dict2):
    """
    Объединяет два словаря в один новый
    Если ключи повторяются, значения из dict2 имеют приоритет
    """
    dict3 = dict1.copy()
    dict3.update(dict2)
    return dict3

def invert_dict(dictionary):
    """
    Создает новый словарь, где ключи и значения поменяны местами
    Предполагается, что значения в исходном словаре уникальны
    """
    return {value: key for key, value in dictionary.items()}


def count_words(text):
    """
    Подсчитывает количество вхождений каждого слова в тексте
    Возвращает словарь, где ключи - слова, значения - количество вхождений
    Слова приводятся к нижнему регистру и очищаются от знаков препинания
    """
    for znaki in ",.1!?:;":
        text = text.replace(znaki, "")
    lst = text.lower().split()
    dic = {}
    for item in lst:
        dic[item] = dic.get(item, 0) + 1
    return dic




def filter_by_value(dictionary, condition):
    """
    Фильтрует словарь по значению, используя функцию condition
    Возвращает новый словарь с парами, для которых condition(value) == True

    Пример использования:
    filter_by_value({'a': 1, 'b': 2, 'c': 3}, lambda x: x > 1)
    Вернет: {'b': 2, 'c': 3}
    """
    dict1 = {}
    for key, value in dictionary.items():
        if condition(value):
            dict1[key] = value
    return dict1
