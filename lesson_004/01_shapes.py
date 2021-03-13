# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


def triangle(point, angle, length):
    l1 = sd.get_vector(start_point=point, angle=angle + 30, length=length)
    l1.draw()
    l2 = sd.get_vector(start_point=l1.end_point, angle=angle + 150, length=length)
    l2.draw()
    l3 = sd.get_vector(start_point=l2.end_point, angle=angle + 270, length=length)
    l3.draw()


triangle(point = sd.get_point(100, 100), angle = 0, length = 100)


def square(point, angle, length):
    l1 = sd.get_vector(start_point=point, angle=angle + 30, length=length)
    l1.draw()
    l2 = sd.get_vector(start_point=l1.end_point, angle=angle + 120, length=length)
    l2.draw()
    l3 = sd.get_vector(start_point=l2.end_point, angle=angle + 210, length=length)
    l3.draw()
    l4 = sd.get_vector(start_point=l3.end_point, angle=angle + 300, length=length)
    l4.draw()


square(point=sd.get_point(400, 100), angle=0, length=100)


def pentagon(point, angle, length):
    l1 = sd.get_vector(start_point=point, angle=angle + 30, length=length)
    l1.draw()
    l2 = sd.get_vector(start_point=l1.end_point, angle=angle + 102, length=length)
    l2.draw()
    l3 = sd.get_vector(start_point=l2.end_point, angle=angle + 174, length=length)
    l3.draw()
    l4 = sd.get_vector(start_point=l3.end_point, angle=angle + 246, length=length)
    l4.draw()
    l5 = sd.get_vector(start_point=l4.end_point, angle=angle + 318, length=length)
    l5.draw()


pentagon(point=sd.get_point(100, 400), angle=0, length=100)


def hexagon(point, angle, length):
    l1 = sd.get_vector(start_point=point, angle=angle + 30, length=length)
    l1.draw()
    l2 = sd.get_vector(start_point=l1.end_point, angle=angle + 90, length=length)
    l2.draw()
    l3 = sd.get_vector(start_point=l2.end_point, angle=angle + 150, length=length)
    l3.draw()
    l4 = sd.get_vector(start_point=l3.end_point, angle=angle + 210, length=length)
    l4.draw()
    l5 = sd.get_vector(start_point=l4.end_point, angle=angle + 270, length=length)
    l5.draw()
    l6 = sd.get_vector(start_point=l5.end_point, angle=angle + 330, length=length)
    l6.draw()

hexagon(point=sd.get_point(400, 400), angle=0, length=100)
# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
