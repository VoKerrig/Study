#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
zoo.insert(1, 'bear')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
new_zoo = zoo + birds
print(new_zoo)

# уберите слона
#  и выведите список на консоль
new_zoo.remove('elephant')
print(new_zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
jail_lion = new_zoo.index('lion') + 1
jail_lark = new_zoo.index('lark') + 1
print('Лев сидит в клетке под номером', jail_lion)
print('Жаворонок сидит в клетке под номером', jail_lark)


