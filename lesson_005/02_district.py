# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1 import room1 as rm1, room2 as rm2
from district.central_street.house2 import room1 as rm3, room2 as rm4
from district.soviet_street.house1 import room1 as rm5, room2 as rm6
from district.soviet_street.house2 import room1 as rm7, room2 as rm8

print((', ').join(rm1.folks + rm2.folks + rm3.folks + rm4.folks + rm5.folks + rm6.folks + rm7.folks + rm8.folks))

# зачет!