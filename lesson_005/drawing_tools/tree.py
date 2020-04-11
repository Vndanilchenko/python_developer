# модуль содержит функцию отрисовки дерева

import simple_draw as sd

def tree(start_point=sd.get_point(300, 30), angle=90, length=100):
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
    tree(next_point, next_angle, next_length)
    tree(next_point2, next_angle2, next_length)

if __name__ == '__main__':
    tree()
    tree()
    sd.pause()