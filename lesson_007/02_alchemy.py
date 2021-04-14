# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:

    def __init__(self):
        self.name = "Вода"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if type(other) == Air:
            return Storm()


class Air:

    def __init__(self):
        self.name = "Воздух"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if type(other) == Fire:
            return Lighting()
        if type(other) == Earth:
            return Dust()


class Fire:

    def __init__(self):
        self.name = "Огонь"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if type(other) == Water:
            return Steam()
        if type(other) == Earth:
            return Lava()


class Earth:

    def __init__(self):
        self.name = "Земля"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if type(other) == Water:
            return Dirt()


class Storm:

    def __init__(self):
        self.name = "Шторм"

    def __str__(self):
        return self.name


class Steam:

    def __init__(self):
        self.name = "Пар"

    def __str__(self):
        return self.name


class Dirt:

    def __init__(self):
        self.name = "Грязь"

    def __str__(self):
        return self.name


class Lighting:

    def __init__(self):
        self.name = "Молния"

    def __str__(self):
        return self.name


class Dust:

    def __init__(self):
        self.name = "Пыль"

    def __str__(self):
        return self.name


class Lava:

    def __init__(self):
        self.name = "Лава"

    def __str__(self):
        return self.name


print(Water(), "+", Air(), "=", Water() + Air())
print(Fire(), "+", Water(), "=", Fire() + Water())
print(Earth(), "+", Water(), "=", Earth() + Water())
print(Air(), "+", Fire(), "=", Air() + Fire())
print(Air(), "+", Earth(), "=", Air() + Earth())
print(Fire(), "+", Earth(), "=", Fire() + Earth())
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
