# модуль содержит функцию отрисовки кирпичной стены

import simple_draw as sd
sd.set_screen_size(1500, 800)

def wall(start_x = sd.random_number(0, 100), start_y = sd.random_number(0, 100), end_x = sd.random_number(300, 800), end_y = sd.random_number(300, 800)):
    for i in range((end_y - start_y) // 50):
        offset = 1 if i % 2 != 0 else 0
        for j in range((end_x - start_x) // 100):
            if j >= (end_x - start_x) // 100 - 1:
                print(j)
                if i % 2 != 0:
                    left_bottom_point = sd.get_point(start_x + j * 100 + offset * 50, start_y + i * 50)
                    right_top_point = sd.get_point(left_bottom_point.x + 50, start_y + (1 + i) * 50)
            else:
                left_bottom_point = sd.get_point(start_x + j*100 + offset*50, start_y + i*50)
                right_top_point = sd.get_point(left_bottom_point.x + 100, start_y + (1+i)*50)
            sd.rectangle(left_bottom_point, right_top_point, color = (sd.COLOR_ORANGE), width=1)

if __name__ == '__main__':
    wall()
    sd.pause()