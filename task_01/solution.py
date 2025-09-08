# Задание 1: Переменные и типы данных
# Заполните переменные согласно их описанию


def get_variables():
    # Целое число
    integer_number = 52

    # Число с плавающей точкой
    float_number = 14.88

    # Строка
    string_value = "Санкт-Петербург"

    # Логическое значение (истина)
    boolean_true = True

    # Логическое значение (ложь)
    boolean_false = False

    # Список из чисел от 1 до 5
    list_of_numbers = [i for i in range(1, 6)]

    # Словарь с ключами 'name' и 'age', и соответствующими значениями
    dictionary = {"name": "Taimaz", "age": 18}

    # Вернуть все переменные в виде кортежа
    return (
        integer_number,
        float_number,
        string_value,
        boolean_true,
        boolean_false,
        list_of_numbers,
        dictionary,
    )
