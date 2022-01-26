# 1. Вывести квадрат числа
from math import sin
from random import randint


def kvadrat(f, n):
    return f ** n


print(kvadrat(4, 2))


# 2. По двум заданным числам проверять является ли первое квадратом второго

def First_Kv_Second(a, b):
    if b * b == a:
        print("Число", a, "является квадратом числа", b)
    else:
        print("Число", a, "не является квадратом числа", b)


First_Kv_Second(25, 5)


# 3. Даны два числа. Показать большее и меньшее число

def Max_Min(first, second):
    if first > second:
        return first
    else:
        return second


print(Max_Min(10, 15))


# 4. По заданному номеру дня недели вывести его название

def Week_Day(day):
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days[day - 1]


print(Week_Day(7))


# 5. Найти максимальное из трех чисел

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


# 6. Написать программу вычисления значения функции y=f(a)

def FunkciaSin(a):
    return sin(a)


print(round(FunkciaSin(180), 2))


# 7. Выяснить является ли число чётным

def ChetNecet(number):
    if number % 2 == 0:
        return "четное"
    else:
        return "не четное"


print("Число", ChetNecet(55))


# 8. Показать числа от -N до N

def DiapasonN(n):
    list = {}
    j = 0
    for i in range(-n, n + 1):
        list[j] = i
        j += 1
    return list


print(DiapasonN(5))


# 9. Показать четные числа от 1 до N

def DiapasonChetN(n):
    list = {}
    j = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            list[j] = i
            j += 1
    return list


print(DiapasonChetN(6))


# 10. Показать последнюю цифру трёхзначного числа

def NumberEnd(number):
    return number % 10


print(NumberEnd(459))


# 11. Показать вторую цифру трёхзначного числа

def SecondNumber(number):
    return (number % 100) // 10


print(SecondNumber(347))


# 12. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

def MaxNumberIn():
    temp = randint(10, 99)
    num1 = temp // 10
    num2 = temp % 10
    if num1 > num2:
        return f"В числе {temp} наибольшее {num1}"
    else:
        return f"В числе {temp} наибольшее {num2}"


print(MaxNumberIn())


# 13. Удалить вторую цифру трёхзначного числа

def DeleteSecondNumber(number):
    num1 = number // 100
    num2 = (number % 100) // 10
    num3 = number % 10
    return f"{num1}{num3}"


print(DeleteSecondNumber(452))

# 14. Выяснить, кратно ли число заданному, если нет, вывести остаток.



# 15. Найти третью цифру числа или сообщить, что её нет
