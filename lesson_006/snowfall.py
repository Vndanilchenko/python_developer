# -*- coding: utf-8 -*-

import simple_draw as sd

x_list = {}
y_list = {}
points = {}
sf_lengths = {}
sf_a = {}
sf_b = {}
sf_c = {}
snowflakes = {}


def snowfall():
    x = sd.random_number(-300, sd.resolution[0])
    y = 500
    return x, y, sd.get_point(x, y), sd.random_number(15, 40), \
           sd.random_number(1, 100) / 100, sd.random_number(1, 100) / 100, sd.random_number(1, 100) / 100, sd.snowflake


def generate_snowfall():
    qnty_snowflakes = list(range(int(input('введите количеcтво снежинок\n'))))
    for i in qnty_snowflakes:
        x_list[i], y_list[i], points[i], sf_lengths[i], sf_a[i], sf_b[i], sf_c[i], snowflakes[i] = snowfall()
    return qnty_snowflakes, x_list, y_list, points, sf_lengths, sf_a, sf_b, sf_c, snowflakes


def generate_snowfall():
    qnty_snowflakes_original = list(range(int(input('введите количеcтво снежинок\n'))))
    qnty_snowflakes = qnty_snowflakes_original.copy()
    x_list = [sd.random_number(-300, sd.resolution[0]) for _ in qnty_snowflakes]
    y_list = [500 for _ in qnty_snowflakes]
    points = [sd.get_point(x_list[i], y_list[i]) for i in qnty_snowflakes]
    sf_lengths = [sd.random_number(15, 40) for _ in qnty_snowflakes]
    sf_a = [sd.random_number(1, 100) / 100 for _ in qnty_snowflakes]
    sf_b = [sd.random_number(1, 100) / 100 for _ in qnty_snowflakes]
    sf_c = [sd.random_number(1, 100) / 100 for _ in qnty_snowflakes]
    snowflakes = {k: sd.snowflake for k, v in enumerate(qnty_snowflakes)}
    return qnty_snowflakes_original, qnty_snowflakes, x_list, y_list, points, sf_lengths, sf_a, sf_b, sf_c, snowflakes


def move_snowflakes(qnty_snowflakes, x_list, y_list, points, snowflakes, sf_lengths, sf_a, sf_b, sf_c):
    for i in qnty_snowflakes:
        delta_x = sd.random_number(-30, 30)
        delta_y = sd.random_number(0, 30)
        x_list[i] += delta_x
        y_list[i] -= delta_y
        if y_list[i] < 10:
            y_list[i] = 10
        points[i] = sd.get_point(x_list[i], y_list[i])
        sd.start_drawing()
        snowflakes[i](points[i], sf_lengths[i], sd.COLOR_WHITE, sf_a[i], sf_b[i], sf_c[i])
        snowflakes[i](sd.get_point(x_list[i] - delta_x, y_list[i] + delta_y), sf_lengths[i], sd.background_color,
                      sf_a[i], sf_b[i], sf_c[i])


def print_fallen_snowflakes(qnty_snowflakes, y_list):
    for i in qnty_snowflakes:
        if y_list[i] == 10:
            print('снежинка номер {} упала'.format(i))
            qnty_snowflakes.remove(i)
            sd.clear_screen()


def add_new_snowfall_on_free_place(x_list, y_list, points, sf_lengths, sf_a, sf_b, sf_c, snowflakes, new_idx, qnty_snowflakes):
    for i in new_idx:
        x_list[i], y_list[i], points[i], sf_lengths[i], sf_a[i], sf_b[i], sf_c[i], snowflakes[i] = snowfall()
    qnty_snowflakes += list(new_idx)
    return qnty_snowflakes, x_list, y_list, points, sf_lengths, sf_a, sf_b, sf_c, snowflakes