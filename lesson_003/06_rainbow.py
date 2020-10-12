# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
# c = -1
# for i in range(10, 70, 5):
#     if c >= 6:
#         break
#     c += 1
#     sd.line(start_point=sd.get_point(50 + i, 50), end_point=sd.get_point(350 + i, 450), color=rainbow_colors[c], width=2)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
point = sd.get_point(200, -200)
radius = 500
colors = -1
for i in range(10, 71, 10):
    radius += 30
    colors += 1
    if colors >= 7:
        break

    sd.circle(center_position=point, radius=radius, width=30, color=rainbow_colors[colors])
sd.pause()
