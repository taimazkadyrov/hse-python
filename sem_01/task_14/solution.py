# Задание 14: Обработка исключений
# Реализуйте функции с использованием обработки исключений


def safe_divide(a, b):
    """
    Безопасное деление a на b
    Если b равно 0, возвращает None вместо вызова исключения
    """
    # Ваш код здесь
    pass


def safe_list_get(lst, index, default=None):
    """
    Безопасное получение элемента списка по индексу
    Если индекс за пределами списка, возвращает default
    """
    # Ваш код здесь
    pass


def safe_dict_get(dictionary, key, default=None):
    """
    Безопасное получение значения из словаря по ключу
    Если ключ отсутствует, возвращает default
    """
    # Ваш код здесь
    pass


def safe_file_read(file_path, default=""):
    """
    Безопасное чтение файла
    Если файл не существует или не может быть прочитан, возвращает default
    """
    # Ваш код здесь
    pass


def safe_json_parse(json_string, default=None):
    """
    Безопасный парсинг JSON-строки
    Если строка не является корректным JSON, возвращает default
    """
    # Ваш код здесь
    pass


def safe_type_convert(value, target_type, default=None):
    """
    Безопасное преобразование value к типу target_type
    Если преобразование невозможно, возвращает default

    Пример использования:
    safe_type_convert("123", int) -> 123
    safe_type_convert("abc", int) -> None
    """
    # Ваш код здесь
    pass


def retry_operation(operation, max_attempts=3):
    """
    Выполняет функцию operation с повторными попытками в случае исключения
    Возвращает результат успешного выполнения или None, если все попытки неудачны

    Параметры:
    - operation: функция без аргументов, которую нужно выполнить
    - max_attempts: максимальное количество попыток
    """
    # Ваш код здесь
    pass
