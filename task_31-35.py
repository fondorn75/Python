# 11. Для натурального N создать множество: 1, -3, 9, -27, 81 и т.д.

from posixpath import split


def NaturalN(N):
    list = set()
    for i in range (N):
        list.add(3**i)
    return sorted(list)



print(NaturalN(6))

# 12. Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3k + 1.


def DictionaryN(n):
    result = {}
    for k in range(1, n+1):
        result[k] = 3*k+1
    return result


print(DictionaryN(6))

# 13. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

def UserString():
    str1 = input("Введите перву строку: ")
    str2 = input("Введите вторую строку: ")
    result = int(str1.count(str2))
    return result

print(UserString())

# 14. Подсчитать сумму цифр в вещественном числе.

def SummaNumbers(number):
    tmp = str(number)
    temp = tmp.split('.')
    num1 = int(temp[0])
    num2 = int(temp[1])
    summa = 0
    while (num1 != 0): # складываем числа целой части
        summa += num1 % 10
        num1 = num1 // 10
    while (num2 != 0): # складываем числа дробной части
        summa += num2 % 10
        num2 = num2 // 10
    return summa

print(SummaNumbers(2456.4587))

# 15. Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

def MultiplayNumbers(N):
    list = []
    tmp = 1
    j = 0
    for i in range (1, N+1):
        list.append(i*tmp)
        tmp = list[j]
        j += 1
    return list

print(MultiplayNumbers(5))