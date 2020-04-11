# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

point = sd.get_point(sd.resolution[0]/2, sd.resolution[1]/2)

# треугольник
def triangle(point = point,  angle = 10, length = 100, color = sd.COLOR_DARK_CYAN):
    v1 = sd.get_vector(point, angle, length)
    v2 = sd.get_vector(v1.end_point, v1.angle + 360/3, length)
    v3 = sd.get_vector(v2.end_point, v2.angle + 360/3, length)
    sd.line(point, v1.end_point, color=color)
    sd.line(v2.start_point, v2.end_point, color=color)
    sd.line(v3.start_point, v3.end_point, color=color)

# квадрат
def square(point=point, angle=10, length=100, color = sd.COLOR_DARK_CYAN):
    v1 = sd.get_vector(point, angle, length)
    v2 = sd.get_vector(v1.end_point, v1.angle + 360/4, length)
    v3 = sd.get_vector(v2.end_point, v2.angle + 360/4, length)
    v4 = sd.get_vector(v3.end_point, v3.angle + 360/4, length)
    sd.line(point, v1.end_point, color=color)
    sd.line(v2.start_point, v2.end_point, color=color)
    sd.line(v3.start_point, v3.end_point, color=color)
    sd.line(v4.start_point, v4.end_point, color=color)

# пятиугольник
def pentagon(point=point, angle=10, length=100, color = sd.COLOR_DARK_CYAN):
    v1 = sd.get_vector(point, angle, length)
    v2 = sd.get_vector(v1.end_point, v1.angle + 360/5, length)
    v3 = sd.get_vector(v2.end_point, v2.angle + 360/5, length)
    v4 = sd.get_vector(v3.end_point, v3.angle + 360/5, length)
    v5 = sd.get_vector(v4.end_point, v4.angle + 360/5, length)
    sd.line(point, v1.end_point, color=color)
    sd.line(v2.start_point, v2.end_point, color=color)
    sd.line(v3.start_point, v3.end_point, color=color)
    sd.line(v4.start_point, v4.end_point, color=color)
    sd.line(v5.start_point, v5.end_point, color=color)

# шестиугольник
def hexagon(point=point, angle=10, length=100, color = sd.COLOR_DARK_CYAN):
    v1 = sd.get_vector(point, angle, length)
    v2 = sd.get_vector(v1.end_point, v1.angle + 360/6, length)
    v3 = sd.get_vector(v2.end_point, v2.angle + 360/6, length)
    v4 = sd.get_vector(v3.end_point, v3.angle + 360/6, length)
    v5 = sd.get_vector(v4.end_point, v4.angle + 360/6, length)
    v6 = sd.get_vector(v5.end_point, v5.angle + 360/6, length)
    sd.line(point, v1.end_point, color=color)
    sd.line(v2.start_point, v2.end_point, color=color)
    sd.line(v3.start_point, v3.end_point, color=color)
    sd.line(v4.start_point, v4.end_point, color=color)
    sd.line(v5.start_point, v5.end_point, color=color)
    sd.line(v6.start_point, v6.end_point, color=color)

print('возможные фигуры: \n 0 : треугольник \n 1 : квадрат \n 2 : пятиугольник \n 3 : шестиугольник')

shape_input = int(input('введите желаемую фигуру >'))
while shape_input>3 or shape_input < 0:
    shape_input = int(input('Вы ввели некорректный номер \n введите желаемую фигуру >'))

figures = [triangle, square, pentagon, hexagon]
figures[shape_input]()

sd.pause()
# зачет!