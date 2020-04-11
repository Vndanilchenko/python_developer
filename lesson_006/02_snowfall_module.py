# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

import snowfall as sf

# создать_снежинки(N)
qnty_snowflakes_original, qnty_snowflakes, x_list, y_list, points, sf_lengths, sf_a, sf_b, sf_c, snowflakes = sf.generate_snowfall()

i=0
while True:
    # нарисовать_снежинки_цветом(color)
    sd.start_drawing()
    #  сдвинуть_снежинки()
    sf.move_snowflakes(qnty_snowflakes, x_list, y_list, points, snowflakes, sf_lengths, sf_a, sf_b, sf_c)
    #  номера_достигших_низа_экрана()
    sf.print_fallen_snowflakes(qnty_snowflakes, y_list)

    sd.finish_drawing()

    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    if len(qnty_snowflakes_original)>len(qnty_snowflakes):
        new_idx = set(qnty_snowflakes_original) - set(qnty_snowflakes)
        qnty_snowflakes, x_list, y_list, points, sf_lengths, sf_a, sf_b, sf_c, snowflakes = \
            sf.add_new_snowfall_on_free_place(x_list,
                                              y_list,
                                              points,
                                              sf_lengths,
                                              sf_a,
                                              sf_b,
                                              sf_c,
                                              snowflakes,
                                              new_idx,
                                              qnty_snowflakes)

    sd.sleep(0.001)
    if sd.user_want_exit():
        break
    i+=1
sd.pause()

# зачет!