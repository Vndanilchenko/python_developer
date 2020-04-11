# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
from collections import defaultdict
import os

class Count_per_period:

    def __init__(self, filter_value, offset):
        self.path_to_file = os.path.join(os.getcwd(), r'python_base\lesson_009')
        self.nok_per_period = defaultdict(int)
        self.file_to_read = 'events.txt'
        self.file_to_write = 'out.txt'
        self.filter_value = filter_value
        self.offset = offset

    def __str__(self):
        return 'вызван класс {}: группировка по {}, формат {}, результат по документу {} сохранен в файл {}'.format(self.__class__.__name__, self.filter_value, 'без сдвига', self.file_to_read, self.file_to_write)

    def write_to_file(self):
        with open(os.path.join(self.path_to_file, self.file_to_write), mode='w') as f:
            for k, v in self.nok_per_period.items():
                f.write(f'[{k}] {v}\n')

    def read_from_file(self):
        with open(os.path.join(self.path_to_file, self.file_to_read), mode='r') as f:
            for line in f:
                line = line.split('] ')
                if line[1] == self.filter_value:
                    self.nok_per_period[str(line[0][1:self.offset])] += 1

    def call_read_write(self):
        self.read_from_file()
        self.write_to_file()
        print(self.__str__())


class Count_per_minute(Count_per_period):

    def __str__(self):
        return 'вызван класс {}: группировка по {}, формат {}, результат по документу {} сохранен в файл {}'.format(self.__class__.__name__, self.filter_value[:-1], 'минуты', self.file_to_read, self.file_to_write)


class Count_per_hour(Count_per_period):

    def __str__(self):
        return 'вызван класс {}: группировка по {}, формат {}, результат по документу {} сохранен в файл {}'.format(self.__class__.__name__, self.filter_value[:-1], 'часы', self.file_to_read, self.file_to_write)


class Count_per_month(Count_per_period):

    def __str__(self):
        return 'вызван класс {}: группировка по {}, формат {}, результат по документу {} сохранен в файл {}'.format(self.__class__.__name__, self.filter_value[:-1], 'месяца', self.file_to_read, self.file_to_write)


class Count_per_year(Count_per_period):

    def __str__(self):
        return 'вызван класс {}: группировка по {}, формат {}, результат по документу {} сохранен в файл {}'.format(self.__class__.__name__, self.filter_value[:-1], 'года', self.file_to_read, self.file_to_write)


# проверка наличия ключа для группировки
filter_value = input('выберите ключ для группировки: \n1 - OK \n2 - NOK \n')
while int(filter_value) < 1 and int(filter_value) < 2:
    filter_value = input('выберите ключ для группировки: \n1 - OK \n2 - NOK \n')
filter_value = ['OK\n', 'NOK\n'][int(filter_value)-1]

# проверка ввода периода
period = input('выберите период округления: \n1 - минута \n2 - час \n3 - месяц \n4 - год \n')
while int(period) < 1 or int(period) > 4:
    period = input('выберите период округления: \n1 - минута \n2 - час \n3 - месяц \n4 - год \n')

if period == '1':
    count_and_write = Count_per_minute(filter_value=filter_value, offset=-10)
elif period == '2':
    count_and_write = Count_per_hour(filter_value=filter_value, offset=-13)
elif period == '3':
    count_and_write = Count_per_month(filter_value=filter_value, offset=-19)
elif period == '4':
    count_and_write = Count_per_year(filter_value=filter_value, offset=-22)

count_and_write.call_read_write()


# ОФОРМИТЬ КЛАСС

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
# зачет!