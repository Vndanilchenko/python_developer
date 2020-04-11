# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# ничего, если они будут разноцветные?
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# a_x = 0
# a_y = 0
# b_x = 100
# b_y = 50
# point_a = sd.get_point(a_x, a_y)
# point_b = sd.get_point(b_x, b_y)
# sd.rectangle(point_a, point_b, color = rainbow_colors[sd.random_number(0, 6)])
for i in range(12):
    a_y = i * 50
    b_y = (1 + i) * 50
    for j in range(7):
        if j == 0:
            if i % 2 == 0:
                a_x = - 50
                b_x = 50
            else:
                a_x = 0
                b_x = 100
        else:
            a_x = b_x
            b_x = b_x + 100
            # a_x = j * 100
            # b_x = (1 + j) * 100
        point_a = sd.get_point(a_x, a_y)
        point_b = sd.get_point(b_x, b_y)
        sd.rectangle(point_a, point_b, color = (sd.COLOR_ORANGE), width=1)
sd.pause()
# зачет!