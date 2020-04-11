# модуль содержит функцию отрисовки <сугроба> из снежинок в окружности некоторой точки

import simple_draw as sd

def snowball(x = sd.random_number(0, 500), y = sd.random_number(0, 500), radius = 200, quantity = 50):
    for i in range(quantity):
        snowflake_point = sd.get_point(x + sd.random_number(-radius/2, radius/2), y = sd.random_number(-radius/2, radius/2))
        sd.snowflake(snowflake_point, sd.random_number(10, 30), sd.COLOR_WHITE, sd.random_number(1, 100)/100,
                     sd.random_number(1, 100)/100, sd.random_number(1, 100))


if __name__ == '__main__':
    snowball()
    sd.pause()