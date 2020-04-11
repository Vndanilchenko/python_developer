# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения
# немного копипасты не помешает)
root_point = sd.get_point(300, 30)
def draw_branches(start_point=root_point, angle=90, length=100):
    if length< 10:
        return
    v1 = sd.get_vector(start_point, angle, length)
    next_point = v1.end_point
    next_angle = v1.angle - 30
    v1.draw()
    v2 = sd.get_vector(start_point, angle, length)
    next_point2 = v2.end_point
    next_angle2 = v2.angle + 30
    v2.draw()
    next_length = length * 0.75
    draw_branches(next_point, next_angle, next_length)
    draw_branches(next_point2, next_angle2, next_length)



length = 100
angle = 90

draw_branches(root_point, angle, length)
draw_branches(root_point, angle, length)

#     length *= 0.75

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

def draw_branches2(start_point=root_point, angle=90, length=100):
    if length< 10:
        return
    v1 = sd.get_vector(start_point, angle, length)
    next_point = v1.end_point
    next_angle = angle - (30 + sd.random_number(-40, 40)/100)
    v1.draw()
    v2 = sd.get_vector(start_point, angle, length)
    next_point2 = v2.end_point
    next_angle2 = angle + (30 + sd.random_number(-40, 40)/100)
    v2.draw()
    next_length = length * (0.75 + sd.random_number(-20, 20)/100)
    draw_branches2(next_point, next_angle, next_length)
    draw_branches2(next_point2, next_angle2, next_length)

draw_branches2(root_point, angle, length)
draw_branches2(root_point, angle, length)


sd.pause()
# зачет!