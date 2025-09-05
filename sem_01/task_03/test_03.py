import pytest
from .solution import (
    string_length,
    string_concatenation,
    string_to_uppercase,
    string_to_lowercase,
    string_replace,
    string_split,
    string_strip,
    is_palindrome,
)


def test_string_length():
    assert string_length("Python") == 6, "Длина строки 'Python' должна быть 6"
    assert string_length("") == 0, "Длина пустой строки должна быть 0"
    assert string_length(" ") == 1, "Длина строки с одним пробелом должна быть 1"


def test_string_concatenation():
    assert (
        string_concatenation("Hello, ", "World!") == "Hello, World!"
    ), "Конкатенация 'Hello, ' и 'World!' должна дать 'Hello, World!'"
    assert (
        string_concatenation("", "Python") == "Python"
    ), "Конкатенация пустой строки и 'Python' должна дать 'Python'"
    assert (
        string_concatenation("123", "456") == "123456"
    ), "Конкатенация '123' и '456' должна дать '123456'"


def test_string_to_uppercase():
    assert (
        string_to_uppercase("python") == "PYTHON"
    ), "'python' в верхнем регистре должно быть 'PYTHON'"
    assert (
        string_to_uppercase("Python") == "PYTHON"
    ), "'Python' в верхнем регистре должно быть 'PYTHON'"
    assert (
        string_to_uppercase("") == ""
    ), "Пустая строка в верхнем регистре должна остаться пустой"


def test_string_to_lowercase():
    assert (
        string_to_lowercase("PYTHON") == "python"
    ), "'PYTHON' в нижнем регистре должно быть 'python'"
    assert (
        string_to_lowercase("Python") == "python"
    ), "'Python' в нижнем регистре должно быть 'python'"
    assert (
        string_to_lowercase("") == ""
    ), "Пустая строка в нижнем регистре должна остаться пустой"


def test_string_replace():
    assert (
        string_replace("Hello, World!", "World", "Python") == "Hello, Python!"
    ), "Замена 'World' на 'Python' в 'Hello, World!'"
    assert (
        string_replace("abcabc", "a", "x") == "xbcxbc"
    ), "Замена всех 'a' на 'x' в 'abcabc'"
    assert (
        string_replace("Python", "z", "y") == "Python"
    ), "Если заменяемой подстроки нет, строка не должна измениться"


def test_string_split():
    assert string_split("a,b,c", ",") == [
        "a",
        "b",
        "c",
    ], "Разделение 'a,b,c' по запятой должно дать ['a', 'b', 'c']"
    assert string_split("Python", "") == [
        "P",
        "y",
        "t",
        "h",
        "o",
        "n",
    ], "Разделение 'Python' по пустой строке должно дать список символов"
    assert string_split("a b c", " ") == [
        "a",
        "b",
        "c",
    ], "Разделение 'a b c' по пробелу должно дать ['a', 'b', 'c']"


def test_string_strip():
    assert (
        string_strip("  Python  ") == "Python"
    ), "Удаление пробелов из '  Python  ' должно дать 'Python'"
    assert (
        string_strip("Python") == "Python"
    ), "Строка без пробелов по краям не должна измениться"
    assert string_strip("   ") == "", "Строка только из пробелов должна стать пустой"


def test_is_palindrome():
    assert is_palindrome("level") == True, "'level' - это палиндром"
    assert (
        is_palindrome("A man a plan a canal Panama") == True
    ), "'A man a plan a canal Panama' - это палиндром (без учета пробелов и регистра)"
    assert (
        is_palindrome("race car") == True
    ), "'race car' - это палиндром (без учета пробелов)"
    assert is_palindrome("hello") == False, "'hello' - это не палиндром"
    assert is_palindrome("") == True, "Пустая строка считается палиндромом"
    assert is_palindrome("a") == True, "Строка из одного символа - палиндром"


if __name__ == "__main__":
    pytest.main()
