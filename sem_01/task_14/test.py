import pytest
import json
import os
import tempfile
from .solution import (
    safe_divide,
    safe_list_get,
    safe_dict_get,
    safe_file_read,
    safe_json_parse,
    safe_type_convert,
    retry_operation,
)


def test_safe_divide():
    assert safe_divide(10, 2) == 5, "10 / 2 должно быть 5"
    assert safe_divide(10, 0) is None, "Деление на 0 должно возвращать None"
    assert safe_divide(0, 5) == 0, "0 / 5 должно быть 0"


def test_safe_list_get():
    lst = [1, 2, 3, 4, 5]
    assert safe_list_get(lst, 2) == 3, "Элемент с индексом 2 должен быть 3"
    assert (
        safe_list_get(lst, 10) is None
    ), "Доступ к несуществующему индексу должен возвращать None"
    assert safe_list_get(lst, -1) == 5, "Элемент с индексом -1 должен быть 5"
    assert (
        safe_list_get(lst, 10, "default") == "default"
    ), "Должно возвращать указанное значение по умолчанию"
    assert (
        safe_list_get([], 0) is None
    ), "Доступ к пустому списку должен возвращать None"


def test_safe_dict_get():
    d = {"a": 1, "b": 2, "c": 3}
    assert safe_dict_get(d, "a") == 1, "Значение для ключа 'a' должно быть 1"
    assert (
        safe_dict_get(d, "d") is None
    ), "Доступ к несуществующему ключу должен возвращать None"
    assert (
        safe_dict_get(d, "d", "default") == "default"
    ), "Должно возвращать указанное значение по умолчанию"
    assert (
        safe_dict_get({}, "a") is None
    ), "Доступ к пустому словарю должен возвращать None"


def test_safe_file_read():
    # Создаем временный файл для тестирования
    fd, path = tempfile.mkstemp()
    try:
        with os.fdopen(fd, "w") as tmp:
            tmp.write("Тестовое содержимое файла")

        # Тест чтения существующего файла
        content = safe_file_read(path)
        assert content == "Тестовое содержимое файла", "Должно вернуть содержимое файла"

        # Тест чтения несуществующего файла
        non_existent_path = path + "_non_existent"
        assert (
            safe_file_read(non_existent_path) == ""
        ), "Для несуществующего файла должна вернуться пустая строка"
        assert (
            safe_file_read(non_existent_path, "default") == "default"
        ), "Должно вернуться указанное значение по умолчанию"
    finally:
        os.remove(path)


def test_safe_json_parse():
    valid_json = '{"name": "John", "age": 30}'
    invalid_json = '{"name": "John", "age": 30'

    assert safe_json_parse(valid_json) == {
        "name": "John",
        "age": 30,
    }, "Должен корректно парсить JSON"
    assert (
        safe_json_parse(invalid_json) is None
    ), "Для некорректного JSON должен возвращаться None"
    assert (
        safe_json_parse(invalid_json, {}) == {}
    ), "Должно возвращаться указанное значение по умолчанию"
    assert safe_json_parse("") is None, "Для пустой строки должен возвращаться None"


def test_safe_type_convert():
    assert (
        safe_type_convert("123", int) == 123
    ), "Строка '123' должна быть преобразована в число 123"
    assert (
        safe_type_convert("abc", int) is None
    ), "Невозможное преобразование должно возвращать None"
    assert (
        safe_type_convert("abc", int, 0) == 0
    ), "Должно возвращаться указанное значение по умолчанию"
    assert (
        safe_type_convert(123, str) == "123"
    ), "Число 123 должно быть преобразовано в строку '123'"
    assert (
        safe_type_convert("True", bool) is True
    ), "Строка 'True' должна быть преобразована в True"


def test_retry_operation():
    # Функция, которая всегда успешна
    def successful_operation():
        return "success"

    # Функция, которая всегда вызывает исключение
    def failing_operation():
        raise ValueError("Operation failed")

    # Функция, которая успешна только с третьей попытки
    attempt_count = [0]

    def eventually_successful_operation():
        attempt_count[0] += 1
        if attempt_count[0] < 3:
            raise ValueError("Operation failed")
        return "success after retries"

    assert (
        retry_operation(successful_operation) == "success"
    ), "Успешная операция должна вернуть результат"
    assert (
        retry_operation(failing_operation) is None
    ), "После всех неудачных попыток должен вернуться None"
    assert (
        retry_operation(eventually_successful_operation) == "success after retries"
    ), "Операция должна быть успешной после повторных попыток"


if __name__ == "__main__":
    pytest.main()
