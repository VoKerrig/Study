# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

text = {0: "red", 1: "orange", 2: "yellow", 3: "green", 4: "cyan", 5: "blue", 6: "purple"}
for i in text:
    print(i, ":", text[i])

colors = input("Введите желаемый цвет > ")
while True:
    if colors == "0":
        colors = sd.COLOR_RED
    elif colors == "1":
        colors = sd.COLOR_ORANGE
    elif colors == "2":
        colors = sd.COLOR_YELLOW
    elif colors == "3":
        colors = sd.COLOR_GREEN
    elif colors == "4":
        colors = sd.COLOR_CYAN
    elif colors == "5":
        colors = sd.COLOR_BLUE
    elif colors == "6":
        colors = sd.COLOR_PURPLE
    else:
        colors = sd.COLOR_YELLOW
        print("Вы ввели некорректный номер!")
    break


def vector_draw(point, angle, length):
    vector = sd.get_vector(start_point=point, angle=angle, length=length)
    vector.draw(color=colors)
    return vector


def triangle(point=sd.get_point(100, 100), angle=30, length=100, any_angle=120):
    last_point = point
    for i in range(1, 4):
        vector = vector_draw(last_point, angle, length)
        last_point = vector.end_point
        angle += any_angle


triangle()


def square(point=sd.get_point(400, 100), angle=30, length=100, any_angle=90):
    last_point = point
    for i in range(1, 5):
        vector = vector_draw(last_point, angle, length)
        last_point = vector.end_point
        angle += any_angle


square()


def pentagon(point=sd.get_point(100, 400), angle=30, length=100, any_angle=72):
    last_point = point
    for i in range(1, 6):
        vector = vector_draw(last_point, angle, length)
        last_point = vector.end_point
        angle += any_angle


pentagon()


def hexagon(point=sd.get_point(400, 400), angle=30, length=100, any_angle=60):
    last_point = point
    for i in range(1, 7):
        vector = vector_draw(last_point, angle, length)
        last_point = vector.end_point
        angle += any_angle


hexagon()

sd.pause()
