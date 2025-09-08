# Задание 3: Строки и операции со строками
# Реализуйте функции для работы со строками


def string_length(s):
    """
    Возвращает длину строки
    """
    return len(s)


def string_concatenation(s1, s2):
    """
    Соединяет две строки
    """
    return s1 + s2


def string_to_uppercase(s):
    """
    Преобразует строку к верхнему регистру
    """
    return s.upper()


def string_to_lowercase(s):
    """
    Преобразует строку к нижнему регистру
    """
    return s.lower()


def string_replace(s, old, new):
    """
    Заменяет в строке s все вхождения подстроки old на new
    """
    return s.replace(old, new)


def string_split(s, delimiter):
    """
    Разбивает строку по указанному разделителю
    """
    if not delimiter:
        return list(s)
    return s.split(delimiter)

def string_strip(s):
    """
    Удаляет начальные и конечные пробелы из строки
    """
    return s.strip()


def is_palindrome(s):
    """
    Проверяет, является ли строка палиндромом
    (читается одинаково слева направо и справа налево)
    Регистр и пробелы не учитываются
    """
    la = s.replace(" ", "").lower()
    return la == la[::-1]
