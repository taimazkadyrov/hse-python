# Задание 5: Циклы (for)
# Реализуйте функции с использованием цикла for


def sum_of_numbers(n):
    """
    Возвращает сумму чисел от 1 до n включительно
    """
    x = 0
    for i in range(1, n + 1):
        x += i
    return x


def factorial(n):
    """
    Возвращает факториал числа n (произведение чисел от 1 до n)
    Для n <= 1 возвращает 1
    """
    x = 1
    if n <= 1:
        return 1
    else:
        for i in range(1, n + 1):
            x *= i
    return x


def count_vowels(s):
    """
    Возвращает количество гласных букв в строке s
    Гласные: 'a', 'e', 'i', 'o', 'u' (регистр не имеет значения)
    """
    return sum(1 for th in s.lower() if th in "aeiou")


def find_max(numbers):
    """
    Возвращает максимальное число из списка numbers
    Если список пуст, возвращает None
    """
    return max(numbers) if numbers else None


def filter_even_numbers(numbers):
    """
    Возвращает новый список, содержащий только четные числа из списка numbers
    """
    lok = list()
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            lok.append(numbers[i])
    return lok


def generate_multiplication_table(n):
    """
    Возвращает таблицу умножения размером n x n в виде списка списков
    Например, для n=3 результат должен быть:
    [
        [1, 2, 3],
        [2, 4, 6],
        [3, 6, 9]
    ]
    """
    x = list()
    for i in range(1, n + 1):
        lk = list()
        for j in range(1, n + 1):
            lk.append(i * j)
        x.append(lk)
    return x
