#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продукты следующего вида (писать прямо в коде)
# sweets = {
#     'название сладости': [
#         {'shop': 'название магазина', 'price': 99.99},
#         #  тут с клавиатуры введите магазины и цены (можно копипастить ;)
#     ],
#     #  тут с клавиатуры введите другую сладость и далее словарь магазинов
# }

sweets = {
    'печенье': [
        {'shop': 'ашан', 'price': 10.99},
        {'shop': 'пятерочка', 'price': 9.99},
        {'shop': 'магнит', 'price': 11.99}
    ],
    'конфеты': [
        {'shop': 'ашан', 'price': 34.99},
        {'shop': 'пятерочка', 'price': 32.99},
        {'shop': 'магнит', 'price': 30.99}
    ],
    'карамель': [
        {'shop': 'ашан', 'price': 45.99},
        {'shop': 'пятерочка', 'price': 46.99},
        {'shop': 'магнит', 'price': 41.99}
    ],
    'пирожное': [
        {'shop': 'ашан', 'price': 67.99},
        {'shop': 'пятерочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99}
    ]
}

# Указать надо только по 2 магазина с минимальными ценами

# PS: скорее всего я неправильно понял задание, потому что еще не проходили циклы, но по-другому не пойму что делать - вручную просто записать чтоли?!..
# в общем, вывел по два магазина на продукт по убыванию цены (работает только для не более 3х магазинов на продукт)
prices = {}
shops = {}
for sweet in sweets:
    min_price = 100000000000
    prices[sweet] = []
    shops[sweet] = []
    for elem in range(3):
        if sweets[sweet][elem]['price'] < min_price:
            min_price = sweets[sweet][elem]['price']
            prices[sweet].insert(0, sweets[sweet][elem]['price'])
            shops[sweet].insert(0, sweets[sweet][elem]['shop'])
        elif sweets[sweet][elem]['price'] >= prices[sweet][-1] and elem>0:
            prices[sweet].insert(len(prices[sweet]), sweets[sweet][elem]['price'])
            shops[sweet].insert(len(shops[sweet]), sweets[sweet][elem]['shop'])
        else:
            prices[sweet].insert(1, sweets[sweet][elem]['price'])
            shops[sweet].insert(1, sweets[sweet][elem]['shop'])

for key in shops.keys():
    print(f'минимальные цены на {key} в магазине {shops[key][0]} : {prices[key][0]} и {shops[key][1]} : {prices[key][1]}')

# зачет будем считать