import pytest
import os
from .solution import (
    read_file_content,
    count_lines,
    count_words,
    find_word,
    get_line_by_number,
    get_longest_line,
    get_most_common_word,
)

# Путь к тестовому файлу
TEST_FILE = os.path.join(os.path.dirname(__file__), "test_file.txt")


def test_read_file_content():
    content = read_file_content(TEST_FILE)
    assert isinstance(content, str), "Содержимое файла должно быть строкой"
    assert (
        "Это первая строка файла." in content
    ), "Содержимое файла должно включать первую строку"
    assert (
        "Файл содержит разные слова" in content
    ), "Содержимое файла должно включать последнюю строку"


def test_count_lines():
    lines_count = count_lines(TEST_FILE)
    assert lines_count == 8, "Файл должен содержать 8 строк"


def test_count_words():
    words_count = count_words(TEST_FILE)
    assert words_count == 74, "Файл должен содержать 74 слова"


def test_find_word():
    assert (
        find_word(TEST_FILE, "файл") == True
    ), "Слово 'файл' должно быть найдено в файле"
    assert (
        find_word(TEST_FILE, "программирование") == False
    ), "Слово 'программирование' не должно быть найдено в файле"
    assert find_word(TEST_FILE, "Файл") == True, "Поиск должен быть регистронезависимым"


def test_get_line_by_number():
    line = get_line_by_number(TEST_FILE, 1)
    assert (
        line == "Это первая строка файла."
    ), "Первая строка должна быть 'Это первая строка файла.'"

    line = get_line_by_number(TEST_FILE, 4)
    assert (
        "самая длинная строка" in line
    ), "Четвертая строка должна содержать 'самая длинная строка'"

    line = get_line_by_number(TEST_FILE, 100)
    assert line is None, "При запросе несуществующей строки должен возвращаться None"


def test_get_longest_line():
    longest_line = get_longest_line(TEST_FILE)
    assert (
        "самая длинная строка" in longest_line
    ), "Самая длинная строка должна содержать 'самая длинная строка'"
    assert len(longest_line) == 85, "Длина самой длинной строки должна быть 85 символов"


def test_get_most_common_word():
    common_word, count = get_most_common_word(TEST_FILE)
    assert common_word.lower() == "файл", "Самое частое слово должно быть 'файл'"
    assert count == 8, "Слово 'файл' должно встречаться 8 раз"


if __name__ == "__main__":
    pytest.main()
