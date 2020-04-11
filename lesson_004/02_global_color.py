# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

# треугольник
def triangle(point = sd.get_point(100, 100),  angle = 120, length = 50, color = sd.COLOR_DARK_BLUE):
    v1 = sd.get_vector(point, 0, length)
    v2 = sd.get_vector(v1.end_point, v1.angle + angle, length)
    v3 = sd.get_vector(v2.end_point, v2.angle + angle, length)
    sd.line(point, v1.end_point, color=color)
    sd.line(v2.start_point, v2.end_point, color=color)
    sd.line(v3.start_point, v3.end_point, color=color)

# квадрат
def square(point=sd.get_point(100, 300), angle=90, length=50, color = sd.COLOR_DARK_BLUE):
    v1 = sd.get_vector(point, 0, length)
    v2 = sd.get_vector(v1.end_point, v1.angle + angle, length)
    v3 = sd.get_vector(v2.end_point, v2.angle + angle, length)
    v4 = sd.get_vector(v3.end_point, v3.angle + angle, length)
    sd.line(point, v1.end_point, color=color)
    sd.line(v2.start_point, v2.end_point, color=color)
    sd.line(v3.start_point, v3.end_point, color=color)
    sd.line(v4.start_point, v4.end_point, color=color)

# пятиугольник
def pentagon(point=sd.get_point(100, 300), angle=360/5, length=50, color = sd.COLOR_DARK_BLUE):
    v1 = sd.get_vector(point, 0, length)
    v2 = sd.get_vector(v1.end_point, v1.angle + angle, length)
    v3 = sd.get_vector(v2.end_point, v2.angle + angle, length)
    v4 = sd.get_vector(v3.end_point, v3.angle + angle, length)
    v5 = sd.get_vector(v4.end_point, v4.angle + angle, length)
    sd.line(point, v1.end_point, color=color)
    sd.line(v2.start_point, v2.end_point, color=color)
    sd.line(v3.start_point, v3.end_point, color=color)
    sd.line(v4.start_point, v4.end_point, color=color)
    sd.line(v5.start_point, v5.end_point, color=color)

# шестиугольник
def hexagon(point=sd.get_point(300, 100), angle=360/6, length=50, color = sd.COLOR_DARK_BLUE):
    v1 = sd.get_vector(point, 0, length)
    v2 = sd.get_vector(v1.end_point, v1.angle + angle, length)
    v3 = sd.get_vector(v2.end_point, v2.angle + angle, length)
    v4 = sd.get_vector(v3.end_point, v3.angle + angle, length)
    v5 = sd.get_vector(v4.end_point, v4.angle + angle, length)
    v6 = sd.get_vector(v5.end_point, v5.angle + angle, length)
    sd.line(point, v1.end_point, color=color)
    sd.line(v2.start_point, v2.end_point, color=color)
    sd.line(v3.start_point, v3.end_point, color=color)
    sd.line(v4.start_point, v4.end_point, color=color)
    sd.line(v5.start_point, v5.end_point, color=color)
    sd.line(v6.start_point, v6.end_point, color=color)

print('возможные цвета: \n 0 : red \n 1 : orange \n 2 : yellow \n 3 : green \n 4 : cyan \n 5 : blue \n 6 : purple')
color_input = int(input('введите желаемый цвет >'))
while color_input>6 or color_input < 0:
    color_input = int(input('Вы ввели некорректный номер \n введите желаемый цвет >'))

colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]

triangle(sd.get_point(200, 200), 120, 100, colors[color_input])
square(sd.get_point(200, 400), 90, 100, colors[color_input])
pentagon(sd.get_point(400, 200), 360/5, 100, colors[color_input])
hexagon(sd.get_point(400, 400), 360/6, 100, colors[color_input])


sd.pause()
# зачет!