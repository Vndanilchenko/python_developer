# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
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
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>

import os
# from collections import defaultdict
import time

def duration(func):
    def surrogate(*args, **qwargs):
        start_time = time.time()
        result = func(*args, **qwargs)
        print(f'затрачено времени(сек): {round(time.time()-start_time, 2)}')
        return result
    return surrogate

class CalculateVolatility():

    def __init__(self, path, filename):
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

@duration
def main():
    path = os.path.join(os.getcwd(), r'trades') # r'..\..\trades' не работает
    volatilities = {}
    for filename in os.listdir(path):
        obj = CalculateVolatility(path, filename)
        volatilities.update(obj.run())

    zeros_list = []
    for name in filter(lambda kv: kv[1] == 0, volatilities.items()):
        zeros_list.append(name[0])
    nonzeros_list = [(k,v) for k,v in sorted(volatilities.items(), key=lambda kv: -kv[1]) if k not in zeros_list]

    i = 0
    for k, v in enumerate(nonzeros_list):
        if i == 0:
            print('Максимальная волатильность:')
        elif i == len(nonzeros_list)-3:
            print('Минимальная волатильность (не нулевая):')
        if k < 3:
            print('{} - {}%'.format(v[0], v[1]))
        if k >= len(nonzeros_list)-3:
            print('{} - {}%'.format(v[0], v[1]))
        else:
            pass
        i += 1
    print('Нулевая волатильность:')
    print(f'{zeros_list}')

if __name__ == '__main__':
    main()
# зачет!