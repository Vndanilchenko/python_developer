# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

from PIL import Image, ImageDraw, ImageColor, ImageFont
import os


def make_ticket(fio, from_, to, date):
    fio = fio
    flight_from = from_
    flight_to = to
    flight_date = date
    filename = r'images/ticket_template.png'
    #lesson_path = r'python_base/lesson_013'
    path_to_file = os.path.join(os.getcwd(), filename)
    picture = Image.open(path_to_file)
    draw = ImageDraw.Draw(picture)
    font = ImageFont.truetype('arial.ttf', 15)
    draw.text((40, 120), fio, fill=ImageColor.colormap['black'], font=font)
    draw.text((40, 190), flight_from, fill=ImageColor.colormap['black'], font=font)
    draw.text((40, 260), flight_to, fill=ImageColor.colormap['black'], font=font)
    draw.text((280, 260), flight_date, fill=ImageColor.colormap['black'], font=font)
    Image._show(picture)
    pass

make_ticket('Данильченко Вадим', 'Москва', 'Марс', '01.01.2035')
# зачет!
# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.


