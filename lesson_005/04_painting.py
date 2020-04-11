# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)
import simple_draw as sd
sd.set_screen_size(1500, 800)

from drawing_tools import rainbow, wall, smile, tree, snowball

# радуга
rainbow.rainbow(x = 600, y = 100, radius = 950)

# дом с кирпичной стеной
left_x = 700
left_y = 100
right_x = 1100
right_y = 550
sd.rectangle(sd.get_point(left_x, left_y), sd.get_point(right_x, right_y), sd.COLOR_ORANGE, 1)
wall.wall(left_x, left_y, right_x, right_y)

# крыша
sd.polygon([sd.get_point(left_x-50, right_y), sd.get_point(right_x+50, right_y), sd.get_point(left_x + (right_x-left_x)/2, right_y + 100)], sd.COLOR_ORANGE)

# окно
sd.rectangle(sd.get_point(left_x + 100, left_y + 100), sd.get_point(right_x - 100, right_y - 100), sd.COLOR_DARK_ORANGE)
sd.rectangle(sd.get_point(left_x + 110, left_y + 110), sd.get_point(right_x - 110, right_y - 110), sd.COLOR_WHITE)

# смайл
smile.smiling_face(left_x + (right_x-left_x)/2, left_y + (right_y-left_y)/2)

# дерево
tree.tree(sd.get_point(right_x+200, left_y))

# сугроб
snowball.snowball(left_x - 200, left_y + 100, 400, 200)

# солнце
point = sd.get_point(left_x - 400, right_y + 100)
sd.circle(point, 100, sd.COLOR_YELLOW, 0)
sd.snowflake(point, 200, sd.COLOR_YELLOW, 0.01, 0.01, 100)

# лавочка под деревом
sd.rectangle(sd.get_point(right_x+50, left_y+70), sd.get_point(right_x+400, left_y+80), sd.COLOR_DARK_ORANGE)
sd.rectangle(sd.get_point(right_x+100, left_y), sd.get_point(right_x+110, left_y+70), sd.COLOR_DARK_ORANGE)
sd.rectangle(sd.get_point(right_x+340, left_y), sd.get_point(right_x+350, left_y+70), sd.COLOR_DARK_ORANGE)

sd.pause()
# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
# зачет!