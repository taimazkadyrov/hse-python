# Задание 1: Переменные и типы данных
# Заполните переменные согласно их описанию


def get_variables():
    print(">>> get_variables вызвана из solution.py")
    # Целое число
    integer_number = 23

    # Число с плавающей точкой
    float_number = 2.1

    # Строка
    string_value = "Okak"

    # Логическое значение (истина)
    boolean_true = True

    # Логическое значение (ложь)
    boolean_false = False

    # Список из чисел от 1 до 5
    list_of_numbers = [1, 2, 3, 4, 5]

    # Словарь с ключами 'name' и 'age', и соответствующими значениями
    dictionary = {"name": "Taimaz", "age": "18"}

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
