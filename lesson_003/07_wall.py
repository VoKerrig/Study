# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd


# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
def horizon_line():
    space = 0
    for step in range(0, 1000, 50):
        space += step
        start = sd.get_point(0, 50 + step)
        end = sd.get_point(1000, 50 + step)
        sd.line(start_point=start, end_point=end, width=1)


def vertical_line():
    space = 0
    for i, step_y in enumerate(range(0, 1000, 50)):
        if i % 2 == 0:
            step_x = 50
        else:
            step_x = 0

        for i, step in enumerate(range(0, 1000, 100)):
            space += step
            start = sd.get_point(step + step_x, step_y)
            end = sd.get_point(step + step_x, 50 + step_y)
            sd.line(start_point=start, end_point=end, width=1)


horizon_line()
vertical_line()

sd.pause()
