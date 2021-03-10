# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(point, color):
    sd.circle(center_position=point, color=color, radius=50, width=1)


def lines():
    sd.lines(point_list=(sd.get_point(1, 20), sd.get_point(20, 10), sd.get_point(40, 10), sd.get_point(60, 20)), color=sd.COLOR_GREEN)


for _ in range(10):
    point = sd.random_point()
    color = sd.COLOR_GREEN
    smile(point=point, color=color)

lines()

sd.pause()
