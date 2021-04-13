# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


from random import randint
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.cat = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 20:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.food -= 20
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def clean(self):
        cprint('{} убрался дома'.format(self.name), color='yellow')
        self.house.dirt -= 100
        self.fullness -= 20

    def take_cat(self):
        cprint('{} взял кота'.format(self.name), color='yellow')
        cat = Cat(name="Кобан", house=self.house)
        self.cat = cat

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if not self.cat:
            self.take_cat()
        if self.house.money >= 50 and self.house.food <= 20:
            cprint('{} сходил в магазин за едой для себя'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        elif self.cat and self.house.money >= 50 and self.house.cat_food <= 10:
            cprint('{} сходил в магазин за едой для кота'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food <= 10 or self.house.cat_food <= 10 and self.cat:
            self.shopping()
        elif self.house.money <= 50:
            self.work()
        elif self.house.dirt >= 100:
            self.clean()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 50
        self.cat_food = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, кошачьей еды {}, степень загрязнения {}'.format(
            self.food, self.money, self.cat_food, self.dirt)


class Cat:

    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.house = house

    def __str__(self):
        return 'Кот - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')
            self.sleep()

    def sleep(self):
        cprint('{} спит'.format(self.name), color='red')
        self.fullness -= 10

    def wallpaper(self):
        cprint('{} подрал обои'.format(self.name), color='cyan')
        self.fullness -= 10
        self.house.dirt += 5

    # def go_to_the_house(self, house):
    #     self.house = house
    #     self.fullness -= 10
    #     cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.wallpaper()
        else:
            self.sleep()


citizens = [
    Man(name='Парень')
]

my_sweet_home = House()
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

for day in range(1, 366*5):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        if isinstance(citisen, Man) and citisen.cat and len(citizens) == 1:
            citizens.append(citisen.cat)
        citisen.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
