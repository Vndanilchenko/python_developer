# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234
#
from collections import defaultdict
import os

class Count_per_period:  # ниже с генератором

    def __init__(self, filter_value, offset):
        self.path_to_file = os.path.join(os.getcwd())#, r'python_base\lesson_011')
        self.nok_per_period = defaultdict(int)
        self.file_to_read = 'events.txt'
        self.file_to_write = 'out.txt'
        self.filter_value = filter_value
        self.offset = offset
        self.i = 0

    def __str__(self):
        return 'вызван класс {}: группировка по {}, формат {}'.format(self.__class__.__name__, self.filter_value, 'без сдвига')

    def read_from_file(self):
        with open(os.path.join(self.path_to_file, self.file_to_read), mode='r') as f:
            for line in f:
                line = line.split('] ')
                if line[1] == self.filter_value:
                    self.nok_per_period[str(line[0][1:self.offset])] += 1

    def __iter__(self):
        self.read_from_file()
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i <= len(self.nok_per_period):
            key = list(self.nok_per_period.keys())[self.i]
            value = self.nok_per_period[key]
            return key, value
        else:
            raise StopIteration()



class Count_per_minute(Count_per_period):

    def __str__(self):
        return 'вызван класс {}: группировка по {}, формат {}'.format(self.__class__.__name__, self.filter_value[:-1], 'минуты')


# grouped_events = Count_per_minute(filter_value='NOK\n', offset=-10)
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')

######################## ГЕНЕРАТОР

nok_per_period = defaultdict(int)  # чтобы не было KeyError
path_to_file = os.path.join(os.getcwd())
file_to_read = 'events.txt'


def count_per_minute():  # будет работать только для упорядоченным по возрастанию значениям
    i=0
    with open(os.path.join(path_to_file, file_to_read), mode='r') as f:
        for line in f:
            line = line.split('] ')
            time_new = str(line[0][1:-10])
            if i == 0:
                time_old = time_new
            if line[1] == 'NOK\n':
                nok_per_period[time_new] += 1
                i += 1
            if time_new > time_old:
                if nok_per_period[time_old] > 0:
                    yield time_old, nok_per_period[time_old]
            time_old = time_new


grouped_events = count_per_minute()
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
# зачет!