# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
import random
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код

# def wall(color, width):
#
#     for i in range(100, 701, 50):
#         sd.vector(
#             start=sd.get_point(0, 700 - i),
#             angle=0,
#             length=600,
#             color=color,
#             width=width
#         )
#     for z in range(0, 701, 100):
#         for t in range(0, 701, 50):
#             sd.vector(start=sd.get_point(z, 550 - t), angle=90, length=50, color=color, width=width)
#
#
# wall(sd.COLOR_ORANGE, 2)


def wall(color, width):
    raw_step = 50
    col_step = 100

    for num_r, raw in enumerate(range(100, 701, raw_step)):
        sd.vector(
            start=sd.get_point(0, 700 - raw),
            angle=0,
            length=600,
            color=color,
            width=5
        )

        for num, col in enumerate(range(0, 701, col_step)):
            start = 0
            if num_r % 2:
                start = -(col_step / 2) # col_step ширина кирпича

            x = col_step + col
            y = raw - col_step
            sd.vector(
                start=sd.get_point(start + x, y),
                angle=90,
                length=50,
                color=color,
                width=width
            )


wall(sd.COLOR_ORANGE, 5)


sd.pause()