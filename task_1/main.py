import Exceptions
from random import randint, choice
from inspect import isclass


CARMA = 500
EXCEPTIONS = [getattr(Exceptions, x) for x in dir(Exceptions) if isclass(getattr(Exceptions, x))]


def one_day() -> int:
    _curr_carma = randint(1, 8)
    if not randint(0, 10):
        raise choice(EXCEPTIONS)('Не вышло, попробуйте ещё раз')
    return _curr_carma


curr_carma = 0
while curr_carma <= 500:
    try:
        curr_carma += one_day()
    finally:
        print(f'Удалось накопить {curr_carma} кармы.')


