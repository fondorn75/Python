# 0. Вывести квадрат числа
from math import sin
from random import randint


def kvadrat(f, n):
    return f ** n


print(kvadrat(4, 2))


# 1. По двум заданным числам проверять является ли первое квадратом второго

def First_Kv_Second(a, b):
    if b * b == a:
        print("Число", a, "является квадратом числа", b)
    else:
        print("Число", a, "не является квадратом числа", b)


First_Kv_Second(25, 5)


# 2. Даны два числа. Показать большее и меньшее число

def Max_Min(first, second):
    if first > second:
        return first
    else:
        return second


print(Max_Min(10, 15))


# 3. По заданному номеру дня недели вывести его название

def Week_Day(day):
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days[day - 1]


print(Week_Day(7))


# 4. Найти максимальное из трех чисел

def MaxFromThreeNumbers(number):
    num1 = number // 100
    num2 = (number % 100) // 10
    num3 = number % 10
    if num1 > num2:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3


print(MaxFromThreeNumbers(358))


# 5. Написать программу вычисления значения функции y=f(a)

def FunkciaSin(a):
    return sin(a)


print(round(FunkciaSin(180), 2))


# 6. Выяснить является ли число чётным

def ChetNecet(number):
    if number % 2 == 0:
        return "четное"
    else:
        return "не четное"


print("Число", ChetNecet(55))


# 7. Показать числа от -N до N

def DiapasonN(n):
    list = {}
    j = 0
    for i in range(-n, n + 1):
        list[j] = i
        j += 1
    return list


print(DiapasonN(5))


# 8. Показать четные числа от 1 до N

def DiapasonChetN(n):
    list = {}
    j = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            list[j] = i
            j += 1
    return list


print(DiapasonChetN(6))


# 9. Показать последнюю цифру трёхзначного числа

def NumberEnd(number):
    return number % 10


print(NumberEnd(459))


# 10. Показать вторую цифру трёхзначного числа

def SecondNumber(number):
    return (number % 100) // 10


print(SecondNumber(347))


# 11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

def MaxNumberIn():
    temp = randint(10, 99)
    num1 = temp // 10
    num2 = temp % 10
    if num1 > num2:
        return f"В числе {temp} наибольшее {num1}"
    else:
        return f"В числе {temp} наибольшее {num2}"


print(MaxNumberIn())


# 12. Удалить вторую цифру трёхзначного числа

def DeleteSecondNumber(number):
    num1 = number // 100
    num2 = (number % 100) // 10
    num3 = number % 10
    return f"{num1}{num3}"


print(DeleteSecondNumber(452))


# 13. Выяснить, кратно ли число заданному, если нет, вывести остаток.

def MultipleNumber(num1, num2):
    if num1 * num1 == num2:
        return f"Число {num2} кратное {num1}"
    else:
        return f"Число {num2} не кратное {num1}"


print(MultipleNumber(5, 25))


# 14. Найти третью цифру числа или сообщить, что её нет

def ThreeNumber(number):
    temp = (number % 100) % 10
    if number // 100 != 0:
        return f"Третья цифра - {temp}"
    else:
        return "Третьей цифры нет"


print(ThreeNumber(463))