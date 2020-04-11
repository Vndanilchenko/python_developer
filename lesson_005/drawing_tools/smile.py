# модуль содержит функцию отрисовки простого смайлика
import simple_draw as sd


def smiling_face(x = 500, y = 500, radius=50, color = sd.COLOR_YELLOW):
    # овал головы
    central_point = central_point=sd.get_point(x, y)
    sd.circle(center_position=central_point, radius=50, color=color)

    point_left = sd.get_point(x - 25, y + 25)
    point_right = sd.get_point(x + 25, y + 25)
    # глаза
    sd.circle(center_position=point_left, radius=10, color=color)
    sd.circle(center_position=point_right, radius=10, color=color)
    # зрачки
    sd.circle(center_position=point_left, radius=2, color=sd.COLOR_BLUE, width=0)
    sd.circle(center_position=point_right, radius=2, color=sd.COLOR_BLUE, width=0)
    # задорная улыбка
    point_left_lips = sd.get_point(x - 25, y - 25)
    v = sd.vector(start=point_left_lips, angle=0, length=50, color=color)

if __name__=='__main__':
    smiling_face(color=sd.COLOR_CYAN)
    sd.pause()