# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(sd.resolution[0]/2, sd.resolution[1]/2)

sd.circle(center_position = point, radius = 100)
sd.circle(center_position = point, radius = 95)
sd.circle(center_position = point, radius = 90)

# Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point = (100, 100), step = 50):
    sd.circle(center_position=sd.get_point(point[0], point[1]), radius=step)

bubble((100, 100), 10)


# Нарисовать 10 пузырьков в ряд
for i in range(10):
    bubble((40*(1+i), 200), 20)

# Нарисовать три ряда по 10 пузырьков
for i in range(3):
    for j in range(10):
        bubble((100*(1+j), 100*(1+i)), 50)


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
#
for i in range(100):
    sd.circle(sd.random_point(), radius=sd.random_number(20, 100), color=sd.random_color())

sd.pause()
# зачет!

