"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [i**2 for i in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
    if n in (0, 1):
        return False
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def filter_numbers(number_list, type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if type == "odd":
        return list(filter(lambda x: x % 2 != 0, number_list))
    elif type == "even":
        return list(filter(lambda x: x % 2 == 0, number_list))
    else:
        return list(filter(is_prime, number_list))
