# 21. Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.

from operator import index


def SecondNumber():
    list = ["ab", "adsf", "thfg", "fgjty", "hdfn", "ab", "afsde"]
    str = "ab"
    tmp = 0
    pos = 0
    for i in list:
        if str == i:
            tmp += 1
        if tmp == 2:
            return f"Второ вхождение в списке на позиции - {pos}"
        pos += 1


print(SecondNumber())

# 22. Найти сумму чисел списка стоящих на нечетной позиции


lst = [2, 3, 6, 3, 7, 9, 4, 6, 5]


def SummNumberInList():
    temp = []
    for i in range(0, len(lst), 2):
        temp.append(lst[i])
        result = sum(temp)
    return f"Сумма чисел списка стоящих на нечетной позиции равна - {result}"


print(SummNumberInList())


# 23. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#     Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

def PairInList():
    lst = [2, 3, 4, 5, 6]
    lst2 = []
    j = 0
    temp = lst[-1]
    for i in range(0, len(lst) // 2):
        temp = lst[i] * lst[:-i]
        lst2[j] = temp
        j += 1
    return lst2


print(PairInList())


# 24. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
#     Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

numbers = [1.1, 1.2, 3.1, 5, 10.01]


def RealNumbers():
    result = []
    for i in numbers:
        temp = round(i % 1, 2)
        if temp != 0:
            result.append(temp)
    substraction = max(result) - min(result)
    return f"Разница между максимальным и минимальным значением дробной части элементов - {substraction}"


print(RealNumbers())

# 25. Написать программу преобразования десятичного числа в двоичное


def DecimalNumber(number):
    return f"Число {number} в двоичном виде - {number :0b}"


print(DecimalNumber(101))
