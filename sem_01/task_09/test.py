import pytest
from solution import (
    create_person,
    get_value,
    update_dict,
    merge_dicts,
    invert_dict,
    count_words,
    filter_by_value,
)


def test_create_person():
    person = create_person("Иван", 25, "Москва")
    assert isinstance(person, dict), "Функция должна возвращать словарь"
    assert person["name"] == "Иван", "Имя должно быть 'Иван'"
    assert person["age"] == 25, "Возраст должен быть 25"
    assert person["city"] == "Москва", "Город должен быть 'Москва'"


def test_get_value():
    dictionary = {"a": 1, "b": 2, "c": 3}
    assert get_value(dictionary, "a") == 1, "Значение для ключа 'a' должно быть 1"
    assert (
        get_value(dictionary, "d") is None
    ), "Значение для отсутствующего ключа должно быть None"
    assert (
        get_value(dictionary, "d", "default") == "default"
    ), "Значение для отсутствующего ключа должно быть 'default'"


def test_update_dict():
    dictionary = {"a": 1, "b": 2}
    updated = update_dict(dictionary, "c", 3)
    assert updated == {
        "a": 1,
        "b": 2,
        "c": 3,
    }, "Словарь должен быть обновлен с новым ключом"

    updated = update_dict(dictionary, "a", 10)
    assert updated == {
        "a": 10,
        "b": 2,
        "c": 3,
    }, "Значение для существующего ключа должно быть обновлено"

    # Проверяем, что исходный словарь тоже изменился
    assert dictionary == {
        "a": 10,
        "b": 2,
        "c": 3,
    }, "Исходный словарь должен быть изменен"


def test_merge_dicts():
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    merged = merge_dicts(dict1, dict2)

    assert merged == {
        "a": 1,
        "b": 3,
        "c": 4,
    }, "Словари должны быть объединены с приоритетом значений из dict2"

    # Проверяем, что исходные словари не изменились
    assert dict1 == {"a": 1, "b": 2}, "Исходный словарь dict1 не должен быть изменен"
    assert dict2 == {"b": 3, "c": 4}, "Исходный словарь dict2 не должен быть изменен"


def test_invert_dict():
    dictionary = {"a": 1, "b": 2, "c": 3}
    inverted = invert_dict(dictionary)

    assert inverted == {
        1: "a",
        2: "b",
        3: "c",
    }, "Ключи и значения должны быть поменяны местами"

    # Проверяем, что исходный словарь не изменился
    assert dictionary == {
        "a": 1,
        "b": 2,
        "c": 3,
    }, "Исходный словарь не должен быть изменен"


def test_count_words():
    text = "Привет, мир! Привет, Python!"
    word_count = count_words(text)

    assert word_count == {
        "привет": 2,
        "мир": 1,
        "python": 1,
    }, "Неправильный подсчет слов"

    text = "a a a b b c"
    word_count = count_words(text)

    assert word_count == {"a": 3, "b": 2, "c": 1}, "Неправильный подсчет слов"

    text = ""
    word_count = count_words(text)

    assert word_count == {}, "Для пустого текста должен возвращаться пустой словарь"


def test_filter_by_value():
    dictionary = {"a": 1, "b": 2, "c": 3, "d": 4}

    filtered = filter_by_value(dictionary, lambda x: x > 2)
    assert filtered == {"c": 3, "d": 4}, "Должны остаться только пары со значениями > 2"

    filtered = filter_by_value(dictionary, lambda x: x % 2 == 0)
    assert filtered == {
        "b": 2,
        "d": 4,
    }, "Должны остаться только пары с четными значениями"

    filtered = filter_by_value(dictionary, lambda x: x > 10)
    assert (
        filtered == {}
    ), "Для условия, которому не удовлетворяет ни одно значение, должен возвращаться пустой словарь"

    # Проверяем, что исходный словарь не изменился
    assert dictionary == {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
    }, "Исходный словарь не должен быть изменен"


if __name__ == "__main__":
    pytest.main()
