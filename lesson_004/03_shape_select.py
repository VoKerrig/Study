# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def vector_draw(point, angle, length):
    vector = sd.get_vector(start_point=point, angle=angle, length=length)
    vector.draw()
    return vector


def triangle(point=sd.get_point(250, 300), angle=30, length=100, any_angle=120):
    last_point = point
    for i in range(1, 4):
        vector = vector_draw(last_point, angle, length)
        last_point = vector.end_point
        angle += any_angle


def square(point=sd.get_point(250, 300), angle=30, length=100, any_angle=90):
    last_point = point
    for i in range(1, 5):
        vector = vector_draw(last_point, angle, length)
        last_point = vector.end_point
        angle += any_angle


def pentagon(point=sd.get_point(250, 300), angle=30, length=100, any_angle=72):
    last_point = point
    for i in range(1, 6):
        vector = vector_draw(last_point, angle, length)
        last_point = vector.end_point
        angle += any_angle


def hexagon(point=sd.get_point(250, 300), angle=30, length=100, any_angle=60):
    last_point = point
    for i in range(1, 7):
        vector = vector_draw(last_point, angle, length)
        last_point = vector.end_point
        angle += any_angle


text = {0: "Треугольник", 1: "Квадрат", 2: "Пятиугольник", 3: "Шестиугольник"}
for i in text:
    print(i, ":", text[i])

figure = input("Введите желаемую фигуру > ")
while True:
    if figure == "0":
        triangle()
    elif figure == "1":
        square()
    elif figure == "2":
        pentagon()
    elif figure == "3":
        hexagon()
    else:
        print("Вы ввели некорректую фигуру!")
    break

sd.pause()
