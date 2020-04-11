# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#

import os
# from collections import defaultdict
from threading import Thread


class CalculateVolatility(Thread):

    def __init__(self, path, filename, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = os.path.join(path, filename)
        self.max_price = {}
        self.min_price = {}
        self.average_price = {}
        self.volatility = {}

    # сравнение максимального и минимального значения для бумаг
    def check_min_max(self, name, price, line):
        if line == 1:
            self.max_price[name] = price
            self.min_price[name] = price
        elif line > 1:
            if price > self.max_price[name]:
                self.max_price[name] = price
            elif price < self.min_price[name]:
                self.min_price[name] = price

    # читает построчно файл и вызывает метод проверки максимального и минимального значения цены
    def read_file(self, filepath):
        with open(filepath, encoding='utf8') as f:
            for i, line in enumerate(f):
                if i > 0:
                    line = line.split(',')
                    # print(line)
                    self.check_min_max(line[0], float(line[2]), i)

    # считает волатильность каждой бумаги и записывает в словарь, в конце сортирует по убыванию
    def calculate_volatility(self):
        for name, max_price in self.max_price.items():
            self.average_price[name] = (max_price + self.min_price[name]) / 2
            if self.average_price[name] == 0:
                self.volatility[name] = 0
            else:
                self.volatility[name] = ((max_price - self.min_price[name]) / self.average_price[name]) * 100

    def run(self):
        self.read_file(self.path)
        self.calculate_volatility()
        return self.volatility


path = os.path.join(os.getcwd(), r'trades')  # r'..\..\trades' не работает
volatilities = {}
for filename in os.listdir(path):
    obj = CalculateVolatility(path, filename)
    obj.start()
    obj.join()  # TODO у вас не получается паралельности - посмотрите на примеры в lesson_012/python_snippets
    volatilities.update(obj.volatility)

filenames = os.listdir(path)
obj1 = CalculateVolatility

zeros_list = []
for name in filter(lambda kv: kv[1] == 0, volatilities.items()):
    zeros_list.append(name[0])
nonzeros_list = [(k, v) for k, v in sorted(volatilities.items(), key=lambda kv: -kv[1]) if k not in zeros_list]

i = 0
for k, v in enumerate(nonzeros_list):
    if i == 0:
        print('Максимальная волатильность:')
    elif i == len(nonzeros_list) - 3:
        print('Минимальная волатильность (не нулевая):')
    if k < 3:
        print('{} - {}%'.format(v[0], v[1]))
    if k >= len(nonzeros_list) - 3:
        print('{} - {}%'.format(v[0], v[1]))
    else:
        pass
    i += 1
print('Нулевая волатильность:')
print(f'{zeros_list}')

# TODO пропала сортировка
# Нулевая волатильность:
# ['O4H9', 'TRH9', 'EDU9', 'JPM9', 'PDU9', 'CLM9', 'EuZ9', 'VIH9', 'RIH0', 'MTM9', 'EuH0', 'RRG9', 'PTU9', 'CYH9']