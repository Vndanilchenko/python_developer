# -*- coding: utf-8 -*-

# Подземелье было выкопано ящеро-подобными монстрами рядом с аномальной рекой, постоянно выходящей из берегов.
# Из-за этого подземелье регулярно затапливается, монстры выживают, но не герои, рискнувшие спуститься к ним в поисках
# приключений.
# Почуяв безнаказанность, ящеры начали совершать набеги на ближайшие деревни. На защиту всех деревень не хватило
# солдат и вас, как известного в этих краях героя, наняли для их спасения.
#
# Карта подземелья представляет собой json-файл под названием rpg.json. Каждая локация в лабиринте описывается объектом,
# в котором находится единственный ключ с названием, соответствующем формату "Location_<N>_tm<T>",
# где N - это номер локации (целое число), а T (вещественное число) - это время,
# которое необходимо для перехода в эту локацию. Например, если игрок заходит в локацию "Location_8_tm30000",
# то он тратит на это 30000 секунд.
# По данному ключу находится список, который содержит в себе строки с описанием монстров а также другие локации.
# Описание монстра представляет собой строку в формате "Mob_exp<K>_tm<M>", где K (целое число) - это количество опыта,
# которое получает игрок, уничтожив данного монстра, а M (вещественное число) - это время,
# которое потратит игрок для уничтожения данного монстра.
# Например, уничтожив монстра "Boss_exp10_tm20", игрок потратит 20 секунд и получит 10 единиц опыта.
# Гарантируется, что в начале пути будет две локации и один монстр
# (то есть в коренном json-объекте содержится список, содержащий два json-объекта, одного монстра и ничего больше).
#
# На прохождение игры игроку дается 123456.0987654321 секунд.
# Цель игры: за отведенное время найти выход ("Hatch")
#
# По мере прохождения вглубь подземелья, оно начинает затапливаться, поэтому
# в каждую локацию можно попасть только один раз,
# и выйти из нее нельзя (то есть двигаться можно только вперед).
#
# Чтобы открыть люк ("Hatch") и выбраться через него на поверхность, нужно иметь не менее 280 очков опыта.
# Если до открытия люка время заканчивается - герой задыхается и умирает, воскрешаясь перед входом в подземелье,
# готовый к следующей попытке (игра начинается заново).
#
# Гарантируется, что искомый путь только один, и будьте аккуратны в рассчетах!
# При неправильном использовании библиотеки decimal человек, играющий с вашим скриптом рискует никогда не найти путь.
#
# Также, при каждом ходе игрока ваш скрипт должен запоминать следущую информацию:
# - текущую локацию
# - текущее количество опыта
# - текущие дату и время (для этого используйте библиотеку datetime)
# После успешного или неуспешного завершения игры вам необходимо записать
# всю собранную информацию в csv файл dungeon.csv.
# Названия столбцов для csv файла: current_location, current_experience, current_date
#
#
# Пример взаимодействия с игроком:
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло времени: 00:00
#
# Внутри вы видите:
# — Вход в локацию: Location_1_tm1040
# — Вход в локацию: Location_2_tm123456
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали переход в локацию Location_2_tm1234567890
#
# Вы находитесь в Location_2_tm1234567890
# У вас 0 опыта и осталось 0.0987654321 секунд до наводнения
# Прошло времени: 20:00
#
# Внутри вы видите:
# — Монстра Mob_exp10_tm10
# — Вход в локацию: Location_3_tm55500
# — Вход в локацию: Location_4_tm66600
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали сражаться с монстром
#
# Вы находитесь в Location_2_tm0
# У вас 10 опыта и осталось -9.9012345679 секунд до наводнения
#
# Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!
#
# У вас темнеет в глазах... прощай, принцесса...
# Но что это?! Вы воскресли у входа в пещеру... Не зря матушка дала вам оберег :)
# Ну, на этот-то раз у вас все получится! Трепещите, монстры!
# Вы осторожно входите в пещеру... (текст умирания/воскрешения можно придумать свой ;)
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло уже 0:00:00
# Внутри вы видите:
#  ...
#  ...
#
# и так далее...
import csv
import json
import os
import re
from datetime import timedelta
from termcolor import cprint


class UnknownElement(Exception):
    pass

class UserExit(Exception):
    pass

class GameOver(Exception):
    pass

class HappyEnd(Exception):
    pass

class Game:

    def __init__(self, location):
        self.remaining_time = float('123456.0987654321')
        self.seconds_from_start = float(0)  # время в игре
        self.total_exp_to_exit = 280 # накопительный опыт пользователя
        self.total_user_exp = 0  # накопительный опыт пользователя
        self.mosters_killed = 0 # количество убитых монстров
        self.num2elem = {}  # хранит номер и оригинальное название
        self.num2action = {}  # номер и тип действия
        self.num2name = {}  # хранит номер и название элемента
        self.num2sec = {}  # номер к секундам
        self.num2time = {}  # номер к времени ЧЧ:ММ:СС
        self.num2exp = {}  # номер к опыту
        self.start_location = location
        self.data = self.read_json()
        self.new_data = self.data # будет накапливаться выбор пользователя для путешествия по json

    def __str__(self):
        cprint('{:-^50s}'.format(' статистика игры '), color='cyan')
        cprint('заработано опыта: {1}, достаточно для выхода из подземелья: {4}\nвремени осталось: {0}, прошло с начала игры {3}\nмонстров убито: {2}'.
               format(str(timedelta(seconds=self.remaining_time)), self.total_user_exp, self.mosters_killed,
                      str(timedelta(seconds=self.seconds_from_start)), self.total_exp_to_exit <= self.total_user_exp), color='cyan')
        cprint('{:-^50s}\n'.format(''), color='cyan')

    # получение основной информации
    def read_json(self):
        # with open(os.path.join(os.getcwd(), r'python_base/lesson_015/rpg.json'), encoding='utf8', mode='r') as f:
        with open(os.path.join(os.getcwd(), r'rpg.json'), encoding='utf8', mode='r') as f:
            data = json.load(f)
        return data

    # функция получения информации из элемента json
    def parse_info(self, element):
        if 'Location' in element:
            # element = 'Location_0_tm0'
            if not re.sub(r'Location_\d+_tm[0-9.]{1,}', '', element):
                elem_name = re.sub(r'_tm[0-9.]{1,}', '', element)
                elem_seconds = re.sub(r'Location_\d+_tm', '', element)
                elem_time = str(timedelta(seconds=float(elem_seconds)))
            else:
                # element = 'Location_B1_tm0.098765432'
                elem_name = re.sub(r'_tm[0-9.]{1,}', '', element)
                elem_seconds = re.sub(r'Location_[A-Z]\d+_tm', '', element)
                elem_time = str(timedelta(seconds=float(elem_seconds)))
            elem_exp = 0
            return elem_name, elem_seconds, elem_time, elem_exp
        elif 'Mob' in element:
            # element = 'Mob_exp10_tm0'
            elem_name = 'Monster'
            elem_seconds = re.sub(r'Mob_exp\d+_tm', '', element)
            elem_time = str(timedelta(seconds=float(elem_seconds)))
            elem_exp = re.sub(r'(Mob_exp)|(_tm[0-9.]{1,})', '', element)
            return elem_name, elem_seconds, elem_time, int(elem_exp)
        elif 'Boss' in element:
            # element = 'Boss_exp280_tm10400000'
            elem_name = 'Boss'
            elem_seconds = re.sub(r'Boss_exp\d+_tm', '', element)
            elem_time = str(timedelta(seconds=float(elem_seconds)))
            elem_exp = re.sub(r'(Boss_exp)|(_tm[0-9.]{1,})', '', element)
            return elem_name, elem_seconds, elem_time, int(elem_exp)
        elif 'Boss' in element:
            # element = 'Boss200_exp30_tm10'
            elem_name = 'Boss'
            elem_seconds = re.sub(r'Boss\d+_exp\d+_tm', '', element)
            elem_time = str(timedelta(seconds=float(elem_seconds)))
            elem_exp = re.sub(r'(Boss\d+_exp)|(_tm[0-9.]{1,})', '', element)
            return elem_name, elem_seconds, elem_time, int(elem_exp)
        elif 'Hatch' in element:
            # element = "Hatch_tm159.098765432"
            elem_name = 'Выбраться из подземелья'
            elem_seconds = re.sub(r'Hatch_tm', '', element)
            elem_time = str(timedelta(seconds=float(elem_seconds)))
            elem_exp = 0
            return elem_name, elem_seconds, elem_time, elem_exp
        else:
            raise UnknownElement(element)

    # лог игры
    def write_info_to_csv(self, current_location, current_experience, current_date):
        with open(os.path.join(os.getcwd(), 'dungeon.csv'), 'a', newline='') as out_csv:
            writer = csv.writer(out_csv)
            field_names = [current_location, current_experience, current_date]
            writer.writerow(field_names)

    # будут пересоздаваться при каждом входе в новую локацию
    def reset_dicts(self):
        self.num2elem = {}
        self.num2action = {}  # номер и тип действия
        self.num2name = {}  # хранит номер и название элемента
        self.num2sec = {}  # номер к секундам
        self.num2time = {}  # номер к времени ЧЧ:ММ:СС
        self.num2exp = {}  # номер к опыту

    # функция выбора действия в локации
    def make_choice(self, num):
        # print(self.num2action)
        flag = False
        while not flag:
            print('теперь перед вами стоит выбор:')
            for j in sorted(self.num2action.keys()):
                print(j, ' ', self.num2action[j], self.num2name[j], ', займет:', self.num2time[j],
                      ', будет заработано:', self.num2exp[j], 'опыта')
            print(max(self.num2action.keys()) + 1, ' ', 'сдаться и выйти из игры')
            user_choice = input(f'\nвведите цифру в соответствии с предложенными вариантами\n')
            if user_choice.isnumeric():
                # выбрал выход
                if int(user_choice)==max(self.num2action.keys())+1:
                    flag = True
                # выбрал один из вариантов
                elif int(user_choice) in self.num2action.keys():
                    flag = True
                else:
                    cprint('других вариантов нет..', color='magenta')
            else:
                cprint('таких вариантов нет..', color='magenta')
        return int(user_choice)

    # основная функция игры
    def run(self, json_element=None):
        try:
            num = 0  # выбор пользователя
            if not json_element:
                self.__str__()
                json_element = self.start_location
            # запишем инфо в лог
            self.write_info_to_csv(json_element, self.total_user_exp, str(timedelta(self.seconds_from_start)))
            # закрепим текущий уровень json
            self.new_data = self.new_data[json_element]
            # сбросим словари
            self.reset_dicts()
            cprint('вы попали в локацию: {}, перед вами выбор:'.format(json_element), color='blue')
            for i in self.new_data:
                num += 1
                if isinstance(i, dict):
                    element = list(i.keys())[0]
                    self.num2action[num] = 'перейти в локацию:'
                else:
                    element = i
                    self.num2action[num] = 'сразиться с:'

                elem_name, elem_seconds, elem_time, elem_exp = self.parse_info(element)
                self.num2name[num] = elem_name
                self.num2elem[num] = element
                self.num2sec[num] = elem_seconds
                self.num2time[num] = elem_time
                self.num2exp[num] = elem_exp

            # примем выбор пользователя
            flag = False
            while not flag:
                user_choice = self.make_choice(num)

                if user_choice==num+1:
                    cprint('ну нафиг, я сваливаю :)', color='yellow')
                    raise UserExit()
                else:
                    cprint('вы выбрали {} {}'.format(self.num2action[user_choice], self.num2name[user_choice]), color='blue')

                self.total_user_exp += self.num2exp[user_choice]
                self.remaining_time -= float(self.num2sec[user_choice])
                self.seconds_from_start += float(self.num2sec[user_choice])
                if self.remaining_time<0:
                    raise GameOver()

                if 'Выбраться' in self.num2name[user_choice]:
                    if self.total_user_exp>=self.total_exp_to_exit:
                        self.__str__()
                        raise HappyEnd()
                    else:
                        cprint('\nкажется у меня недостаточно опыта, что выйти отсюда!..', color='red')
                        raise GameOver()
                elif 'Location' not in self.num2name[user_choice]:
                    self.num2elem.pop(user_choice)
                    self.num2action.pop(user_choice)
                    self.num2name.pop(user_choice)
                    self.num2sec.pop(user_choice)
                    self.num2time.pop(user_choice)
                    self.num2exp.pop(user_choice)
                    self.mosters_killed += 1
                    cprint('монстр повержен!', color='yellow')
                    # стоит ли сделать пересчет ключей-индексов словаря?
                else:
                    flag = True
                # распечатаем статистику по игре
                self.__str__()
            self.new_data = self.new_data[user_choice-1]
            self.run(self.num2elem[user_choice])
        except ValueError as e:
            cprint('\nпохоже это тупик..где же выход?!..', color='red')
            raise GameOver()
        except UnknownElement as e:
            print('ошибка! элемент {} не обработан в игре'.format(e.args[0]))
            # return
        except UserExit as e:
            cprint('игра прекращена пользователем..', color='red')
        except GameOver as e:
            cprint(
            "Почему так много воды?! о нет, я не успел..\nУ вас темнеет в глазах... прощай, принцесса...\n{:-^100s}\n".format(' restart '),
            color='red'
            )
            self.__str__()
            cprint(
            "\n\nНо что это?! Я снова у входа в пещеру... Не зря матушка дала вам оберег :)\nНу, на этот-то раз у вас все получится! Трепещите, монстры!)\n",
            color='green'
            )
            self.new_data=self.data
            self.run('Location_0_tm0')
        except HappyEnd as e:
            cprint(' {:*^100s} '.format(' УРА! Все монстры повержены, иди ко мне моя принцесса! '), color='green')
            cprint(' {:*^100s} '.format(' хватит с меня этих приключений '), color='green')
            cprint('\n{: ^100s} '.format(' ПОБЕДА '), color='green')
            # return


obj = Game('Location_0_tm0')
obj.run()

with open(os.path.join(os.getcwd(), r'python_base/lesson_015/rpg.json'), encoding='utf8', mode='r') as f:
    data = json.load(f)
data['Location_0_tm0'][1]['Location_1_tm1040'][2]['Location_3_tm33000'][0]['Location_7_tm33300'][0]['Location_10_tm55100'][4]['Location_12_tm0.0987654320']
# если выбираем атаковать монстра, то повторяем выбор активности, удалив из него совершенное действие

# Учитывая время и опыт, не забывайте о точности вычислений!
