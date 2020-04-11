# модуль содержит функцию отрисовки радуги по заданным координатам центра окружности

import simple_draw as sd

def rainbow(x = 600, y = 50, radius = 450):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    width = 4
    for i in rainbow_colors:
        point = sd.get_point(x, y)
        radius += 10
        width += 2
        sd.circle(center_position=point, radius=radius, width=width, color=i)

if __name__ ==  '__main__':
    rainbow()
    sd.pause()