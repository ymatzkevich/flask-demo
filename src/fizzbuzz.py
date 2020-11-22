from typing import List


def fizzbuzz(number: int) -> str:
    """
    will return:
        "fizz" if number is a multiple of 3
        "buzz" if number is multiple of 5
        "fizzbuzz" if number is a multiple of both
        str(number) otherwise
    :param number:
    :return:
    """
    s = ''
    if number % 3 == 0:
        s += 'fizz'
    if number % 5 == 0:
        s += 'buzz'
    if s == '':
        s = str(number)
    return s


def fizzbuzz_1_to_number(number: int) -> List[str]:
    """
    will return a list of fizzbuzz'd numbers for all integers in  [1, n]
    :param number: integer, must be greater than 0
    :return:
    """
    if number <= 0:
        return []

    return [fizzbuzz(n + 1) for n in range(number)]