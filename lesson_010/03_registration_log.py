# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

import os

class NotNameError(Exception):
    pass

class NotEmailError(Exception):
    pass

class Check_data:

    def __init__(self):
        self.filename = 'registrations.txt'
        self.pathname = os.path.join(os.getcwd(), r'python_base\lesson_010')
        self.output_filename_correct = 'registrations_good.log'
        self.output_filename_errors = 'registrations_bad.log'
        self.output_errors_list = []
        self.output_correct_list = []

    def __str__(self):
        return 'совершена проверка данных из файла {} на корректное заполнение - правильные данные записаны в файл {}, неправильные в {}'.\
            format(self.filename, self.output_filename_correct, self.output_filename_errors)

    # оповещает о типе ошибки
    def error_teller(self, e):
        print(f'Исключение типа {type(e)} пролетело мимо! его параметры {e.args}')
        return False

    # проверяет на ошибки и выкидывает исключения при нахождении
    def find_errors(self, *args):
        data_tmp = args[0]
        try:
            if len(data_tmp) < 3:
                raise ValueError('НЕ присутсвуют все три поля')
            elif not str(data_tmp[0]).isalpha():
                raise NotNameError('поле имени содержит НЕ только буквы. введено: {}'.format(data_tmp[0]))
            elif '.' not in data_tmp[1] or '@' not in data_tmp[1]:
                raise NotEmailError('поле емейл НЕ содержит @ или .(точку). введено: {}'.format(data_tmp[0]))
            elif int(data_tmp[2]) < 10 or int(data_tmp[2]) > 99:
                raise ValueError('поле возраст НЕ является числом от 10 до 99. введено: {}'.format(data_tmp[2]))
            else:
                return True
        except ValueError as e:
            return self.error_teller(e)
        except NotNameError as e:
            return self.error_teller(e)
        except NotEmailError as e:
            return self.error_teller(e)
        except Exception as e:
            return self.error_teller(e)


    # построчное чтение файла и распределение между корректным и списком с ошибками
    def check_file(self):
        with open(os.path.join(self.pathname, self.filename), mode='r', encoding='utf8') as f:
            for line in f:
                if self.find_errors(line.split()):
                    self.output_correct_list.append(line)
                else:
                    self.output_errors_list.append(line)


    # запись ошибок из списка в сответствующий файл
    def write_errors_to_file(self):
        with open(os.path.join(self.pathname, self.output_filename_errors), mode='w') as f:
            for line in self.output_errors_list:
                f.writelines(line)

    # запись корректных данных из списка в сответствующий файл
    def write_correct_to_file(self):
        with open(os.path.join(self.pathname, self.output_filename_correct), mode='w') as f:
            for line in self.output_correct_list:
                f.writelines(line)

    # последовательный запуск всех функций класса
    def prepare_files(self):
        self.check_file()
        self.write_correct_to_file()
        self.write_errors_to_file()
        print(self.__str__())


temp_obj = Check_data()
temp_obj.prepare_files()

# зачет!