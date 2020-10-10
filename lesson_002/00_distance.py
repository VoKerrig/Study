#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = dict()

Moscow = sites['Moscow']
London = sites['London']
Paris = sites['Paris']
Moscow_London = ((Moscow [0] - London [0]) ** 2 + (Moscow [1] - London [1]) ** 2) ** .5
London_Paris = ((London [0] - Paris [0]) ** 2 + (London [1] - Paris [1]) ** 2) ** .5
Moscow_Paris = ((Moscow [0] - Paris [0]) ** 2 + (Moscow [1] - Paris [1]) ** 2) ** .5

distances['Moscow'] = {}
distances['Moscow']['London'] = Moscow_London
distances['Moscow']['Paris'] = Moscow_Paris

distances['London'] = {}
distances['London']['Paris'] = London_Paris
print(distances)
dfgdfg






