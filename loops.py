# print('Loops')

# a=int(input("Enter first digit:"))
# b=int(input("Enter second digit"))

# if a > b:
#     print("a>b")
# elif a < b:
#     print("a<b")
# else:
#     print("a=b")
#     print("test")


# def say_hello():
#     name=input("Enter your name")
#     print("Hello", name)

# say_hello()

# def plus(a, b):
#     return a + b

# sum = plus(13,4)
# print(sum)

# def plus(*params): #коли не знаємо наперед скільки аргументів приймає функція
#     print(params)
#     res=0
#     for item in params:
#         res += item
#     return res

# sum=plus(2,4,4,4)
# print("SUM=>",sum)


# Протягом тижня вимірювали температуру повітря. Знайти кількість днів, коли температура перевищувала 10o С.


# day=0
# counter=0

# while True:
#     if day==7:
#         break
#     temp=int(input("Enter temperature day"))
#     day+=1
#     if temp>10:
#         counter += 1

# print("Temperature more than 10:", counter, "times.")


# Вивести на екран таблицю множення на задане із клавіатури число.

# digit=int(input("Enter the digit 1-10"))

# for i in range(1,11):
#     print(digit*i)


# Комп’ютер кидає кубик(за допомогою генератора випадкових чисел). Порахувати через скільки спроб випаде шістка.


# from random import randint

# trying = 1

# while True:
#     rand=randint(1,6)
#     print(rand)
#     if rand != 6:
#         trying += 1
#     else:
#         break

# print("Try number", trying)


# Гра у кості. Гравці(комп’ютер і людина) кидають по 2 кубики. У кого сума на кубиках більша, той заробляє 1 бал. Якщо на кубиках дубль(подвоєння, тобто дві четвірки і т.і.), то гравець додатково заробляє 2 бали. Гра закінчується при наборі одним із гравцем N балів.

# from random import randint

# exit=True
# score=0

# while exit:
#     dice1_player=randint(1,6)
#     dice2_player=randint(1,6)
#     print("Ваш перший кубик: ",dice1_player)
#     print("Ваш другий кубик: ", dice2_player)
#     sum_player=dice1_player+dice2_player
#     print("Сума очок гравця", sum_player)

#     dice1_comp=randint(1,6)
#     dice2_comp=randint(1,6)
#     print("Перший кубик компютера: ", dice1_comp)
#     print("Другий кубик компютера: ", dice2_comp)
#     sum_comp=dice1_comp+dice2_comp
#     print("Сума очок компютера",sum_comp)

#     if sum_player>sum_comp:
#         score+=1
#         print("Вітаю! Ви перемогли!",score)
#     elif sum_player<sum_comp:
#         score+=1
#         print("Перемога компютера :(",score)
#     elif dice1_player==dice2_player:
#         score+=2
#     elif dice1_comp==dice2_comp:
#         score+=2
#     else:
#         print("Нічия!", score)
#         exit=False

# https://github.com/xRedDragonx/py_virtual_dice/blob/master/virtual_dice.py


# Написати функцію, яка отримує відстань, яку пробіг спортсмен та час пробігу і повертає швидкість спортсмена. Відстань та час пробігу вводяться користувачем

# distance = int(input("Введіть відстань яку пробіг спортсмен, км "))
# time=int(input("Введіть час пробігу, хв "))

# def speed(distance, time):
#     return distance/(time/60)

# print("Швидкість спортсмена: ",speed(distance,time)," км/год")


# Написати функцію, яка обчислює вартість поїздки на автомобілі на дачу (туди і назад). Вхідними даними є: відстань до дачі (км); кількість бензину, яку споживає автомобіль на 100 км пробігу; ціна одного літру бензину. Дані для розрахунків вводяться користувачем.

# distance=int(input("Введіть відстань до дачі, км "))
# petrol=int(input("Кількість бензину, яку споживає автомобіль на 100 км пробігу, л "))
# price=int(input("Ціна за літр бензину, грн "))

# def price_per_trip(distance,petrol,price):
#     x=petrol/100 #трата бензину на 1 км
#     return 2*distance*x*price

# print("Вартість поїздки туди і назад становить", price_per_trip(distance,petrol,price), " грн")


# Написати функцію, яка отримує дату (день, місяць) і виводить назву свята, що випадає на цей день (наприклад, 7.01 – Різдво, 9.05 – День Перемоги). Запрограмувати реакцію програми на 4 – 5 свят.

day = input("Введіть день ")
month = input("Введіть номер місяця (01) ")


def holiday(day, month):
    if day == "7" and month == "01":
        print("Різдво")
    elif day == "9" and month == "05":
        print("День перемоги")
    elif day == "19" and month == "12":
        print("День Святого Миколая")
    elif day == "19" and month == "01":
        print("Святе Водохреща")
    elif day == "8" and month == "03":
        print("Міжнародний день жінок")
    else:
        print("Не припадає свят на цей день:(")


holiday(day, month)
