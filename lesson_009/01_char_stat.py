# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# import zipfile
# zip = zipfile.ZipFile(r'C:\Users\vndan\projects\skillbox\python_base\lesson_009\python_snippets\voyna-i-mir.txt.zip')
# zip.extractall(r'C:\Users\vndan\projects\skillbox\python_base\lesson_009\python_snippets')
# zip.close()

from collections import defaultdict
import os


class Calculate_letters_statistics:

    def __init__(self):
        self.path_to_file = os.path.join(os.getcwd(), r'python_base\lesson_009\python_snippets')
        self.statistics = defaultdict(int)
        self.file_to_read = 'voyna-i-mir.txt'
        self.summ = 0

    def __str__(self):
        return 'вывод статистики использования букв по словарю'

    def calculate_statistics(self):
        with open(os.path.join(self.path_to_file, self.file_to_read), encoding='cp1251') as f:
            for sentence in f.readlines():
                for letter in sentence:
                    if letter.isalpha():
                        self.statistics[letter] += 1

    def print_statistics_header(self):
        # вывод словаря
        print(self.__str__())
        print('+{:-^7s}-+-{:-^7s} +'.format('', ''))
        print('|{0: ^7s} | {1: ^7s} |'.format('буква', 'частота'))
        print('+{:-^7s}-+-{:-^7s} +'.format('', ''))

    def print_statistics_totals(self):
        print('+{:-^7s}-+-{:-^7s} +'.format('', ''))
        print('|{0: ^7s} | {1:7d} |'.format('итого', self.summ))
        print('+{:-^7s}-+-{:-^7s} +'.format('', ''))

    def sort_statistics(self):
        for k, v in sorted(self.statistics.items(), key=lambda kv: kv[0]):
            print('|{0: ^7s} | {1:7d} |'.format(k, v))
            self.summ += v

    def print_statistics(self):
        self.calculate_statistics()
        self.print_statistics_header()
        self.sort_statistics()
        self.print_statistics_totals()




class Print_statistics_format1(Calculate_letters_statistics):

    def __str__(self):
        return 'Упорядочивание по частоте по убыванию\n'

    def sort_statistics(self):
        for k, v in sorted(self.statistics.items(), key=lambda kv: -kv[1]):
            print('|{0: ^7s} | {1:7d} |'.format(k, v))
            self.summ += v



# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию

class Print_statistics_format2(Calculate_letters_statistics):

    def __str__(self):
        return 'Упорядочивание по частоте по возрастанию\n'

    def sort_statistics(self):
        for k, v in sorted(self.statistics.items(), key=lambda kv: kv[1]):
            print('|{0: ^7s} | {1:7d} |'.format(k, v))
            self.summ += v

#  - по алфавиту по возрастанию
class Print_statistics_format3(Calculate_letters_statistics):

    def __str__(self):
        return 'Упорядочивание по алфавиту по возрастанию\n'

    def sort_statistics(self):
        for k, v in sorted(self.statistics.items(), key=lambda kv: kv[0]):
            print('|{0: ^7s} | {1:7d} |'.format(k, v))
            self.summ += v


#  - по алфавиту по убыванию
class Print_statistics_format4(Calculate_letters_statistics):

    def __str__(self):
        return 'Упорядочивание по алфавиту по убыванию\n'

    def sort_statistics(self):
        statistics_sorted = sorted(self.statistics.items(), key=lambda kv: kv[0])
        for k, v in sorted(statistics_sorted, key=lambda kv: -kv[1]):
            print('|{0: ^7s} | {1:7d} |'.format(k, v))
            self.summ += v


choice = input('\nвыберите порядок сортировки: \n1 - по частоте по убыванию \n2 - по частоте по возрастанию \n3 - по алфавиту по возрастанию \n4 - по алфавиту по убыванию \n')
while int(choice) not in [1,2,3,4]:
    choice = input('\nвыберите порядок сортировки: \n1 - по частоте по убыванию \n2 - по частоте по возрастанию \n3 - по алфавиту по возрастанию \n4 - по алфавиту по убыванию \n')
if choice == '1':
    smthng = Print_statistics_format1()
elif choice == '2':
    smthng = Print_statistics_format2()
elif choice == '3':
    smthng = Print_statistics_format3()
elif choice == '4':
    smthng = Print_statistics_format4()
smthng.print_statistics()


# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
# зачет!