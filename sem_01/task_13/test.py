import pytest
import os
import tempfile
from solution import (
    write_to_file,
    append_to_file,
    write_lines_to_file,
    copy_file,
    save_dict_to_file,
    save_list_to_file,
    save_table_to_file,
)


# Используем временные файлы для тестирования
@pytest.fixture
def temp_file():
    fd, path = tempfile.mkstemp()
    yield path
    os.close(fd)
    if os.path.exists(path):
        os.remove(path)


@pytest.fixture
def temp_source_file():
    fd, path = tempfile.mkstemp()
    with open(path, "w") as f:
        f.write("Исходный файл для тестирования копирования")
    yield path
    os.close(fd)
    if os.path.exists(path):
        os.remove(path)


def test_write_to_file(temp_file):
    content = "Тестовая строка"
    write_to_file(temp_file, content)

    with open(temp_file, "r") as f:
        result = f.read()

    assert result == content, "Содержимое файла должно быть 'Тестовая строка'"

    # Проверка перезаписи
    new_content = "Новая строка"
    write_to_file(temp_file, new_content)

    with open(temp_file, "r") as f:
        result = f.read()

    assert (
        result == new_content
    ), "Содержимое файла должно быть перезаписано на 'Новая строка'"


def test_append_to_file(temp_file):
    initial_content = "Первая строка\n"
    with open(temp_file, "w") as f:
        f.write(initial_content)

    append_content = "Вторая строка"
    append_to_file(temp_file, append_content)

    with open(temp_file, "r") as f:
        result = f.read()

    assert (
        result == initial_content + append_content
    ), "Содержимое файла должно быть 'Первая строка\\nВторая строка'"


def test_write_lines_to_file(temp_file):
    lines = ["Строка 1", "Строка 2", "Строка 3"]
    write_lines_to_file(temp_file, lines)

    with open(temp_file, "r") as f:
        result = f.read().splitlines()

    assert result == lines, "Файл должен содержать строки из списка"


def test_copy_file(temp_source_file, temp_file):
    copy_file(temp_source_file, temp_file)

    with open(temp_source_file, "r") as source:
        source_content = source.read()

    with open(temp_file, "r") as dest:
        dest_content = dest.read()

    assert dest_content == source_content, "Содержимое файлов должно совпадать"


def test_save_dict_to_file(temp_file):
    dictionary = {"key1": "value1", "key2": "value2", "key3": "value3"}
    save_dict_to_file(temp_file, dictionary)

    with open(temp_file, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) == len(
        dictionary
    ), "Количество строк должно соответствовать количеству пар в словаре"

    for line in lines:
        key, value = line.split(": ")
        assert (
            dictionary[key] == value
        ), f"Пара ключ-значение {key}: {value} должна быть в файле"


def test_save_list_to_file(temp_file):
    lst = ["элемент1", "элемент2", "элемент3"]
    save_list_to_file(temp_file, lst)

    with open(temp_file, "r") as f:
        lines = f.read().splitlines()

    assert lines == lst, "Строки в файле должны соответствовать элементам списка"


def test_save_table_to_file(temp_file):
    table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    save_table_to_file(temp_file, table)

    with open(temp_file, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) == len(
        table
    ), "Количество строк должно соответствовать количеству строк в таблице"

    for i, line in enumerate(lines):
        values = line.split(",")
        assert [int(val) for val in values] == table[
            i
        ], f"Строка {i+1} должна содержать значения {table[i]}"


if __name__ == "__main__":
    pytest.main()
