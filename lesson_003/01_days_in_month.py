# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
# year = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']
if month == 1 or month == 3 or month == 5 or month == 7 or month == 9 or month == 11:
    print('31')
elif month == 4 or month == 6 or month == 8 or month == 10 or month == 12:
    print('30')
elif month == 2:
    print('28')
else:
    print('Номер месяца не распознан')
# print('Вы ввели', month)


