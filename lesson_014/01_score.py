# -*- coding: utf-8 -*-

# Вас взяли на работу в молодой стартап. Идея стартапа - предоставлять сервис расчета результатов игр.
# Начать решили с боулинга, упрощенной версии.
#
# Правила такие.
#
# Всего 10 кеглей. Игра состоит из 10 фреймов. В одном фрейме до 2х бросков, цель - сбить все кегли.
# Результаты фрейма записываются символами:
#   «Х» – «strike», все 10 кеглей сбиты первым броском
#   «<число>/», например «4/» - «spare», в первый бросок сбиты 4 кегли, во второй – остальные
#   «<число><число>», например, «34» – в первый бросок сбито 3, во второй – 4 кегли.
#   вместо <число> может стоять прочерк «-», например «-4» - ни одной кегли не было сбито за первый бросок
# Результат игры – строка с записью результатов фреймов. Символов-разделителей между фреймами нет.
# Например, для игры из 3 фреймов запись результатов может выглядеть так:
#   «Х4/34-4»
# Предлагается упрощенный способ подсчета количества очков:
#   «Х» – 20 очков, «4/» - 15 очков, «34» – сумма 3+4=7, «-4» - сумма 0+4=4
# То есть для игры «Х4/34» сумма очков равна 20+15+7+4=46
#
# Надо написать python-модуль (назвать bowling), предоставляющий API расчета количества очков:
# функцию get_score, принимающую параметр game_result. Функция должна выбрасывать исключения,
# когда game_result содержит некорректные данные. Использовать стандартные исключения по максимуму,
# если не хватает - создать свои.
#
# Обязательно написать тесты на этот модуль. Расположить в папке tests.

import bowling
import argparse


parser = argparse.ArgumentParser(description='расчет исхода игры для двух команд')
parser.add_argument('results', type=str, nargs='+',
                    help='добавьте результаты двух команд через пробел: X4/-3 XX34')
parser.add_argument('--result', dest='result', action='store_const',
                    const=sum, default=max,
                    help='подсчет очков за игру для каждой команды')

args = parser.parse_args()
results = args.results
# results = ["11--11", "Х4/34-4"]


game_results = []
commands = ['команда 1', 'команда 2']
for i in range(2):
    # summ = enter_the_data(commands[i], results[i])
    j = 0
    game_sum = 0
    while game_sum == 0:
        if j == 0:
            game_result = results[i]
        else:
            game_result = input('\nвведите результаты: ' + str(commands[i]) + '\n')
        objects = bowling.CalculateResult(result=game_result, name=commands[i])
        try:
            objects.run()
            game_sum = objects.game_sum
        except IndexError as e:
            print(f'вышли за границы диапазона! ошибка {e.args}')
            game_sum = 0
        except bowling.EmptyList as e:
            print(f'введи результаты игры! ошибка {e.args}')
            game_sum = 0
        except bowling.TooManySets as e:
            print(f'ошибка: введено слишком много сетов ({e.args[0]})')
            game_sum = 0
        except bowling.WrongSymbol as e:
            print(f'ошибка: введен неправильный символ в фрейме номер: ({e.args[0]})')
            game_sum = 0
        except AttributeError as e:
            print(f'ошибка атрибута: ({e.args[0]})')
            game_sum = 0
        except bowling.OverTenError as e:
            print(f'введи корректные значения для фрейма! ошибка суммы во фрейме номер: ({e.args[0]})')
            game_sum = 0
        except bowling.WrongSymbolsCountError as e:
            print(f'введи корректные значения! ошибка : ({e.args})')
            game_sum = 0
        except bowling.DoubleSlashError as e:
            print('ошибка! введен двойной слэш в фрейме номер: ', e.args[0])
            game_sum = 0
        except bowling.ZerroExistsError as e:
            print('ошибка! введен 0 в фрейме номер: ', e.args[0])
            game_sum = 0
        except bowling.WrongFirstSymbolError as e:
            print('ошибка! введен / на первом месте в фрейме номер: ', e.args[0])
            game_sum = 0


        j += 1

    game_results.append(game_sum)
    print(f'Количество очков для команды {commands[i]}: {game_sum}')

# а я в папке tests сделал test_01_score, можно по ним ОС тоже? тесты на эксепшены в процессе доделаю пока

# Из текущего файла сделать консольную утилиту для определения количества очков, с помощью пакета argparse
# Скрипт должен принимать параметр --result и печатать на консоль:
#   Количество очков для результатов ХХХ - УУУ.




# При написании кода помнить, что заказчик может захотеть доработок и новых возможностей...
# И, возможно, вам пригодится паттерн проектирования "Состояние",
#   см https://clck.ru/Fudd8 и https://refactoring.guru/ru/design-patterns/state

# не понял как это применить
