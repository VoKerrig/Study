#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['mom', 'dad', 'sister', 'brother', 'grandmother']
print(my_family)

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    ['mom', 175],
    ['dad', 180],
    ['sister', 178],
    ['brother', 186],
    ['grandmother', 170]
]
print(my_family_height)
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
dad = my_family_height[1]
height_dad = dad[1]
print('Рост отца - ', height_dad, 'см')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
mom = my_family_height[0]
sister = my_family_height[2]
brother = my_family_height[3]
grandmother = my_family_height[4]
height_mom = mom[1]
height_sister = sister[1]
height_brother = brother[1]
height_grandmother = grandmother[1]
family_height = height_dad + height_mom + height_sister + height_brother + height_grandmother
print('Общий рост моей семьи - ', family_height, 'см')