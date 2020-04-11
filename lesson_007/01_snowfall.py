# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.id = 0

    def generate_snowflake(self, id):

        self.sf_lengths = sd.random_number(15, 40)
        # зачем метод generate_snowflake? одного __init__ не достаточно - в него можно предавать параметры тоже
        self.sf_a = sd.random_number(1, 100) / 100
        self.sf_b = sd.random_number(1, 100) / 100
        self.sf_c = sd.random_number(1, 100) / 100
        self.x = sd.random_number(-300, sd.resolution[0])
        self.y = sd.resolution[0]
        self.id = id
        self.draw()

    def move(self):
        delta_x = sd.random_number(-30, 30)
        delta_y = sd.random_number(0, 30)
        self.x += delta_x
        self.y -= delta_y
        sd.snowflake(sd.get_point(self.x, self.y), self.sf_lengths, sd.COLOR_WHITE,
                      self.sf_a, self.sf_b, self.sf_c)
        sd.finish_drawing()

    def can_fall(self):
        return self.y < 20

    def clear_previous_picture(self):
        self.draw()
        sd.snowflake(sd.get_point(self.x, self.y), self.sf_lengths, sd.background_color,
                     self.sf_a, self.sf_b, self.sf_c)

    def draw(self):
        sd.start_drawing()

    def __str__(self):
        return 'снежинка {} с координатами x={} и y={}'.format(self.id, self.x, self.y)

# flake = Snowflake()
# flake.generate_snowflake(id=0)
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


class snowfall:

    def __init__(self):
        self.snowflakes = []
        self.count = 1
        self.cnt_fallen = []

    def get_flakes(self, count):
        self.count = count
        for i in range(self.count):
            flake = Snowflake()
            self.snowflakes.append(flake)
            self.snowflakes[i].generate_snowflake(id=i)
        return self.snowflakes

    def get_fallen_flakes(self):
        for i in range(self.count):
            if self.snowflakes[i].can_fall():
                self.cnt_fallen.append(i)
        return self.cnt_fallen

    def append_flakes(self):
        # sd.clear_screen()
        for i in self.cnt_fallen:
            self.snowflakes[i].clear_previous_picture()
            self.snowflakes[i].generate_snowflake(id=i)
            self.cnt_fallen.remove(i)


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = snowfall()
flakes.get_flakes(count=10)  # создать список снежинок

while True:
    for flake in flakes.snowflakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = flakes.get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        print(fallen_flakes)
        flakes.append_flakes()  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
# зачет!