# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirty = 0
        self.cat_food = 30

    def __str__(self):
        return 'в доме денег {} еды {} кошачьего корма {} грязи {}'.format(self.money, self.food, self.dirty, self.cat_food)

    def make_dirty(self):
        self.dirty += 5

    def act(self):
        self.make_dirty()


class Human:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happy = 100
        self.money_earned = 0 # количество заработанных денег
        self.qnty_furs = 0 # количество купленных шуб
        self.days_wo_eat = 0 # дней без еды - больше 3х умирает
        self.is_alive = True # статус жив/умер

    def __str__(self):
        type_role = self.__class__.__name__
        return 'я {}: меня зовут {} степень сытости {} степень счастья {} заработано денег {} куплено шуб {}'.format(
            type_role, self.name, self.fullness, self.happy, self.money_earned, self.qnty_furs)

    def eat(self, food_to_eat=30):
        min_val = min(self.house.food, food_to_eat)
        cprint('{} скушал(-а) {} еды'.format(self.name, min_val), color='yellow')
        self.house.food -= min_val
        self.fullness += min_val
        self.days_wo_eat = 0

    def pet_cat(self):
        cprint('{} гладил(-а) кота '.format(self.name), color='yellow')
        self.happy += 5
        self.fullness -= 10

    def buy_cat_food(self):
        cprint('{} сходил(-а) за кормом для кота'.format(self.name), color='yellow')
        self.house.cat_food += 10
        self.house.money -= 10 # просто прозапас покупали)
        self.fullness -= 10


    def act(self):
        made_action = False
        if self.is_alive:
            if self.fullness <= 10:
                if self.fullness > 0 and self.house.food > 0:
                    self.eat()
                    made_action = True
                else:
                    if self.days_wo_eat >= 3:
                        cprint('{} умер(-ла) от голода..'.format(self.name), color='red')
                        self.is_alive = False
                    else:
                        self.days_wo_eat += 1
                        cprint('{} голодает {} день..'.format(self.name, self.days_wo_eat), color='red')
            elif self.happy < 10:
                cprint('{} умер(-ла) от депрессии..'.format(self.name), color='red')
                self.is_alive = False
                made_action = True
            elif self.happy < 20:
                self.pet_cat()
                made_action = True
            elif self.house.cat_food <= 10:
                self.buy_cat_food()
                made_action = True
            if self.house.dirty > 90 and self.__class__.__name__ != 'Child':
                self.happy -= 10
        else:
            cprint('{} давненько уже умер(-ла)..'.format(self.name), color='red')
        return made_action

    def go_to_the_house(self, house):
        cprint('{} заехал(-а) в дом'.format(self.name), color = 'blue')
        self.house = house

    def __add__(self, other):
        other.house = self.house
        self.fullness -= 10
        cprint('кот {} был забран с улицы в дом'.format(other.name), color='white')


class Husband(Human):

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='green')
        self.house.money += 150
        self.fullness -= 10
        self.money_earned += 150

    def gaming(self):
        cprint('{} поиграл в WoT'.format(self.name), color='magenta')
        self.happy += 20
        self.fullness -= 10

    def act(self):
        if not super(Husband, self).act() and self.is_alive:
            dice = randint(1, 7)
            if self.house.money <= 60:
                self.work()
            elif self.fullness < 20:
                self.gaming()
            elif masha.fullness <= 25:
                self.work()
            elif dice == 3 or dice == 6:
                self.work()
            elif dice == 4:
                self.pet_cat()
            else:
                self.gaming()
        return True


class Wife(Human):
    def act(self):
        if not super(Wife, self).act() and self.is_alive:
            dice = randint(1, 7)
            if self.house.food < 60:
                self.shopping()
            elif self.fullness < 20:
                self.buy_fur_coat()
            elif self.house.dirty > 90:
                self.clean_house()
            elif dice == 3 or dice == 6:
                self.shopping()
            elif dice == 7:
                self.buy_fur_coat()
            elif dice == 4:
                self.pet_cat()
            else:
                self.clean_house()
        return True

    def shopping(self):
        min_val = min(self.house.money, 60)
        cprint('{} купила {} еды'.format(self.name, min_val), color='green')
        self.house.food += min_val
        self.house.money -= min_val
        self.fullness -= 10

    def buy_fur_coat(self):
        if self.house.money >= 350:
            cprint('{} купила шубу'.format(self.name), color='magenta')
            self.happy += 60
            self.house.money -= 350
            self.qnty_furs += 1
        else:
            cprint('{} хотела, но на шубу денег не хватило'.format(self.name), color='magenta')
        self.fullness -= 10
        # serge.happy -= 20   # а как тогда изменить значение в другом объекте, ведь он же не знает, что был вызван этот
                              # метод в текущем

    def clean_house(self):
        min_val = min(self.house.dirty, 100)
        cprint('{} убрала {} грязи '.format(self.name, min_val), color='grey', attrs=['dark'])
        self.house.dirty -= min_val
        self.fullness -= 10



######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = None
        self.is_alive = True

    def __str__(self):
        return 'я {}: меня зовут {} степень сытости {}'.format(
            self.__class__.__name__, self.name, self.fullness)

    def act(self):
        if self.is_alive:
            dice = randint(1, 7)
            if self.fullness < 10 and self.house.cat_food > 0:
                self.eat()
            elif self.fullness < 0:
                cprint('кот {} умер...'.format(self.name), color='red')
                self.is_alive = False
            elif dice == 3 or dice == 6:
                self.soil()
            else:
                self.sleep()
        else:
            cprint('кот {} давненько так помер...'.format(self.name), color='red', attrs=['dark'])
        return True

    def eat(self):
        min_val = min(self.house.cat_food, 10)
        cprint('кот {} скушал {} еды'.format(self.name, min_val), color='yellow')
        self.house.cat_food -= min_val
        self.fullness += (min_val*2)

    def sleep(self):
        cprint('кот {} спал целый день'.format(self.name), color='green')
        self.fullness -= 10

    def soil(self):
        cprint('{} подрал обои'.format(self.name), color='blue')
        self.house.dirty += 5
        self.fullness -= 10

######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Human):

    def act(self):
        if not super(Child, self).act() and self.is_alive:
            self.sleep()
        return True

    def eat(self):
        super().eat(food_to_eat=10)

    def sleep(self):
        cprint('{} спал(-а) целый день'.format(self.name), color='green')
        self.fullness -= 10


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


serge = Husband(name='Сережа')
masha = Wife(name='Маша')
liza = Child(name='Лиза')

home = House()
serge.go_to_the_house(house=home)
masha.go_to_the_house(house=home)
liza.go_to_the_house(house=home)

barsik = Cat(name='Барсик')
masha + barsik

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')

    # проверка на статус зомби
    if not masha.is_alive and not masha.is_alive and not liza.is_alive and not barsik.is_alive:
        cprint('\n {txt: ^46}'.format(txt=' GAME OVER '), color='white', attrs=['dark'])
        cprint(' {txt: ^46}'.format(txt=' --------- '), color='white', attrs=['dark'])
        cprint(' {txt:^46}'.format(txt=' directed by '), color='white', attrs=['dark'])
        cprint(' {txt:^46}'.format(txt=' ROBERT B. WEIDE '), color='white', attrs=['dark'])
        break
    else:
        serge.act()
        masha.act()
        liza.act()
        barsik.act()
        home.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(liza, color='cyan')
    cprint(barsik, color='cyan')
    cprint(home, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

# зачет!