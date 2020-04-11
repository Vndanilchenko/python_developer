# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

# N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# x = 0
# y = 500
# while True:
#     sd.clear_screen()
#     point = sd.get_point(x, y)
#
#     s1 = sd.snowflake(point, sd.random_number(15, 40), sd.random_color(), sd.random_number(0, 100)/100, sd.random_number(0, 100)/100, sd.random_number(0, 100)/100)
#     x += sd.random_number(5, 15)
#     y -= sd.random_number(15, 30)
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

qnty_snowflakes = sd.random_number(10, 100)
x_list = [sd.random_number(-300, sd.resolution[0]) for _ in range(qnty_snowflakes)]
y_list = [500 for _ in range(qnty_snowflakes)]
points = [sd.get_point(x_list[i], y_list[i]) for i in range(qnty_snowflakes)]
sf_lengths = [sd.random_number(15, 40) for _ in range(qnty_snowflakes)]
sf_a = [sd.random_number(1, 100)/100 for _ in range(qnty_snowflakes)]
sf_b = [sd.random_number(1, 100)/100 for _ in range(qnty_snowflakes)]
sf_c = [sd.random_number(1, 100)/100 for _ in range(qnty_snowflakes)]
snowflakes = [sd.snowflake for i in range(qnty_snowflakes)]
i=0
while True:
    sd.start_drawing()
    for i in range(qnty_snowflakes):
        delta_x = sd.random_number(-30, 30)
        delta_y = sd.random_number(0, 30)
        x_list[i] += delta_x
        y_list[i] -= delta_y
        if y_list[i]<10:
            y_list[i] = 10
        points[i] = sd.get_point(x_list[i], y_list[i])
        sd.start_drawing()
        snowflakes[i](points[i], sf_lengths[i], sd.COLOR_WHITE, sf_a[i], sf_b[i], sf_c[i])
        snowflakes[i](sd.get_point(x_list[i]-delta_x, y_list[i]+delta_y), sf_lengths[i], sd.background_color, sf_a[i], sf_b[i], sf_c[i])

    sd.finish_drawing()
    sd.sleep(0.001)
    if max(y_list) == 10:
        break
    if sd.user_want_exit():
        break
    i+=1
sd.pause()
# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

# зачет!
