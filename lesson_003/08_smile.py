# -*- coding: utf-8 -*-

# (определение функций)
import random
import simple_draw as sd

sd.resolution = (1200, 1000)


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
def smile(x, y, color):
    glass = 0
    slope = 0
    empty = 0
    negation = 0
    sd.circle(center_position=sd.get_point(x - negation, y), radius=100, color=color, width=4)
    negation = 40
    for i in range(2):
        sd.circle(center_position=sd.get_point(x + glass - negation, y), radius=15, color=sd.COLOR_YELLOW, width=0)
        glass += 90
        negation = 50
    for z in range(2):
        sd.line(start_point=sd.get_point(x + empty - negation, y + slope - negation),
                end_point=sd.get_point(x - negation, y - negation), color=sd.COLOR_RED, width=4)
        # slope += 0
        empty += 100
        negation = 50


for _ in range(10):
    x = random.randint(300, 1000)
    y = random.randint(300, 1000)
    smile(x=x, y=y, color=sd.COLOR_YELLOW)

sd.pause()
