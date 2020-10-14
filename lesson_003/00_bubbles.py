# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# point = sd.get_point(200, 400)
# radius = 50
# for _ in range(3):
#     radius += 25
#     sd.circle(center_position=point, radius=radius)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point, step, color):
    radius = 50
    for _ in range(5):
        radius += step
        sd.circle(center_position=point, color=sd.random_color(), radius=radius, width=3)

point = sd.get_point(200, 400)
bubble(point=point, step=10, color=sd.random_color())

# # Нарисовать 10 пузырьков в ряд
# for x in range(100, 1001, 100):
#     point2 = sd.get_point(x, 100)
#     bubble(point=point2, step=5)
#
# # Нарисовать три ряда по 10 пузырьков
# for y in range(100, 301, 100):
#     for x in range(100, 1001, 100):
#         point = sd.get_point(x, y)
#         bubble(point=point, step=5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    color = sd.random_color()
    bubble(point=point, step=5, color=sd.random_color())

sd.pause()


