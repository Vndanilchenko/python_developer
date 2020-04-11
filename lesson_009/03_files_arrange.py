# -*- coding: utf-8 -*-

import os, time, shutil
from collections import defaultdict

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class Count_NON_per_minutes:

    def __init__(self):
        self.path_to_file = os.path.join(os.getcwd(), r'python_base\lesson_009')
        self.input_directory_name = 'icons'
        self.output_directory_name = 'icons_by_year'
        self.duplicated_files = []

    def sort_and_replace_files(self):
        for dirpath, filepath, filenames in os.walk(os.path.join(self.path_to_file, self.input_directory_name)):
            for filename in filenames:
                modification_date = time.gmtime(os.path.getmtime(os.path.join(dirpath, filename)))
                dst_months = os.path.join(self.path_to_file, self.output_directory_name, str(modification_date[0]), str(modification_date[1]))
                print(dst_months)
                os.makedirs(dst_months, exist_ok=True)
                try:
                    shutil.copy2(os.path.join(dirpath, filename), os.path.join(dst_months, filename))
                except FileExistsError:
                    self.duplicated_files.append(os.path.join(dirpath, filename))


some_file = Count_NON_per_minutes()
some_file.sort_and_replace_files()
print('файлов не обработано:', len(some_file.duplicated_files))

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
# зачет!