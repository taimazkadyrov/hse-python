# Задание 4: Условные операторы (if-else)
# Реализуйте функции с использованием условных операторов


def is_positive(number):
    """

    """
    return number > 0


def is_even(number):
    """
    Возвращает True, если число четное, иначе False
    """
    return number % 2 == 0


def is_in_range(number, start, end):
    """
    Возвращает True, если число находится в диапазоне [start, end], иначе False
    """
    return start <= number <= end


def max_of_three(a, b, c):
    """
    Возвращает максимальное из трех чисел
    """
    return max(a, b, c)


def fizz_buzz(number):
    """
    Если число делится на 3, возвращает "Fizz"
    Если число делится на 5, возвращает "Buzz"
    Если число делится и на 3, и на 5, возвращает "FizzBuzz"
    Иначе возвращает само число в виде строки
    """
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return str(number)


def grade_converter(score):
    """
    Конвертирует числовую оценку в буквенную:
    90-100: 'A'
    80-89: 'B'
    70-79: 'C'
    60-69: 'D'
    0-59: 'F'
    Если score не в диапазоне 0-100, возвращает 'Invalid score'
    """
    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
