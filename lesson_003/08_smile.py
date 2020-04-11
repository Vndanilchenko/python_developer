# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

for i in range(10):
    rand = sd.random_number(50, 300)
    point = sd.get_point(rand, rand)
    sd.circle(center_position=point, radius=50)

    point_left = sd.get_point(rand-25, rand+25)
    point_right = sd.get_point(rand+25, rand+25)
    sd.circle(center_position=point_left, radius=10)
    sd.circle(center_position=point_right, radius=10)

    point_left_lips = sd.get_point(rand-25, rand-25)
    # point_left_lips = sd.get_point(20, 30)
    # point_right_lips = sd.get_point(30, 30)
    sd.vector(start=point_left_lips, angle = 0, length=50)

sd.pause()
# зачет!