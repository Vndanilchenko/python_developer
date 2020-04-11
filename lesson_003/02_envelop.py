# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
# paper_x, paper_y = 8, 9 # нет
# проверить для
# paper_x, paper_y = 9, 8 # нет
# paper_x, paper_y = 6, 8 # да
# paper_x, paper_y = 8, 6 # да
# paper_x, paper_y = 3, 4 # да
# paper_x, paper_y = 11, 9 # нет
paper_x, paper_y = 9, 11 # нет
# (просто раскоментировать нужную строку и проверить свой код)

if (paper_x < envelop_x  and paper_y < envelop_y) or (paper_x < envelop_y  and paper_y < envelop_x):
    print('бумага поместилась в конверте')
else:
    print('бумага не поместилась в конверте')

# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

hole_x, hole_y = 8, 9
# brick_x, brick_y, brick_z = 11, 10, 2 # нет
# brick_x, brick_y, brick_z = 11, 2, 10 # нет
# brick_x, brick_y, brick_z = 10, 11, 2 # нет
# brick_x, brick_y, brick_z = 10, 2, 11 # нет
# brick_x, brick_y, brick_z = 2, 10, 11 # нет
# brick_x, brick_y, brick_z = 2, 11, 10 # нет
# brick_x, brick_y, brick_z = 3, 5, 6 # да
# brick_x, brick_y, brick_z = 3, 6, 5 # да
# brick_x, brick_y, brick_z = 6, 3, 5 # да
# brick_x, brick_y, brick_z = 6, 5, 3 # да
# brick_x, brick_y, brick_z = 5, 6, 3 # да
# brick_x, brick_y, brick_z = 5, 3, 6 # да
# brick_x, brick_y, brick_z = 11, 3, 6 # да
# brick_x, brick_y, brick_z = 11, 6, 3 # да
# brick_x, brick_y, brick_z = 6, 11, 3 # да
# brick_x, brick_y, brick_z = 6, 3, 11 # да
# brick_x, brick_y, brick_z = 3, 6, 11 # да
brick_x, brick_y, brick_z = 3, 11, 6 # да
# (просто раскоментировать нужную строку и проверить свой код)

# определим минимальные стороны, потом проверим проходит или нет
min_0 = 0
min_1 = 0
if brick_x <= brick_y:
    if brick_y <= brick_z:
        min_0 = brick_x
        min_1 = brick_y
    else:
        if brick_x <= brick_z:
            min_0 = brick_x
            min_1 = brick_z
        else:
            min_0 = brick_z
            min_1 = brick_x
elif brick_x >= brick_y:
    if brick_y >= brick_z:
        min_0 = brick_z
        min_1 = brick_y
    else:
        if brick_x <= brick_z:
            min_0 = brick_y
            min_1 = brick_x
        else:
            min_0 = brick_y
            min_1 = brick_z

if (min_0 < hole_x  and min_1 < hole_y) or (min_1 < hole_x  and min_0 < hole_y):
    print('кирпич проходит через отверстие')
else:
    print('кирпич не проходит через отверстие')
# зачет!