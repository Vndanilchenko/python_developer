# -*- coding: utf-8 -*-
import random

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


exceptions = [IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError]

def one_day():
    rnd_death = random.randint(1, 13)
    if rnd_death == 13:
        try:
            raise random.choice(exceptions)
        except IamGodError:
            print('возомнил себя богом и глупо умер')
        except DrunkError:
            print('напился до смерти')
        except CarCrashError:
            print('разбился в атокатастрофе')
        except GluttonyError:
            print('объелся до смерти')
        except DepressionError:
            print('умер от депрессии')
        except SuicideError:
            print('покончил жизнь самоубийством')
    return random.randint(1, 7)

summ = 0
day_num = 0
while summ<ENLIGHTENMENT_CARMA_LEVEL:
    day_num += 1
    summ += one_day()
    print('день номер: {}, заработано кармы: {}'.format(day_num, summ))

print(f'{" УРА! ":*^50s}')
print('прожито дней: {}, заработано кармы: {}'.format(day_num, summ))

# зачет!