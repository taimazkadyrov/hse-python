import pytest
from solution import get_variables


def test_variables():
    # Получаем переменные из решения
    (
        integer_number,
        float_number,
        string_value,
        boolean_true,
        boolean_false,
        list_of_numbers,
        dictionary,
    ) = get_variables()

    # Проверяем типы и значения
    assert isinstance(integer_number, int), "integer_number должен быть целым числом"

    assert isinstance(
        float_number, float
    ), "float_number должен быть числом с плавающей точкой"

    assert isinstance(string_value, str), "string_value должен быть строкой"
    assert len(string_value) > 0, "string_value не должен быть пустой строкой"

    assert isinstance(
        boolean_true, bool
    ), "boolean_true должен быть логическим значением"
    assert boolean_true is True, "boolean_true должен быть True"

    assert isinstance(
        boolean_false, bool
    ), "boolean_false должен быть логическим значением"
    assert boolean_false is False, "boolean_false должен быть False"

    assert isinstance(list_of_numbers, list), "list_of_numbers должен быть списком"
    assert list_of_numbers == [
        1,
        2,
        3,
        4,
        5,
    ], "list_of_numbers должен содержать числа от 1 до 5"

    assert isinstance(dictionary, dict), "dictionary должен быть словарем"
    assert "name" in dictionary, "dictionary должен содержать ключ 'name'"
    assert "age" in dictionary, "dictionary должен содержать ключ 'age'"
    assert isinstance(
        dictionary["name"], str
    ), "Значение ключа 'name' должно быть строкой"
    assert isinstance(
        dictionary["age"], int
    ), "Значение ключа 'age' должно быть целым числом"


if __name__ == "__main__":
    pytest.main()
