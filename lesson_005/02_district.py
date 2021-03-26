# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from pprint import pprint

from district.central_street.house1 import room1 as cs1_1, room2 as cs1_2
from district.central_street.house2 import room1 as cs2_1, room2 as cs2_2
from district.soviet_street.house1 import room1 as ss1_1, room2 as ss1_2
from district.soviet_street.house2 import room1 as ss2_1, room2 as ss2_2

district = ",".join(cs1_1.folks), ",".join(cs1_2.folks), ",".join(cs2_1.folks), ",".join(cs2_2.folks),\
           ",".join(ss1_1.folks), ",".join(ss1_2.folks), ",".join(ss2_1.folks), ",".join(ss2_2.folks)

pprint(district)


