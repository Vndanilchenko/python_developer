# -*- coding: utf-8 -*-
#
#

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# треугольник
def triangle(point = sd.get_point(100, 100),  angle = sd.random_number(0, 360), length = 50):
    v1 = sd.get_vector(point, angle, length)
    v2 = sd.get_vector(v1.end_point, v1.angle + 120, length)
    v3 = sd.get_vector(v2.end_point, v2.angle + 120, length)
    v1.draw()
    v2.draw()
    v3.draw()

triangle(sd.get_point(200, 200), 10, 100)

# квадрат
def square(point=sd.get_point(100, 300), angle=sd.random_number(0, 360), length=50):
    v1 = sd.get_vector(point, angle, length)
    v2 = sd.get_vector(v1.end_point, v1.angle + 90, length)
    v3 = sd.get_vector(v2.end_point, v2.angle + 90, length)
    v4 = sd.get_vector(v3.end_point, v3.angle + 90, length)
    v1.draw()
    v2.draw()
    v3.draw()
    v4.draw()

square(sd.get_point(200, 400), 10, 100)

# пятиугольник
def pentagon(point=sd.get_point(100, 300), angle=sd.random_number(0, 360), length=50):
    v1 = sd.get_vector(point, angle, length)
    v2 = sd.get_vector(v1.end_point, v1.angle + 360/5, length)
    v3 = sd.get_vector(v2.end_point, v2.angle + 360/5, length)
    v4 = sd.get_vector(v3.end_point, v3.angle + 360/5, length)
    v5 = sd.get_vector(v4.end_point, v4.angle + 360/5, length)
    v1.draw()
    v2.draw()
    v3.draw()
    v4.draw()
    v5.draw()

pentagon(sd.get_point(400, 200), 10, 100)

# шестиугольник
def hexagon(point=sd.get_point(300, 100), angle=sd.random_number(0, 360), length=50):
    v1 = sd.get_vector(point, angle, length)
    v2 = sd.get_vector(v1.end_point, v1.angle + 360/6, length)
    v3 = sd.get_vector(v2.end_point, v2.angle + 360/6, length)
    v4 = sd.get_vector(v3.end_point, v3.angle + 360/6, length)
    v5 = sd.get_vector(v4.end_point, v4.angle + 360/6, length)
    v6 = sd.get_vector(v5.end_point, v5.angle + 360/6, length)
    v1.draw()
    v2.draw()
    v3.draw()
    v4.draw()
    v5.draw()
    v6.draw()

hexagon(sd.get_point(400, 400), 200, 100)
# зачет!
# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!

import simple_draw as sd


def shape(point, angle, length, n):
    shape_angle = 360//n
    for i in range(n):
        vector = sd.get_vector(point, angle+shape_angle*i, length)
        point = vector.end_point
        vector.draw()

def triangle(point, angle, length):
    shape(point, angle, length, 3)

def square(point, angle, length):
    shape(point, angle, length, 4)

def pentagon(point, angle, length):
    shape(point, angle, length, 5)

def hexagon(point, angle, length):
    shape(point, angle, length, 6)

triangle(sd.get_point(200, 200), 10, 70)
square(sd.get_point(200, 400), 360, 70)
pentagon(sd.get_point(400, 400), 10, 70)
hexagon(sd.get_point(400, 200), 10, 70)

sd.pause()
