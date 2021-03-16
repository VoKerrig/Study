# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1280, 720)

root_point = sd.get_point(600, 90)


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


# def draw_branches(point, angle, length):
#     if length < 10:
#         return
#     line_1 = sd.get_vector(start_point=point, angle=angle, length=length)
#     line_1.draw()
#     line_2 = sd.get_vector(start_point=point, angle=angle, length=length)
#     line_2.draw()
#     delta = 30
#     next_point = line_1.end_point
#     next_point_2 = line_2.end_point
#     next_angle = angle - delta
#     next_angle_2 = angle + delta
#     next_length = length * 0.75
#     draw_branches(point=next_point, angle=next_angle, length=next_length)
#     draw_branches(point=next_point_2, angle=next_angle_2, length=next_length)
#
#
# draw_branches(point=root_point, angle=90, length=100)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

#
def draw_branches(point, angle, length):
    if length < 3:
        return
    line_1 = sd.get_vector(start_point=point, angle=angle, length=length)
    line_1.draw()
    line_2 = sd.get_vector(start_point=point, angle=angle, length=length)
    line_2.draw()
    delta = 30 + sd.random_number((-30*40/100), (30*40/100))
    next_point = line_1.end_point
    next_point_2 = line_2.end_point
    next_angle = angle - delta
    next_angle_2 = angle + delta
    next_length = length * (sd.random_number(-0.75*20, 0.75*20)/100 + 0.75)
    draw_branches(point=next_point, angle=next_angle, length=next_length)
    draw_branches(point=next_point_2, angle=next_angle_2, length=next_length)


draw_branches(point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.random_number()

sd.pause()
